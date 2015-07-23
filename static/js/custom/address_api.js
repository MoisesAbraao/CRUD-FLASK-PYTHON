var geocoder;
var map;
var marker;
 
function initialize() {
    var lat = $('#id_latitude').val();
    var lng = $('#id_longitude').val();
    var customZoom = 16;

    if(!lat || !lng) {
        lat = -5.8019527;
        lng = -35.2223209;
        customZoom = 10;
    }

    var latlng = new google.maps.LatLng(lat,lng);

    var options = {
        zoom: customZoom,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
 
    map = new google.maps.Map(document.getElementById("gmap"), options);
 
    geocoder = new google.maps.Geocoder();
 
    marker = new google.maps.Marker({
        map: map,
        draggable: true,
    });
 
    marker.setPosition(latlng);
}
 
function consultacep(cep){
    cep = cep.replace(/\D/g,"");
    url="http://cep.correiocontrol.com.br/"+cep+".js";
    s=document.createElement('script');
    s.setAttribute('charset','utf-8');
    s.src=url;
    document.querySelector('head').appendChild(s);
}

function correiocontrolcep(valor){
    if (valor.erro) {
        alert('Cep não encontrado');       
        return;
    }

    loadMap(valor.logradouro + ', ' + valor.bairro + ', ' + valor.localidade + ', ' + valor.uf);

    $('#id_logradouro').val(valor.logradouro);
    $('#id_bairro').val(valor.bairro);
    $('#id_cidade').val(valor.localidade);
    $('#id_uf').val(valor.uf);
    $('#id_numero').focus();

    habilitaCamposEndereco();
}

function loadMap(address) {
    geocoder.geocode({ 'address': address + ', Brasil', 'region': 'BR' }, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            if (results[0]) {
                var latitude = results[0].geometry.location.lat();
                var longitude = results[0].geometry.location.lng();

                //$('#txtEndereco').val(results[0].formatted_address);
                $('#id_latitude').val(latitude);
                $('#id_longitude').val(longitude);

                var location = new google.maps.LatLng(latitude, longitude);
                marker.setPosition(location);
                map.setCenter(location);
                map.setZoom(16);
            }
        }
    });
}
function habilitaCamposEndereco(habilita) {
    habilita = habilita || true;
    if(habilita) {
        $('#id_logradouro').removeAttr('readonly');
        $('#id_bairro').removeAttr('readonly');
        $('#id_cidade').removeAttr('readonly');
        $('#id_uf').removeAttr('readonly');
        $('#id_numero').removeAttr('readonly')
        $('#id_complemento').removeAttr('readonly');
    }
    else {
        $('#id_logradouro').attr('readonly');
        $('#id_bairro').attr('readonly');
        $('#id_cidade').attr('readonly');
        $('#id_uf').attr('readonly');
        $('#id_numero').attr('readonly')
        $('#id_complemento').attr('readonly');
    }
}
    
$(document).ready(function () {
    if($('#id_logradouro').val())
        habilitaCamposEndereco();

    initialize();

    google.maps.event.addListener(marker, 'drag', function () {
        geocoder.geocode({ 'latLng': marker.getPosition() }, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                    if (results[0]) { 
                    //$('#txtEndereco').val(results[0].formatted_address);
                    $('#id_latitude').val(marker.getPosition().lat());
                    $('#id_longitude').val(marker.getPosition().lng());
                }
            }
        });
    });

});