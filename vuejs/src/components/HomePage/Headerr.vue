<template>
  <v-app-bar
    color="blue"
    density="compact"
    height="120"
  >
        
    <v-row no-gutters>
      <v-col
        md="9"
        class="d-flex"
      >
        <v-app-bar-title class="mt-4">THANH TOÁN</v-app-bar-title>
        <v-text-field
          label="Nhập mã sản phẩm"
          variant="contained"
          hide-details
          class="search"
          v-model="productId"
          
        >
        </v-text-field>
        <v-btn icon="fas fa-search" class="mt-1" @click="addProduct"></v-btn>
        </v-col>
                  
        <v-col md="3">
          <v-row 
          justify="end"
          class="mt-1"
          >
        <v-menu  v-if="check != false">
        <template v-slot:activator="{ props }">
          <v-btn
            icon
            v-bind="props"
          >
          <v-avatar
            size="large"
          >
          <v-img :src="check.user_img"></v-img>
          </v-avatar>
          </v-btn>
        </template >
        <v-card class="test">
          <v-card-text>
            <div class="mx-auto text-center">
              <v-avatar
                size="large"
              >
              <v-img :src='check.user_img'></v-img>
              </v-avatar>
              <h3>{{ check.user_name }}</h3>
              <p class="text-caption mt-1">
                {{ check.accumulate_points }}
              </p>
              <v-divider class="my-3"></v-divider>
              <v-btn
                rounded
                variant="text"
              > 
                <router-link to="/" @click="resetUser">
                Logout
                </router-link>
              </v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-menu>
      <v-menu v-if="check == false">
        <template v-slot:activator="{ props }">
          <v-btn
            icon
            v-bind="props"
          >
          <v-avatar
            size="large"
          >
          <v-img :src="user.img"></v-img>
          </v-avatar>
          </v-btn>
        </template >
        <v-card class="test">
          <v-card-text>
            <div class="mx-auto text-center">
              <v-avatar
                size="large"
              >
              <v-img :src='user.img'></v-img>
              </v-avatar>
              <h3>{{ user.name }}</h3>
              <p class="text-caption mt-1">
                {{ user.accumulate_points }}
              </p>
              <v-divider class="my-3"></v-divider>
              <v-btn
                rounded
                variant="text"
              > 
                <router-link to="/account">
                Login
                </router-link>
              </v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-menu>
    </v-row>
  </v-col>
      </v-row>
  </v-app-bar>


</template>

<script>
export default {
    name: 'headerr-vue',
    data: () => ({
      user: {
        id: '',
        img: 'https://hostpapasupport.com/knowledgebase/wp-content/uploads/2018/04/1-13.png',
        name: '',
        accumulate_points: '',
      },
      productId: '',
      check: localStorage.user ? JSON.parse(localStorage.user) : false,

    }),
    methods: {
      addProduct(event) {
        event.preventDefault();
        this.$emit('addProduct', this.productId);
        this.productId = '';
      },
      resetUser() {
        this.check = false;
        localStorage.clear();
      }
    },
    
}
</script>

<style scoped>
.search{
  max-width: 1000px;
}

.test {
  position: relative;
  top: 2px;
  right: 74px;
}


</style>