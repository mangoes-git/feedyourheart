<template>
  <v-app>
    <v-app-bar
      app
      color="#001F3F"
      dark
    >
      <img class="mr-3" :src="require('./assets/feedyourheart_logo_bright.png')" height="40"/>
      <v-toolbar-title id="title">Feed Your Heart</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn
        @click="showAbout = true"
        text
      >
        <span class="mr-2">About</span>
        <v-icon>mdi-information</v-icon>
      </v-btn>
    </v-app-bar>
    
    <v-main>
      <div class="text-center" id="about-container">
      <v-dialog
        id="about-dialog"
        v-model="showAbout"
      >
        <About
          v-on:close-dialog="showAbout = false"
        />
      </v-dialog>
      </div>
      <v-container fluid id="main-container">
        <v-row id="main-row">
        <Map/>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Map from './components/Map.vue';
import About from './components/About.vue';

export default {
  name: 'App',

  components: {
    Map,
    About,
  },

  data: function () {
    return {
      showAbout: true,
    }
  },

  created: function() {
    document.title = "Feed Your Heart Map"
  }
};
</script>

<style scoped>
  @font-face {
    font-family: "AsapSemibold";
    src: local("AsapSemibold"),
    url(./assets/fonts/Asap-SemiBold.ttf) format("truetype");
  }

  @font-face {
    font-family: "AsapCondensed";
    src: local("AsapCondensed"),
    url(./assets/fonts/AsapCondensed-Regular.ttf) format("truetype");
  }

  #title {
    font-family: "AsapSemibold";
  }

  #about-container {
    width: 600px;
    max-width: 80vw;
  }

  #about-dialog {
    width: 600;
    /* max-width: 80vw; */
  }

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