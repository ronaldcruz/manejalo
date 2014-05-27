$(function() {
    $("select").selecter({
        defaultLabel: "Seleccione"
    });    

    
    var tour = new Tour({
        steps: [
            {
                element: "#step1",
                title: "Detalles del vehículo",
                content: "Ingresa la información acerca de tú vehículo para tener mejores resultados en las búsquedas que realicen."
            },
            {
                element: "#step2",
                title: "Características",
                content: "Mientras más características específiques, tendrás más posibilidades de que tu vehículo aparesca al realizar un filtro."
            },
            {
                element: "#step3",
                title: "Fotos",
                content: "Los avisos que contengan fotos del vehículo son mucho más confiables. No te olvides de añadir el interior y exterior de tú vehículo."
            },
            {
                element: "#step4",
                title: "Contacto",
                content: "No olvides ingresar tus datos de contacto y tús preferencias para una posible visita."
            },
            {
                element: "#submitAdvertisement",
                title: "Publicar Aviso",
                placement: "left",
                content: "Finalmente, sube tu aviso. Este estará disponible por 30 días."
            }
        ],
        template: function(i, step) {
            return $('<div class="popover tour popover-submit">').append($('#tour-popover').html());
        },
        onEnd: function (tour) {
            var body = $("html, body");
            body.animate({scrollTop:0}, '500', 'swing');
            $('#step1 > a').tab('show');
        },
        onNext: function (tour) {
            var step = tour.getCurrentStep();
            if (step == 0) {
                $('#step2 > a').tab('show');
            }
            if (step == 1) {
                $('#step3 > a').tab('show');
            }
            if (step == 2) {
                $('#step4 > a').tab('show');
            }
            if (step > 2) {
                $('#step1 > a').tab('show');
            }
        },
        onPrev: function (tour) {
            var step = tour.getCurrentStep();
            if (step == 4) {
                $('#step4 > a').tab('show');
            }
            if (step == 3) {
                $('#step3 > a').tab('show');
            }
            if (step == 2) {
                $('#step2 > a').tab('show');
            }
            if (step == 1) {
                $('#step1 > a').tab('show');
            }
        },
    });

    // Initialize the tour
    tour.init();

    // Start the tour
    tour.start();
    

    $(":file").filestyle({
        input: false,
        buttonName: "btn-default",
        size: 'lg',
        iconName: "glyphicon-upload",
        buttonText: 'Examinar'
    });

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                $(input).closest('.item-photo').find('a > img').attr('src', e.target.result);
            }

           reader.readAsDataURL(input.files[0]);
        }
    }

    $('#section_photos .item-photo').find(':file').change(function() {
        readURL(this);
    });

});    