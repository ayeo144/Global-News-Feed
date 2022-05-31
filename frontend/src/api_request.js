fetch('http://host.docker.internal:8000/records/')
    .then(function (response) {
        return response.json()
    })
    .then(function (data) {
        appendData(data);
    })
    .catch(function (err) {
        console.log(err);
    });

function appendData(data) {
    console.log(data.data.length);
}