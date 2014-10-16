$(document).ready(function() {
    $("body").tooltip({ selector: '[data-toggle=tooltip]' });
    $(".manuscript-detail span").popover({
        placement : 'top'
    });
});
