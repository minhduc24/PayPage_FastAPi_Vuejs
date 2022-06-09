<template>
    
    <v-row no-gutters class="body">
      <v-col md="8">

      <side-bar />

      </v-col>
      <v-col md="4">

        <side-bar-right />

      </v-col>
    </v-row>

</template>

<script>
import SideBar from '../components/HomePage/SideBar.vue'
import SideBarRight from '../components/HomePage/SideBarRight.vue'





export default {
  components: {SideBar, SideBarRight},
  name: 'Home-vue',

}
</script>

<style>


.body {
  height: 89.4vh;
  background-color: violet;
}
</style>