var yMap, yPlacemark;

ymaps.ready(init);

async function init() {
    var place_input = document.getElementById('id_place')

    if (place_input.value) {
        var data = await ymaps.geocode(place_input.value)
        var firstGeoObject = data.geoObjects.get(0);
        var coords = firstGeoObject.geometry.getCoordinates();
    }
    else {
        var coords = [55.76, 37.64]
    }

    yMap = new ymaps.Map("map", {
        center: coords,
        zoom: 10,
    });

    yPlacemark = new ymaps.Placemark(coords, {}, { draggable: true });
    yMap.geoObjects.add(yPlacemark);

    yPlacemark.properties.set({
        balloonContent: 'Место на карте'
    });

    yPlacemark.events.add('dragend', async (e) => {
        var coords = yPlacemark.geometry.getCoordinates();
        var data = await ymaps.geocode(coords);
        var firstGeoObject = data.geoObjects.get(0);
        var address = firstGeoObject.getAddressLine();
        document.getElementById('id_place').value = address;
    });

    document.getElementById('id_place').addEventListener('change', async () => {
        var address = document.getElementById('id_place').value;
        var data = await ymaps.geocode(address);
        var firstGeoObject = data.geoObjects.get(0);
        var coords = firstGeoObject.geometry.getCoordinates();
        yMap.setCenter(coords, 16);
        yPlacemark.geometry.setCoordinates(coords);
    });

    var suggestView = new ymaps.SuggestView('id_place');

    suggestView.events.add('suggestselect', async (e) => {
        var address = e.get('item').value;
        document.getElementById('id_place').value = address;
        var data = await ymaps.geocode(address);
        var firstGeoObject = data.geoObjects.get(0);
        var coords = firstGeoObject.geometry.getCoordinates();
        yMap.setCenter(coords, 16);
        yPlacemark.geometry.setCoordinates(coords);
    });
}
