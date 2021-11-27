<template>
  <v-app>
    <v-app-bar
      app
      color="pink"
      dark
    >
      <v-toolbar-title>Feed Your Heart</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container fluid id="main-container">
        <v-row id="main-row">
        <Map/>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Map from './components/Map.vue'

export default {
  name: 'App',

  components: {
    Map
  },

  data: () => ({
    //
  }),
};
</script>

<style scoped>
  #main-container {
    width: 100%;
    height: 100%;
    margin: 0;
    padding:0
  }
  #main-row {
    /* overflow: hidden; */
    width: 100%;
    height: 100%;
    margin:0;
    padding:0;
  }
</style>