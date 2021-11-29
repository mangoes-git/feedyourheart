<template>
  <l-map id="l-map" :zoom="zoom" :center="center">
    <l-control-layers ref="controls"></l-control-layers>
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>

    <l-layer-group 
      v-for="category in categories"
      :key="category.key"
      ref="layers"
      layerType="overlay"
      :name="category.name"
      :visible="true">
        <l-marker
          v-for="place in places[category.key]"
          :key="place.Name"
          :lat-lng="[place.Latitudes, place.Longitudes]"
          :icon="getIcon(category)">
            <l-popup>
              <div v-html="generatePopupText(category, place)">
              </div>
            </l-popup>
        </l-marker>
    </l-layer-group>
  </l-map>
</template>

<script>
  import L from "leaflet";
  import {LMap, LTileLayer, LMarker, LPopup, LLayerGroup, LControlLayers} from 'vue2-leaflet';

  export default {
    name: 'Map',

    components: {
      LMap,
      LTileLayer,
      LMarker,
      LPopup,
      LLayerGroup,
      LControlLayers,
      // LIcon,
    },

    data: function() {
      return {
        places: [],

        center: [43.7, -79.39],
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        zoom: 12,

        ttcIcon: L.icon({
          iconUrl: require('/src/assets/ttc.svg'),
          iconSize: [40, 20], // size of the icon
        }),
      }
    },

    methods: {
      generateTtcText: function(data) {
        let result = `<b>TTC Station</b><br><b>Station Name:</b> ${data['Station Name']}`
        return result
      },
      generatePopupText: function(category, data) {
        let result = '';
        if (category.key === 'ttc') {
          result = this.generateTtcText(data);
        } else {
          result += `<b>${category.name}</b><br>`;
          result += `<b>Name:</b> ${data.Name}<br>`;
          result += `<b>Address:</b> ${data.Address}<br>`;
          result += data['Opening hours'] ? `<b>Opening Hours:</b> ${data['Opening hours']}<br>` : '';
          result += data['Phone Number'] ? `<b>Phone Number:</b> ${data['Phone Number']}<br>` : '<b>Phone Number:</b> Not available<br>';
          result += data['Ethnicity'] ? `<b>Ethnicity:</b> ${data['Etnicity']}<br>` : '';
          result += data['Region'] ? `<b>Region:</b> ${data['Region']}<br>` : '';
          result += data['Closest TTC Stops'] ? `<b>Closest TTC Stops:</b> ${data['Closest TTC Stops']}<br>` : '';
          result += data['Website'] ? `<b>Website:</b> <a href="https://${data['Website']}" target="_blank" rel="noopener noreferrer">${data['Website']}</a><br>` : '<b>Website:</b> Not available<br>';
          result += data['Eligibility'] ? `<b>Eligibility:</b> ${data['Eligibility']}<br>` : '';
          result += data['Community Initiatives'] ? `<b>Community Initiatives:</b> ${data['Community Initiatives']}<br>` : '';
        }
        return result;
      },

      getIcon: function(category) {
        if (category.key === 'ttc') {
          return this.ttcIcon;
        } else {
          return null;
        }
      }
    },

    computed: {
      categories: function() {
        return [
          {
            name: 'Campus Eateries',
            key: 'campus_eateries'
          },
          {
            name: 'Food Pantry',
            key: 'food_pantry',
          },
          {
            name: 'Food Initiatives',
            key: 'food_initiatives'
          },
          {
            name: 'Grocery Stores',
            key: 'grocery_stores'
          },
          {
            name: 'TTC Stations',
            key: 'ttc'
          }
        ]
      },
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

  #l-map {
    z-index: 0;
    position: relative;
  }
</style>