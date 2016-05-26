let myMap = L.map('my-map').setView([-0.1828190562356577, -78.48433256149292], 16)
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap)

let selectedLocation = undefined

myMap.locate({setView: true, maxZoom: 16})
let myMarker = L.marker([-0.1828190562356577, -78.48433256149292])
myMarker.addTo(myMap)

function onMapClick(e) {
  myMarker.setLatLng(e.latlng)
  myMarker.update()
  console.log(e.latlng)
  selectedLocation = e.latlng
}
myMap.on('click', onMapClick)
