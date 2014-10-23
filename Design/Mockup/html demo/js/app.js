$(document).ready(function() {
    $("body").tooltip({ selector: '[data-toggle=tooltip]' });
    $(".manuscript-detail span").popover({
        placement : 'top'
    });
});
$( document.body ).on( 'click', '.dropdown-menu li', function( event ) {
  var $target = $( event.currentTarget );
  $target.closest( '.btn-group' )
     .find( '[data-bind="label"]' ).text( $target.text() )
        .end()
     .children( '.dropdown-toggle' ).dropdown( 'toggle' );
  return false;
});

/* assigned by class */
$(function () { $("input,select,textarea").not("[type=submit]").jqBootstrapValidation(); } );

/* assigned by element */
$(function(){$(".validated").jqBootstrapValidation();});