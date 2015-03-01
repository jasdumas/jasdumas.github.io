//var invocation = new XMLHttpRequest();
//var dataUrl = 'https://gist.githubusercontent.com/jasdumas/30b4a2e7388be9f894ae/raw/a8afaf2e938b3f6cf1bf70e52736b919520d17d5/marker-points.csv';
   
//function callOtherDomain() {
  //if(invocation) {    
    //invocation.open('GET', dataUrl, true);
    //invocation.withCredentials = true;
    //invocation.onreadystatechange = handler;
    //invocation.send(); 
  //}
//}
//Access-Control-Allow-Origin: http://jasdumas.github.io/
//var dataUrl = 'https://github.com/jasdumas/jasdumas.github.io/blob/master/data/marker-points.csv';
//var dataUrl = 'data/marker-points.csv';
var geoJSON = {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [38.91318805974558, -77.03238901390978]
        },
        "properties": {
          "title": "Mapbox DC",
          "marker-symbol": "monument"
        }
      },
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [-122.414, 37.776]
        },
        "properties": {
          "title": "Mapbox SF",
          "marker-symbol": "harbor"
        }
      }
    ]};
var maxZoom = 15;
var fieldSeparator = ',';
//Access-Control-Allow-Origin: http://otile{s}.mqcdn.com/
var baseUrl = 'http://otile{s}.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.jpg';
var baseAttribution = 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>, <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/" target="_blank">CC-BY-SA</a>';
var subdomains = '1234';
var clusterOptions = {showCoverageOnHover: false, maxClusterRadius: 50};
var labelColumn = "Name";
var opacity = 1.0;
