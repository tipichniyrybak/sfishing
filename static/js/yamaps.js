class YandexMap {
    map = null;
    PlacemarkArray = [];

    constructor() {
        var that = this;
        ymaps.ready(function () {
            that.map = new ymaps.Map('map', {
                center: [59.939095, 30.315961],
                zoom: 10,
                controls: []
            });
        });
    }

    get_place_info(place_id) {
        $.ajax({
            type: "POST",
            url: "/get_place_info?place_id=" + place_id,

            type: 'POST',
            success: function(response) {
                var json_resp = jQuery.parseJSON(response)

                console.log('json_resp:');
                console.log(json_resp);
                $(".content").html(json_resp);

            },
            error: function(error) {
                console.log('error:');
                console.log(error);
            }
        });
    }

    set_places() {
        var that = this;
        $.ajax({
            type: "POST",
            url: "/get_places",

            type: 'POST',
            success: function(response) {
                var json_resp = jQuery.parseJSON(response)

                console.log('json_resp:');
                console.log(json_resp);
                ymaps.ready(function () {
                    json_resp.forEach(function(element) {
                        console.log(element[1]);
                        var myPlacemark1 = new ymaps.Placemark([element[2], element[3]], {
                            iconContent: element[1]
                        }, {
                            preset: 'islands#darkOrangeStretchyIcon'
                        });
                        myPlacemark1.events.add(['click'],  function (e) {
                            console.log('click cluck');
//                            document.getElementByID("divcontentID").innerHTML = element[1];

                            that.get_place_info(element[0]);

                        });
                        that.PlacemarkArray.push(myPlacemark1);
                        that.map.geoObjects.add(myPlacemark1);
                    });
                });
            },
            error: function(error) {
                console.log('error:');
                console.log(error);
            }
        });
    }
}
