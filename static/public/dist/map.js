'use strict';

var myMap = L.map('my-map').setView([-0.1828190562356577, -78.48433256149292], 16);
var latitude = 0;
var longitude = 0;
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

myMap.locate({ setView: true, maxZoom: 16 });

function onMapClick(e) {
  L.marker([e.latlng.lat, e.latlng.lng]).addTo(myMap);
  latitude = e.latlng.lat;
  longitude = e.latlng.lng;
  console.log(e.latlng);
}
myMap.on('click', onMapClick);