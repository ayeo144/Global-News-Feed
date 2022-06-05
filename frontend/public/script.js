// Set up console logging to a specific HTML element
window.console = {
    log: function(str){
        var node = document.createElement("div");
        node.appendChild(document.createTextNode(str));
        document.getElementById("items").appendChild(node);
    }
}

// Create the template map and add to HTML element "map"
var coords = [51.505, -0.09]
var zoomLevel = 13
var map = L.map('map').setView(coords, zoomLevel);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

// Make the GET request to the backend REST API
var xhr = new XMLHttpRequest();

// Display the results of the request
xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE) {

        const res = JSON.parse(xhr.responseText);
        const data = res["data"];

        // console.log(JSON.stringify(data[0], null, 4));

        console.log(data[0]["Title"]);

        // for (const item in data){
        //     console.log(item)
        // }
    }
};

xhr.open("GET", "http://localhost:8081/records/")
xhr.setRequestHeader('Accept', 'application/json');
xhr.send(null);