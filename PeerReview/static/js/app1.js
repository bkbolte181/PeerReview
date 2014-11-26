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
	var reviewers;
	$(".add-btn").click(function(){
		$(".msg").addClass("hide");
		$(this).prop('disabled', true);
		cur_form = $(this).closest("form");
		cur_row= cur_form.closest(".row");
		cur_row.find(".col-sm-5").removeClass("col-sm-5").addClass("col-sm-4");
		cur_row.find("#add-icon").removeClass("hide");
		reviewers = $("#reviewer-list caption a span").map(function() {
			return $(this);
		}).get();

		cur_listedReviewers = cur_form.find("input:checkbox").map(function() {
			return $(this).parent().next().find(">:first-child").attr("value");
		}).get();
		cur_listedAuthors = cur_form.find("a.admin_author").map(function() {
			return $(this).find(">:first-child").attr("value");
		}).get();
		cur_listedReviewers = cur_listedReviewers.concat(cur_listedAuthors);
		console.log("cur_listedReviewers:");
		console.log(cur_listedReviewers);
		for (var i=0;i < reviewers.length; i++) {
			for (var j=0;j < cur_listedReviewers.length; j++) {
				if (reviewers[i].attr('value') === cur_listedReviewers[j]) {
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
			if (!$(this).hasClass('highlight-disable')) {
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
	});

	$("#add-icon").click(function(){
		cur_form.find(".add-btn").prop('disabled', false);
		var checkedValues = $('#reviewer-list caption.highlight').map(function() {
			return $(this);
		}).get();
		if (checkedValues.length>0) {
			cur_form.find(".add-reviewer").removeClass("hide");
			var str = "";
			for (var i=0;i < checkedValues.length; i++) {
				emailId = checkedValues[i].find("span.glyphicon-ok").attr('value').split(";");
				email = emailId[0];
				id = emailId[1];
				href = checkedValues[i].find("a");
				str = str + '<span class="checkbox hide"><input type="checkbox" value = "' + email +
					'" name = "reviewers_add" checked="checked "></span><a class="user" href="'+ href.attr('href')+'">' +
					href.text() + "</a>";
				str = str + " ";
				cur_listedReviewers.push(email);
			}
			cur_form.find(".add-reviewer td:last").append(str);
		}

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
		var manuscript_id = $(this).val();
		//ajax part
		$.ajax({
			url : "admin_submit_ajax/", 
			type : "POST",
			dataType: "json", 
			data : {
				manuscript_id: manuscript_id,
				csrfmiddlewaretoken: '{{ csrf_token }}',
			},
			success : function(data) {
				for (var reviewer in data.reviewers) {
					as_reviewer = data.reviewers[reviewer];
				}
				console.log(data.constraint);
			}
		});

		$("#reviewer-list .checkbox").addClass("hide");
	});

	$(".confirm-yes-btn").click(function(){
		var manuscript_id = $(this).val();
		var dom = $(this).parent().parent().parent().parent().find('.modal-body');
		//ajax part
		$.ajax({
			url : "admin_confirm_ajax/", 
			type : "POST",
			dataType: "json", 
			data : {
				manuscript_id: manuscript_id,
				csrfmiddlewaretoken: '{{ csrf_token }}',
			},
			success : function(data) {
				if (data.success == 'true') {
					var str = '<p>Your decision for the following manuscript has been made.</p><div class="'+'manu"';
					str += '><p>' +data.manuscript.id + '. '+ data.manuscript.title + ' (ID:' + data.manuscript.id +
						')</p><p>Author: ' + data.manuscript.author + '</p><p>Reviewers: ';
					strstr = "";
					for (var reviewer in data.reviewers)
						strstr += data.reviewers[reviewer].name + ', ';
					if (strstr.length == 0) {
						strstr = "<span style='color:red'>No reviewers for this manuscript.</span>";
					} else {
						strstr = strstr.substring(0, str.length-2);
						str = str.substring(0, str.length-2);
					}
					str = str + strstr;
					str += '</p></div><p>We have successfully send emails to the author and reviewers about the decision.</p>';
					dom.html(str);
					dom.prev().find('h4').html("Success");
					str = '<div class='+'"btn-group pull-right"'+'><button onclick="location.href='+'\'/admin_browselist/\'"'
					+' type="'+'button"'+ ' class="'+'btn btn-default confirm-no-btn"'+'>OK</button></div>';
					//console.log(str);
					dom.next().html(str);
				}
			}
		});
	});


	$(".finish-edit-btn").click(function(){
		my_form = $(this).closest("form");
		var manuscript_id = $(this).val();
		var check_list = document.getElementsByName('reviewers' + manuscript_id);
		var reviewers = '';
		for(var i=0; i<check_list.length; i++){
			if(check_list[i].checked) 
				reviewers += check_list[i].value + ',';
		}  
		//added reviewers
		var add_list = document.getElementsByName('reviewers_add');
		for(var i=0; i<add_list.length; i++){
			if(add_list[i].checked) 
				reviewers += add_list[i].value + ',';
		}  

		//ajax part
		$.ajax({
			url : "admin_ajax/", 
			type : "POST",
			dataType: "json", 
			data : {
				reviewers: reviewers,
				manuscript_id: manuscript_id,
				csrfmiddlewaretoken: '{{ csrf_token }}',
			},
			success : function(data) {
				var str = "";
				assigned_reviewer_td = my_form.find("tr.assigned-reviewer").children('td').eq(1);
				href_prefix_str = "/user_detail/";
				assigned_reviewer_td.empty();
				console.log("from server: assigned_reviewers: ")

				for (var assigned_reviewer in data.assigned) {
					as_reviewer = data.assigned[assigned_reviewer];
					console.log(as_reviewer.name);
					email = as_reviewer.email;
					id = as_reviewer.id;
					href = href_prefix_str + id + "/";
					name = as_reviewer.name;
					str = str + '<span class="checkbox hide"><input type="checkbox" value = "' + email + '" name = "reviewers'+manuscript_id+'" checked="checked "></span><a class="user" href="'+ href+'"><span value="'+id+'"></span>' + name + "</a>";
					str = str + ", ";
				}
				if (str.length == 0) {
					str = "<span style='color:red'>No assigned reviewers for this manuscript.</span>"
				} else {
					str = str.substring(0, str.length-2);
				}
				assigned_reviewer_td.append(str);


				str = "";
				recommended_reviewer_td = my_form.find("tr.recommend-reviewer").children('td').eq(1);
				recommended_reviewer_td.empty();

				for (var recommended_reviewer in data.recommend) {
					re_reviewer = data.recommend[recommended_reviewer];
					email = re_reviewer.email;
					id = re_reviewer.id;
					href = href_prefix_str + id + "/";
					name = re_reviewer.name;
					str = str + '<span class="checkbox hide"><input type="checkbox" value = "' + email + '" name = "reviewers'+manuscript_id+'"></span><a class="user" href="'+ href+'"><span value="'+id+'"></span>' + name + "</a>";
					str = str + ", ";
				}
				if (str.length == 0) {
					str = "<span style='color:red'>No recommended reviewers for this manuscript.</span>";
				} else {
					str = str.substring(0, str.length-2);
				}
				recommended_reviewer_td.append(str);

				added_reviewer_td = my_form.find("tr.add-reviewer").children('td').eq(1);
				added_reviewer_td.empty();
				msg_span = my_form.find("tr.msg td").first().find("span");
				msg_span.empty();
				if (data.constraint.length > 0)
					msg_span.append("<br/> Warning! The matching constrains are not satisfied because: " + data.constraint);
				str = '#modal-body'+manuscript_id + " .manu p span";
				str_warning = '#modal-body'+manuscript_id + " p.warning";
				modal_warning = $(str_warning);
				modal_reviewer = $(str);
				modal_reviewer.empty();
				str = "";
				console.log(modal_warning);
				modal_warning.empty();
				if (data.constraint.length > 0)
					modal_warning.append("Warning! The matching constrains are not satisfied because: " + data.constraint);
				for (var reviewer in data.assigned)
					str += data.assigned[reviewer].name + ', ';
				//str = str.substring(0, str.length-2);
				if (str.length == 0) {
					str = "<span style='color:red'>No assigned reviewers for this manuscript.</span>";
				} else {
					str = str.substring(0, str.length-2);
				}
				//recommended_reviewer_td.append(str);
				modal_reviewer.append(str);
			}
		});
		
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
		cur_row= form.closest(".row");
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
