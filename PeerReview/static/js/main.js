$(document).ready(function() {
	$('.more_nav_items').hide();
});
$('.more_nav').click(function() {
	$('.more_nav_items').slideToggle(200);
	$(this).toggleClass('expanded');
	if ($(this).hasClass('expanded')) {
		$(this).html('Less');
	} else {
		$(this).html('More');
	}
});