$(document).ready(function() {
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
					reviewers[i].parent().parent().addClass('hide');
					/*
					reviewers[i].find('span').removeClass('hide');
					reviewers[i].addClass('highlight-disable');
					*/
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
	$(".finish-edit-btn").click(function(){
		location.href="admin_finish_edit.html";
	});	
	$(".submit-no-btn").click(function(){
		location.href="admin_home.html";
	});		
	
	$(".confirm-yes-btn").click(function(){
		location.href="admin_submit_success.html";
	});	
	$(".home").click(function(){
		location.href="admin_home.html";
	});		
	$(".click").click(function(){
		location.href="admin_home.html";
	});	
	$(".submit-success-btn").click(function(){
		location.href="admin_home.html";
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
