<template>
  <v-card 
    id="about-card"
    color="#FFE8D5">
    <v-card-title>
      <h1 id="about-title">About</h1>
      <v-img
        :src="fyhLogo"
        contain
        max-height="150"
        >
      </v-img>
    </v-card-title>

    <v-card-text>
      <span class="text-subtitle-1 font-weight-bold">Map description</span>
      <br>
      <p>
        FeedYourHeart Map aims to provide a centralized resource of affordable and culturally diverse food spaces for newcomer students living in Toronto. This resource takes the form of an interactive map, where students can find information about pricing, proximity to public transportation, and culturally-specific food and ingredients. We want to provide newcomer students with a resource that increases access to affordable food they miss to get a little taste of home!
      </p>

      <span class="text-subtitle-1 font-weight-bold">Disclaimer</span>
      <p>
        This map is for informational purposes and may not have been prepared for or be suitable for legal purposes. Information and/or data are to be applied at your own risk and/or discretion; there is no guarantee of the accuracy of any information and/or data affiliated with this website. It does not represent an on-the-ground survey and represents only the approximate relative location of food spaces.
      </p>

      <span class="text-subtitle-1 font-weight-bold">Land acknowledgement</span>
      <p>
        The land we are standing on today is the traditional territory of many nations including the Mississaugas of the Credit, the Anishnabeg, the Chippewa, the Haudenosaunee and the Wendat peoples and is now home to many diverse First Nations, Inuit and Métis peoples.
      </p>

      <p>
        For indigenous peoples, lands and food are at the centre of what it is to be indigenous. In other instances, nomadic cultures required access to vast territories, which in turn ensured access to traditional foods. Tribal values of giving, sharing and trading are at the heart of land care and food sovereignty. As we know Toronto is built on stolen and sacred land and so every time we do or partake in a land acknowledgment we are all taking part in an act of reconciliation, remembrance and honouring the land and Indigenous Heritage which dates back over 10,000 years.
      </p>

      <span class="text-subtitle-1 font-weight-bold">Moderation</span>
      <p>
        FeedYourHeart is moderated by RISE ambassadors to prevent spam or inaccuracies. We welcome you to contribute to the map in any way you see fit. Provide your input <a href="https://forms.gle/izfVkuseimH1F8mS7" target="_blank">here</a>.
      </p>

      <p>
        All information will be verified before they become publicly available on the map.
      </p>

      <span class="text-subtitle-1 font-weight-bold">Contact Us</span>
      <p>
        <b>Email</b>: 
        <a href="mailto:aisbriseto@gmail.com">aisbriseto@gmail.com</a> <br>
        <b>Instagram</b>:
        <a href="https://www.instagram.com/aisbrise_to/">https://www.instagram.com/aisbrise_to/</a> <br>
        <b>Facebook</b>:
        <a href="https://www.facebook.com/aisbriseTO">https://www.facebook.com/aisbriseTO</a> <br>
        <b>Twitter</b>:
        <a href="https://twitter.com/aisbrise_to">https://twitter.com/aisbrise_to</a> <br>
        <b>Website</b>:
        <a href="https://www.apathyisboring.com/risetoronto">https://www.apathyisboring.com/risetoronto</a><br>
      </p>

      <div id="logos">
        <v-container>
          <v-row class="justify-center">
            <v-col
              v-for="(logo, i) in logos"
              :key="i"
              class="justify-center"
            >
              <v-img
                :src="logo"
                contain
                sm="3"
                md="3"
                lg="3"
                class="mx-auto"
                width="66%"
                max-height="150"
              >
              </v-img>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        color="#001F3F"
        text
        outlined
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
    return {
      fyhLogo: require('../assets/feedyourheart_logo_dark.png'),
      logos: [
        require('../assets/aisb_logo.png'),
        require('../assets/rise_logo.png'),
        require('../assets/canada_service_corps_logo.webp'),
        require('../assets/rbc_logo.png'),
        // require('../assets/feedyourheart_logo_dark.png'),
      ]
    };
  },

  methods: {
    closeAbout: function() {
      this.$emit('close-dialog');
    }
  }
}
</script>

<style>
  #about-title {
    font-family: "AsapCondensed";
  }
  #about-card {
    font-family: "AsapCondensed";
    padding-top: 5%; 
    width: 600px;
  }
</style>