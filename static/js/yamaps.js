class YandexMap {
    map = null;
    PlacemarkArray = [];
    d = 7;

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
                // $(".content").html(json_resp[0][1]);
                $("#base_name").html('<b>Place name:</b> ' + json_resp[0][1]);
                $("#lant").html('<b>Place lant:</b> ' + json_resp[0][2]);
                $("#long").html('<b>Place long:</b> ' + json_resp[0][3]);
                $("#decription").html('<b>Place description:</b> ' + json_resp[0][4]);

                console.log('photos str:  ');
                console.log(json_resp[0][5]);
                var photo_names = json_resp[0][5].split('|');
                console.log('photo_names:  ');
                console.log(photo_names);
                var photosHTML = '<b>Place photos:</b> <br> ';
                photo_names.forEach(function(element) {
                    photosHTML = photosHTML + '<img src="/static/img/tmp_places_photo/' + element + '" />';
                });

                $("#photos").html(photosHTML);
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
