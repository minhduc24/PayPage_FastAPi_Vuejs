<template>

<v-card
    class="mx-auto"
    outline
    color="pink"
  >
    <v-card-title > 
      <p style="font-size: 30px" class="my-5"> Phương Thức Thanh Toán </p>
    </v-card-title>

    <v-card-text>
      <v-row
      justify="center"
      v-for="item in payMethods"
      :key="item.id"
      style="height: 150px;"

    >
      <v-col>
        <v-card
        class="mx-auto pay-method"
        :prepend-avatar= "item.image"
        max-width="300"
        @click="getPayMethod(item.id)"
        :class="{payChoose: item.state}"
      >
      <template v-slot:title>
        {{item.name}}
      </template>
      </v-card>
      </v-col>
    </v-row>
    </v-card-text>

    <v-divider color="black"></v-divider>

    <v-card-actions>
      <v-row no-gutters="">
        <v-col>
          <v-btn 
            variant="outlined" 
            class="pa-5 pay-btn "
            height="60" 
            width="200"  
          >
            <p style="font-size: 20px">   Hủy   </p>
          </v-btn>
        </v-col>

        <v-spacer></v-spacer>

        <v-col>
          <v-btn 
            variant="outlined" 
            class="pa-5 pay-btn "
            height="60"  
            width="200"
            @click="sendPaymentName"
          >
            <p style="font-size: 20px" > Thanh Toán </p>
          </v-btn>
        </v-col>
      </v-row>
    </v-card-actions>
  </v-card>

</template>

<script>
export default {
    name: 'sidebarRight-vue',
    data: () => ({
      payMethods: [
        { 
          id: 1,
          image: 'https://play-lh.googleusercontent.com/dQbjuW6Jrwzavx7UCwvGzA_sleZe3-Km1KISpMLGVf1Be5N6hN6-tdKxE5RDQvOiGRg',
          name: 'MoMo',
          state: false,
        },
        { 
          id: 2,
          image: 'https://cardtot.com/wp-content/uploads/2022/03/shopeepay.jpg',
          name: 'ShopeePay',
          state: false,
        },
        {
          id: 3,
          image: 'https://play-lh.googleusercontent.com/ddHMBgdUl2T2oWLVF71CPpUYuBvTjoDVDoZxytHR5b0XCHpj0GKfzLqsftWd9xGz9Q',
          name: 'Viettel Money',
          state: false,
        },
        { 
          id: 4,
          image: 'https://downloadlogomienphi.com/sites/default/files/logos/download-logo-vector-vnpayqr-noqr-mien-phi.jpg',
          name: 'VNPAY-QR',
          state: false,
        },
      ],
      paymentName: ''
      
    }),
    methods: {
      getPayMethod(id) {
        if(this.payMethods[id - 1].state == false) {
          this.payMethods[id - 1].state = true;
          for (let i in this.payMethods) {
            if(i != (id - 1)) this.payMethods[i].state = false;
          }
        }
        this.paymentName = this.payMethods[id-1].name;
      },
      sendPaymentName(event) {
         event.preventDefault();
        this.$emit('paymentName', this.paymentName);
        
      }
    }

}
</script>

<style scoped>

.pay-method {
  cursor: pointer;
}

.pay-btn {
  background-color: turquoise;
}

.payChoose {
  background-color: cyan;
}



</style>