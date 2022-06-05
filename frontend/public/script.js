window.console = {
    log: function(str){
        var node = document.createElement("div");
        node.appendChild(document.createTextNode(str));
        document.getElementById("items").appendChild(node);
    }
}

var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE) {
        console.log(xhr.responseText);
    }
}
xhr.open("GET", "http://localhost:8081/records/")
xhr.send(null);