/*global navigator*/
/*global $*/


var x = document.getElementById("coords_info");
var latitude;
var longitude;

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
  console.log(position.coords.latitude)
  console.log(position.coords.longitude)
}

function showLocationOnMap() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showCurrentLocationOnMap);
    } else {
        x.innerHTML("Gelocation is not supported by this browser.")
    }
}

function showCurrentLocationOnMap(position) {
  var crd = position.coords;
  console.log("Here 1");
  var current_lat = crd.latitude;
  var current_lon = crd.longitude;
  var coords = current_lat + ', ' + current_lon;
  document.getElementById("google_map").setAttribute('src', 'https://maps.google.co.uk?q='+ coords +'&z=40&output=embed')
}

/*
function successCoords(position) {
  var crd = position.coords;
  latitude = crd.latitude;
  longitude = crd.longitude;
  console.log(latitude, longitude);
  $.ajax({
            url: "{% url 'remote_clock_page' %}",
            data: { 
                "latitude": latitude, 
                "longitude": longitude
            },
            type: "GET",
            cache: false,
            success: function(data, jqXHR){
                console.log(this.data + ", " + this.url);
            },  
            error: function(data){
                console.log("In this error");
            }   
        });
}
*/