$(document).ready(function() {
	// Show tooltips, if there are any
	$('[rel=tooltip]').tooltip()
	
	$('.more_nav_items').hide();
	$(".msg").addClass("hide");
	$(".checkbox").addClass("hide").prop('disabled', false);
	$(".glyphicon-ok").addClass("hide").prop('disabled', false);
	$(".add-btn").addClass("hide").prop('disabled', false);
	$(".finish-edit-btn").addClass("hide").prop('disabled', false);
	$(".edit-btn").removeClass("hide").prop('disabled', false);
	$(".submit-btn").removeClass("hide").prop('disabled', false);
	$("#add-icon").addClass("hide").prop('disabled', false);
	$(".add-reviewer").addClass("hide").prop('disabled', false);
	/*
    $("body").tooltip({ selector: '[data-tooltip=tooltip]' });
    $(".manuscript-detail span").popover({
        placement : 'top'
    });*/
	var cur_form;
	var cur_row;
	var cur_listedReviewers;
	var reviewers;
	$(".add-btn").click(function(){
		$(".msg").addClass("hide");
		console.log("click add-btn");
		$(this).prop('disabled', true);
		cur_form = $(this).closest("form");
		cur_row= cur_form.closest(".row");
		cur_row.find(".col-sm-5").removeClass("col-sm-5").addClass("col-sm-4");
		cur_row.find("#add-icon").removeClass("hide");
		reviewers = $("#reviewer-list caption").map(function() {
			return $(this);
			//return this.value;
		}).get();
		console.log(reviewers);
		for (var i=0;i < reviewers.length; i++) {
			for (var j=0;j < cur_listedReviewers.length; j++) {
				//console.log(reviewers[i].find('a').text());
				//console.log(cur_listedReviewers[j]);
				if (reviewers[i].find('a').text() === cur_listedReviewers[j]) {
					console.log("--------");
					/*reviewers[i].parent().parent().addClass('hide');*/
					
					reviewers[i].find('span').removeClass('hide');
					reviewers[i].addClass('highlight-disable');
					
					/*
					console.log(reviewers[i].find("input[type='checkbox']"));
					reviewers[i].find("input[type='checkbox']").prop('disabled',true);
					*/
					//.prop('checked',true);
				}
			}
		}
		$('#reviewer-list caption a').addClass('disabled');
	});
	$('#reviewer-list caption').click(function(){
		if (typeof(cur_form) !=='undefined' && cur_form.find(".add-btn").prop('disabled')) {
			var n = 0;
			console.log("click caption "+(++n));
			if (!$(this).hasClass('highlight-disable')) {
				console.log("toggle hight"+ $(this));
				$(this).toggleClass('highlight');
				$(this).find('span').toggleClass('hide');
			}
		}
	})

	$('#reviewer-list caption').hover( function() {
			if (typeof(cur_form) !=='undefined' && cur_form.find(".add-btn").prop('disabled')) {
				$( this ).addClass("highlight-hover");
			}
		}, function() {
			if (typeof(cur_form) !=='undefined' && cur_form.find(".add-btn").prop('disabled')) {
				$( this ).removeClass("highlight-hover");
			}
	})
	$(".edit-btn").click(function(){
		$(".msg").addClass("hide");
		var form = $(this).closest("form");
		form.find('table').addClass("highlight");
		form.find('caption').addClass("highlight");
		form.find(".edit-btn").addClass("hide");
		form.find(".submit-btn").addClass("hide");
		form.find('.checkbox').removeClass('hide');
		$('#manuscript-list .btn').prop('disabled', true);
		form.find(".add-btn").removeClass("hide").prop('disabled', false);
		form.find(".finish-edit-btn").removeClass("hide").prop('disabled', false);
		cur_listedReviewers = form.find("input:checkbox").map(function() {
			return $(this).parent().next().text();
			//return this.value;
		}).get();
		console.log(cur_listedReviewers);
	});

	$("#add-icon").click(function(){
		cur_form.find(".add-btn").prop('disabled', false);
		var checkedValues = $('#reviewer-list caption.highlight').map(function() {
			return $(this).find('a').text();
			//return this.value;
		}).get();
		console.log(checkedValues);
		if (checkedValues.length>0) {
			cur_form.find(".add-reviewer").removeClass("hide");
			var str = "";
			for (var i=0;i < checkedValues.length; i++) {
				str = str + '<span class="checkbox hide"><input type="checkbox" checked="checked "></span><a class="user" href="user_detail.html">' + checkedValues[i] + "</a>";
				str = str + " ";
				cur_listedReviewers.push(checkedValues[i]);
			}

			cur_form.find(".add-reviewer td:last").append(str);
		}
		console.log(cur_listedReviewers);

		cur_form.find(".checkbox").removeClass("hide");
		cur_row= cur_form.closest(".row");
		cur_row.find("#add-icon").addClass("hide");
		cur_row.find(".col-sm-4").removeClass("col-sm-4").addClass("col-sm-5");
		$('#reviewer-list .reviewer').removeClass('hide');
		$("#reviewer-list .checkbox").addClass("hide");

		$('#reviewer-list caption').removeClass('highlight').removeClass('highlight-disable');
		$('#reviewer-list caption span').addClass('hide');
		$('#reviewer-list caption a').removeClass('disabled');

	});
	$(".submit-btn").click(function(){
		$("#reviewer-list .checkbox").addClass("hide");
	});

	$(".submit-no-btn").click(function(){
		location.href="admin_browselist.html";
	});
	$(".confirm-yes-btn1").click(function(){
		
	})
	$(".confirm-yes-btn").click(function(){
		//location.href="admin_submit_success.html";
		var dom = $(this).parent().parent().parent().parent().find('.modal-body');
		console.log(dom);
		var str = '<p>Your decision for the following manuscript has been made.</p><div class="'+'manu"'+'><p>PCA versus LDA (ID:XXXXX)</p><p>Author: Martinez, A.</p><p>Reviewers: John Lee*, Emily White, Mary Green*, Jim Chen</p></div><p>We have successfully send emails to the author and reviewers about the decision.</p>';
		dom.html(str);;
		dom.prev().find('h4').html("Success");
		dom.next().hide();
	});
	$(".home").click(function(){
		location.href="admin_browselist.html";
	});
	$(".click").click(function(){
		location.href="admin_browselist.html";
	});
	$(".submit-success-btn").click(function(){
		location.href="admin_browselist.html";
	});
	$(".finish-edit-btn").click(function(){
		$(this).parent().parent().parent().parent().find('.msg').removeClass('hide');
		var form = $(this).closest("form");
		form.find('table').removeClass("highlight");
		form.find('caption').removeClass("highlight");
		
		form.find('.checkbox').addClass('hide');
		form.find(".add-btn").addClass("hide").prop('disabled', false);
		form.find(".finish-edit-btn").addClass("hide").prop('disabled', false);
		$("#manuscript-list .submit-btn").removeClass("hide").prop('disabled', false);
		$("#manuscript-list .edit-btn").removeClass("hide").prop('disabled', false);
		form.find(".add-reviewer").addClass("hide").prop('disabled', false);
		//location.href="admin_browselist.html";
		cur_row.find("#add-icon").addClass("hide");
		$('#reviewer-list .reviewer').removeClass('hide');
		$("#reviewer-list .checkbox").addClass("hide");

		$('#reviewer-list caption').removeClass('highlight').removeClass('highlight-disable');
		$('#reviewer-list caption span').addClass('hide');
		$('#reviewer-list caption a').removeClass('disabled');		
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
$('.more_nav').click(function() {
	$('.more_nav_items').slideToggle(200);
	$(this).toggleClass('expanded');
	if ($(this).hasClass('expanded')) {
		$(this).html('Less');
	} else {
		$(this).html('More');
	}
});

/* Handles adding and deleting form fields */

// Initialize a counter
var i = 1;

// Add an element by appending html
function add_next_element() {
	html = '<input class="filefield' + ++i + '" name="file" type="file" style="border: none;"/><a class="filefield' + i + '" href="javascript:delete_element(\'filefield' + i + '\')">Remove</a>';
	$('.all_file_inputs').append(html);
}

// Remove a specific element by id
function delete_element(id) {
	$('.'+id).remove()
}

// Removing a file in an ajax-y way
function remove_file(url, divid) {
	$.ajax({
		type: "POST",
		url: url,
		data: {
			csrfmiddlewaretoken:document.getElementsByName('csrfmiddlewaretoken')[0].value
		},
		success: function(data) {
			$('#'+divid).html('Removed')
		}
	});
}
