jQuery(document).ready(function() {
    var redColor = "#FF0000";
    jQuery("#red_header").click(function() {
        jQuery("header").css("color", redColor);
    });
});
