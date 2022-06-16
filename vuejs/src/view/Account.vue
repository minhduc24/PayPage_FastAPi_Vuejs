<template>
<div>
    <v-app-bar app dark color="blue">
      <v-toolbar-title>Login Page</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text rounded>
        <router-link to="/"><p>HOME</p></router-link>
        </v-btn>
    </v-app-bar>

      <v-card width="500" class="mx-auto mt-9">
        <v-card-title>Đăng nhập</v-card-title>
        <v-card-text>
          <v-text-field
           label="Nhập ID" 
           prepend-icon="mdi-account-circle"
           v-model="userId"
           />
        </v-card-text>

        <v-divider></v-divider>
        <v-card-actions class="mb-5">
          <v-btn color="info" @click="getUser">Login</v-btn>
        </v-card-actions>


      <v-alert
      dense
      text
      type="success"
      v-if="check2"
    >
      Bạn đã đăng nhập thành công
    </v-alert>

      <v-alert
      dense
      outlined
      type="error"
      v-if="check1"
    >
      Đăng nhập thất bại
    </v-alert>

      </v-card>

      
</div>
    
</template>

<script>
  import axios from 'axios';
  export default{
  components: {  },
    name: 'AccountVue',
    data: () => ({
      userId: '',
      user: '',
      check1: false,
      check2: false,
    }),
    methods: {
      async getUser() {
        try {
          const res = await axios.get(
            `http://127.0.0.1:8000/users/${this.userId}`
          )
          this.user = res.data;
        } catch (error) {
          console.log(error)
        }
        
        if(this.user != null) {
          console.log('1111');
          this.check2 = true;
          window.location.href = '/';
        } else {
          this.check1 = true;
        }
        }
      },
      mounted() {
        if (localStorage.user) {
        this.user = JSON.parse(localStorage.user);
    }
  },
    watch: {
      user(newName) {
        localStorage.user = JSON.stringify(newName);
      }
  }
    }
  
</script>

<style>

</style>