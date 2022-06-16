<template>
  <div>
  <headerr  v-on:addProduct="addProductParent"/>
  <v-card class="makeBorder"> 
    <v-table
    fixed-header
    height="660px"
    theme= "this.$vuetify.theme.themes.dark.background"
  >
    <thead>
      <tr>
        <th class="text-left" style="font-size: 20px">
          Name
        </th>
        <th class="text-left" style="font-size: 20px">
          Quantily
        </th>
        <th class="text-left" style="font-size: 20px">
          Price
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in products"
        :key="item.id"
      >
        <td>{{ item.product_name }}</td>
        <td>
          <v-btn 
            class="mx-2"
            icon
            color="secondary"
            size="x-small"
            @click="rmProductToList(item.id); totalPrice()"
          > 
          <v-icon icon="fas fa-minus" class="icon"  ></v-icon>
          </v-btn>
            {{ item.quantity }}
          <v-btn 
            class="mx-2"
            icon
            color="secondary"
            size="x-small"
            @click="addProductToList(item.id); totalPrice()"
          > 
          <v-icon icon="fas fa-plus" class="icon"  ></v-icon>
          </v-btn>
        </td>
        <td>{{ item.price }}</td>
      </tr>
    </tbody>
  </v-table>
  </v-card>

  <v-card class="bottom"> 
    <v-row no-gutters>
      <v-col
        md="4"
      >
        <v-card
          class="pa-2 card-bottom"
          outlined
          tile
          color="#EEEEEE"
        >
          <p style="font-weight: bold; font-size: 25px">Tổng tiền</p>
        </v-card>
      </v-col>
      <v-col
        md="8"
      >
        <v-card
          class="pa-2 card-bottom"
          outlined
          tile
          style="border-left: 1px solid black; "
          color="#EEEEEE"
        >
          <p style="font-weight: bold; font-size: 25px"> {{ total }} </p>
        </v-card>
      </v-col>
    </v-row>
  </v-card>


  </div>


</template>

<script>
import Headerr from './Headerr.vue';
import axios from 'axios';
export default {
  components: { Headerr },
    name: 'sidebar-vue',
    // props: {
    //   test1: {
    //   type: Function,
    //   default() {
    //     return {}
    //   }}
    // },
    data: () => ({
      width: 300,
      aspectRatio: 16 / 9,
      aspectRatios: [
        {
          title: '16/9',
          value: 16 / 9,
        },
        {
          title: '4/3',
          value: 4 / 3,
        },
        {
          title: '1/1',
          value: 1,
        },
      ],
      products: [],
      total: 0,

    }),
    props: ["paymentDone"],
    methods: {
      getProduct(id) {
        axios.get(`http://127.0.0.1:8000/products/${id}`)
        .then(response => {
          response.data.quantity = 1;
          this.products.push(response.data);
        })
        .catch(e => {
          console.log(e);        
        })
      },
      addProductToList(id) {
        for (let i in this.products) {
          if(this.products[i].id == id) { 
            let temp = this.products[i].price / this.products[i].quantity;
            this.products[i].quantity += 1;
            this.products[i].price = this.products[i].quantity * temp;
          }
        }
      },

      rmProductToList(id) {
        for (let i in this.products) {
          if (this.products[i].id == id) {
            if(this.products[i].quantity <= 1) { this.products = this.products.filter(item =>  item.id != id ) }
            else {
              let temp = this.products[i].price / this.products[i].quantity;
              this.products[i].quantity -= 1;
              this.products[i].price = this.products[i].quantity * temp;
            }
          }
        }
      },

      totalPrice() {
        this.total = 0;
        for (let i in this.products) {
            this.total += this.products[i].price;
        }
      },

      addProductParent(productId) {
        if (this.products.length <= 0) {
          this.getProduct(productId);
        } else {
          let checked = false; // check xem phan tu co trong mang hay chua
          for (let i in this.products) {
            if (this.products[i].id == productId) {
              checked=true;
            }
          }

        if(checked == true) { // neu da co trong mang ==> tim va tang so luong
          for (let i in this.products) {
            if(this.products[i].id == productId) {
            let temp = this.products[i].price / this.products[i].quantity;
            this.products[i].quantity += 1;
            this.products[i].price = this.products[i].quantity * temp;
            this.totalPrice();
            }
          }
          } else {
          this.getProduct(productId);
          }
        }
      },

      passDataToOrder() {
        this.$emit('toOrder', this.products, this.total);
      }

    }, 
  computed: {
    productsLength() {
      return this.products.length
    },

  },
  watch: {
    productsLength () {
      this.totalPrice();
    },
    total() {
      this.passDataToOrder();
    },
    paymentDone() {
      if(this.paymentDone) {
        console.log(this.paymentDone);
        this.products = [];
        this.total = 0;
      }
    }
  }
}

</script>

<style scoped>
.search{
  max-width: 1000px;
}

.test {
  position: relative;
  top: 5px;
  right: 125px;
}

.icon{
  font-size: 15px;
}

.makeBorder {
  border-bottom: 1px solid black;
  border-right: 1px solid black;
}

.bottom {
  border-top: 1px solid black;
  border-right: 1px solid black;
  background-color: springgreen;
}

.card-bottom {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 75px;
}
</style>