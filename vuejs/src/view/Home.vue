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
    },
    getPaymentName(name) {

      let user = JSON.parse(localStorage.user);
      user.accumulate_points += this.totalPrice;
      this.totalPrice = user.accumulate_points;
      localStorage.user = JSON.stringify(user)

      let user_id = user.id;
      this.paymentName = name;
      const orderDetails = this.products.map(product => {
        return {
          product_id: product.id,
          pay_method: name,
          total_price: this.totalPrice,
        }
      });
        axios.post(`http://127.0.0.1:8000/orders`, {
          user_id: user_id,
          order_details: orderDetails
        })
        .then(response => {
          response.data;
          this.paymentDone = true;
          alert("thanh toan thanh cong");
          location.reload();
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