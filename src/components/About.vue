<template>
  <v-card 
    id="about-card"
    color="#FFE8D5">
    <v-card-title>
      <span class="text-h5">About</span>
    </v-card-title>

    <v-card-text>
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        color="#001F3F"
        text
        @click="closeAbout"
        >
        Close
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'About',

  data: function() {
    return {};
  },

  methods: {
    closeAbout: function() {
      this.$emit('close-dialog');
    }
  }
}
</script>

<style>
  #about-card {
    width: 600px;
  }
</style>