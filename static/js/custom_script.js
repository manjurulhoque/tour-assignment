// django.jQuery(document).ready(function () {
//     console.log("ready!");
//     django.jQuery('#id_locations').change(function () {
//         alert("Handler for #id_category was called.");
//     });
// });

window.addEventListener("load", function () {
    (function ($) {
        django.jQuery('#id_locations').change(function () {
            $.ajax({
                type: "POST",
                url: "/get-minimum-and-type/",
                data: {
                    'location_ids': $("#id_locations").select2("val") // from form
                },
                success: function (res) {
                    $('#id_type').val(res.tour_type);
                    $('#id_minimum_duration').val(res.total_minutes);
                }
            })
        });
    })(django.jQuery);
});