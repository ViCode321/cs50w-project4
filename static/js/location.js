function getLocation() {
    var input = document.getElementById("locationInput");

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) {
                showPosition(position, input);
            },
            showError
        );
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position, input) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;

    // API de geocodificación de MapQuest
    var request = new XMLHttpRequest();
    request.open('GET', 'http://www.mapquestapi.com/geocoding/v1/reverse?key=WGo3hrhE6fUsEkDLxCLW3pVUyzfwj8iz&location=' + lat + ',' + lon, true);

    request.onload = function () {
        if (this.status >= 200 && this.status < 400) {
            // La solicitud fue exitosa
            var data = JSON.parse(this.response);
            var location = data.results[0].locations[0];
            var city = location.adminArea5;

            // Mostrar la ciudad en el elemento input
            input.value = city;
        } else {
            // Hubo un error con la solicitud
            console.log('Error: ' + this.status);
        }
    };

    request.onerror = function () {
        // Hubo un error de conexión
        console.log('Error de conexión');
    };

    request.send();
}


function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("Para conocer su ubicación recarge la página y presione el cuadro de texto de 'Ubicación'");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("La información de ubicación no está disponible.");
            break;
        case error.TIMEOUT:
            alert("Se agotó el tiempo de espera para obtener la ubicación del usuario.");
            break;
        case error.UNKNOWN_ERROR:
            alert("Ocurrió un error desconocido al obtener la ubicación del usuario.");
            break;
    }
}
