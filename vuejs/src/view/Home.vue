<template>
    
    <v-row no-gutters class="body">
      <v-col md="8">

      <side-bar :paymentDone="paymentDone" @toOrder="createOrder"/>

      </v-col>
      <v-col md="4">

        <side-bar-right v-on:paymentName="getPaymentName"/>

      </v-col>
    </v-row>

</template>

<script>
import SideBar from '../components/HomePage/SideBar.vue'
import SideBarRight from '../components/HomePage/SideBarRight.vue'
import axios from 'axios';




export default {
  components: {SideBar, SideBarRight},
  name: 'Home-vue',
  data: () => ({
    paymentName: '',
    products: [],
    totalPrice: 0,
    paymentDone: false
  }),
  methods: {
    
    createOrder(products, totalPrice) {
      this.products = products;
      this.totalPrice = totalPrice;
      console.log(this.products, this.totalPrice);
    },
    getPaymentName(name) {
      this.paymentName = name;
      let user_id = JSON.parse(localStorage.user).id;
      console.log(user_id);
      const orderDetails = this.products.map(product => {
        return {
          product_id: product.id,
          pay_method: name,
          total_price: this.totalPrice,
        }
      });
      console.log(orderDetails);
        axios.post(`http://127.0.0.1:8000/orders`, {
          user_id: user_id,
          order_details: orderDetails
        })
        .then(response => {
          response.data;
          this.paymentDone = true;
          alert("thanh toan thanh cong");
          
        })
        .catch(e => {
          console.log(e);        
        })
    },
  },
}

</script>

<style>

</style>