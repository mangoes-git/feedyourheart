<template>
  <l-map style="height: 100%" :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>

    <l-marker
      v-for="place in allPlaces"
      :key="place.Name"
      :lat-lng="[place.Latitudes, place.Longitudes]">
        <l-popup>
          <div v-html="generatePopupText(place)">
          </div>
        </l-popup>
    </l-marker>

    <l-marker
      v-for="station in stations"
      :key="station['Station Name']"
      :lat-lng="[station.Latitudes, station.Longitudes]"
      :icon="ttcIcon"
      >

        <l-popup>
          <div>
            <b>{{station['Station Name']}} Station</b>
          </div>
        </l-popup>
    </l-marker>
  </l-map>
</template>

<script>
  import L from "leaflet";
  import {LMap, LTileLayer, LMarker, LPopup,} from 'vue2-leaflet';

  export default {
    name: 'Map',

    components: {
      LMap,
      LTileLayer,
      LMarker,
      LPopup,
      // LIcon,
    },

    data: function() {
      return {
        places: [],

        center: [43.7, -79.39],
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        zoom: 12,

        ttcIcon: L.icon({
          iconUrl: require('/src/assets/ttc.svg'),
          iconSize: [38, 95], // size of the icon
        }),
      }
    },

    methods: {
      generatePopupText: function(data) {
        let result = '';
        for (const [key, value] of Object.entries(data)) {
          if (key !== 'Longitudes' || key !== 'Latitudes') {
            result += `<b>${key}:</b> ${value}<br>`
          }
        }
        return result;
      }
    },

    computed: {
      allPlaces: function() {
        return [
          ...this.places.campus_eateries,
          ...this.places.food_pantry,
          ...this.places.food_initiatives,
          ...this.places.grocery_stores
          ];
      },

      stations: function() {
        return this.places.ttc;
      }
    },

    beforeMount: function () {
      // this.setupLeafletMap();
      delete L.Icon.Default.prototype._getIconUrl;

      L.Icon.Default.mergeOptions({
        iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
        iconUrl: require('leaflet/dist/images/marker-icon.png'),
        shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
      });

      this.places = require('../../data/data.json');
      console.log(this.places)
    }
  }
</script>

<style>
#map-container {
 width: 100%;
 height: 100%;
 overflow: hidden;
}
</style>