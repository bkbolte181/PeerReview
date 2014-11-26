$(document).ready(function() {
	$(".msg").addClass("hide");
	$(".checkbox").addClass("hide").prop('disabled', false);
	$(".glyphicon-ok").addClass("hide").prop('disabled', false);
	$(".add-btn").addClass("hide").prop('disabled', false);
	$(".finish-edit-btn").addClass("hide").prop('disabled', false);
	$(".edit-btn").removeClass("hide").prop('disabled', false);
	$(".submit-btn").removeClass("hide").prop('disabled', false);
	$("#add-icon").addClass("hide").prop('disabled', false);
	$(".add-reviewer").addClass("hide").prop('disabled', false);

	var cur_form;
	var cur_row;
	var cur_listedReviewers;
	var reviewers;
	$(".add-btn").click(function(){
		$(".msg").addClass("hide");
		//console.log("click add-btn");
		$(this).prop('disabled', true);
		cur_form = $(this).closest("form");
		cur_row= cur_form.closest(".row");
		cur_row.find(".col-sm-5").removeClass("col-sm-5").addClass("col-sm-4");
		cur_row.find("#add-icon").removeClass("hide");
		reviewers = $("#reviewer-list caption a span").map(function() {
			return $(this);
		}).get();
		//console.log("reviewers in reviewer list:");
		//console.log(reviewers);
		for (var i=0;i < reviewers.length; i++) {
			for (var j=0;j < cur_listedReviewers.length; j++) {
				if (reviewers[i].attr('value') === cur_listedReviewers[j]) {//if (reviewers[i].find('a').text() === cur_listedReviewers[j]) {
					//console.log("--------");
					//console.log(reviewers[i].attr('value'));
					
					reviewers[i].parent().parent().find('span.glyphicon-ok').removeClass('hide');
					reviewers[i].parent().parent().addClass('highlight-disable');
				}
			}
		}
		$('#reviewer-list caption a').addClass('disabled');
	});
	$('#reviewer-list caption').click(function(){
		if (typeof(cur_form) !=='undefined' && cur_form.find(".add-btn").prop('disabled')) {
			var n = 0;
			//console.log("click caption "+(++n));
			if (!$(this).hasClass('highlight-disable')) {
				//console.log("toggle hight"+ $(this));
				$(this).toggleClass('highlight');
				$(this).find('span.glyphicon-ok').toggleClass('hide');
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
			return $(this).parent().next().find(">:first-child").attr("value");
			//return this.value;
		}).get();
		cur_listedAuthors = form.find("a.admin_author").map(function() {
			return $(this).find(">:first-child").attr("value");
		}).get();
		cur_listedReviewers = cur_listedReviewers.concat(cur_listedAuthors);
		//cur_listedReviewers.push("134@emory.edu");
		//console.log("cur_listedReviewers:");
		//console.log(cur_listedReviewers);
		//console.log("cur_listedAuthors:");
		//console.log(cur_listedAuthors);
	});

	$("#add-icon").click(function(){
		cur_form.find(".add-btn").prop('disabled', false);
		var checkedValues = $('#reviewer-list caption.highlight').map(function() {
			return $(this);
		}).get();
		//console.log("checkValues:");
		//console.log(checkedValues);
		if (checkedValues.length>0) {
			cur_form.find(".add-reviewer").removeClass("hide");
			var str = "";
			for (var i=0;i < checkedValues.length; i++) {
				emailId = checkedValues[i].find("span.glyphicon-ok").attr('value').split(";");
				email = emailId[0];
				id = emailId[1];
				href = checkedValues[i].find("a");
				//console.log("email: " + email+"; id: "+ id);
				str = str + '<span class="checkbox hide"><input type="checkbox" value = "' + email + '" name = "reviewers" checked="checked "></span><a class="user" href="'+ href.attr('href')+'">' + href.text() + "</a>";
				str = str + " ";
				cur_listedReviewers.push(checkedValues[i]);

			}
			//console.log(str);
			cur_form.find(".add-reviewer td:last").append(str);
		}
		//console.log(cur_listedReviewers);

		cur_form.find(".checkbox").removeClass("hide");
		cur_row= cur_form.closest(".row");
		cur_row.find("#add-icon").addClass("hide");
		cur_row.find(".col-sm-4").removeClass("col-sm-4").addClass("col-sm-5");
		$('#reviewer-list .reviewer').removeClass('hide');
		$("#reviewer-list .checkbox").addClass("hide");

		$('#reviewer-list caption').removeClass('highlight').removeClass('highlight-disable');
		$('#reviewer-list caption span.glyphicon-ok').addClass('hide');
		$('#reviewer-list caption a').removeClass('disabled');

	});
	$(".submit-btn").click(function(){
		$("#reviewer-list .checkbox").addClass("hide");
	});
	/*
	$(".submit-no-btn").click(function(){
		location.href="admin_browselist1.html";
	});
	$(".confirm-yes-btn1").click(function(){
		
	})*/
	$(".confirm-yes-btn").click(function(){
		//location.href="admin_submit_success.html";
		var dom = $(this).parent().parent().parent().parent().find('.modal-body');
		//console.log(dom);
		var str = '<p>Your decision for the following manuscript has been made.</p><div class="'+'manu"'+'><p>PCA versus LDA (ID:XXXXX)</p><p>Author: Martinez, A.</p><p>Reviewers: John Lee*, Emily White, Mary Green*, Jim Chen</p></div><p>We have successfully send emails to the author and reviewers about the decision.</p>';
		dom.html(str);;
		dom.prev().find('h4').html("Success");
		//console.log('Hello');
		//console.log(dom.next());
		dom.next().html('<div class="'+'btn-group pull-right"'+'><button type="'+'button"'+ 'class="'+'btn btn-default confirm-no-btn"'+  'data-dismiss="'+'modal"'+'>OK</button></div>');		
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
		$('#reviewer-list caption span.glyphicon-ok').addClass('hide');
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
