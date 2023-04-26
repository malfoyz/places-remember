var yMap, yPlacemark;

ymaps.ready(init);

function init() {
    yMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 10
    });

    var coords = [55.76, 37.64];
    yPlacemark = new ymaps.Placemark(coords, {}, { draggable: true });
    yMap.geoObjects.add(yPlacemark);

    yPlacemark.properties.set({
        balloonContent: 'Место на карте'
    });

    yPlacemark.events.add('dragend', function (e) {
        var coords = yPlacemark.geometry.getCoordinates();
        ymaps.geocode(coords).then(function (res) {
            var firstGeoObject = res.geoObjects.get(0);
            var address = firstGeoObject.getAddressLine();
            document.getElementById('address').value = address;
        });
    });

    document.getElementById('address').addEventListener('change', function () {
        var address = document.getElementById('address').value;
        ymaps.geocode(address).then(function (res) {
            var firstGeoObject = res.geoObjects.get(0);
            var coords = firstGeoObject.geometry.getCoordinates();
            yMap.setCenter(coords, 16);
            yPlacemark.geometry.setCoordinates(coords);
        });
    });

    var suggestView = new ymaps.SuggestView('address');

    suggestView.events.add('suggestselect', function (e) {
        var address = e.get('item').value;
        document.getElementById('address').value = address;
        ymaps.geocode(address).then(function (res) {
            var firstGeoObject = res.geoObjects.get(0);
            var coords = firstGeoObject.geometry.getCoordinates();
            yMap.setCenter(coords, 16);
            yPlacemark.geometry.setCoordinates(coords);
        });
    });
}
