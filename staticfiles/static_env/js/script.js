function getCookie(name) {
        // Function to get any cookie available in the session.
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    function csrfSafeMethod(method) {
        // These HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');
    var page_title = $(document).attr("title");
    // This sets up every ajax call with proper headers.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


$(document).ready(function(){
	/*comment button toggle form on click */
	$('.like-comment-action-icon-div .comment-action-js').on('click',function(e){
		let context_form = $(this).parents('.parent-wrap').find('.hide-comment-form-wrap');
		context_form.toggle();
		
	});

	/*Search*/
	/*TODO*/
	$('.search-query').on('keyup',function(e){
		const search_url = $(this).attr('action');
		let val_ = $('.search-query').val().trim();
		len = val_.length;
		if (!(len > 1)){
			return false;
		}

		let request_data = {
			'query':val_,
		}

		$.ajax({
				url : search_url,
				data: request_data,
				type: 'GET',
				dataType:'json',
				cache: false,
				success : function(response){
					console.log(response.data);
					
				}
		});
		return false;	
	});

	/*comment*/
	$('.comment-form').on('submit',function(e){
		e.preventDefault();
		const comment_form_url = $(this).attr('action');
		var comment_text = $(this).find('.comment-input')[0].value;
		var post_id 	 = $(this).find('input[name="post_id"]')[0].value;
		var comment_count = $(this).parents('.parent-wrap').find('.comment-para span')[0];
		// console.log(comment_count);
		let request_data = {
			'post_id':post_id,
			'comment_text':comment_text,
			'csrf_token':csrftoken
		}
		$self = $(this)

		$.ajax({
				url : comment_form_url,
				data: request_data,
				type: 'POST',
				cache: false,
				success : function(response){
					// console.log(response);
					comment_count.textContent = parseInt(response.comments_count);
					$self.find('.comment-input')[0].value = "";
				}
		});
		return false;		

	});

	/*follow*/
	  // let follow_action = (form_class) => {

	  // };

	 $('form.follow-avatar--btn').on('submit',function(e){
	 	e.preventDefault();
	 	const follow_form_url = $(this).attr('action');
	 	var btn = $(this).find('button')[0];
	 	var to_user = $(this).find('input[name="to_user"]')[0].value;
	 	// console.log(to_user);

	 	let request_data = {
	 		'to_user__username':to_user,
	 		'csrf_token':csrftoken
	 	}
	 	$self = $(this);

		$.ajax({
				url : follow_form_url,
				data: request_data,
				type: 'POST',
				cache: false,
				// beforeSend: function(){ console.log('follow button clicked.')},
				success : function(response){
					// console.log(response);
					var text = response.is_follow ? 'UnFollow':'Follow';
					btn.textContent = text;
					if ($self.find('button').hasClass('btn--unfollow')){
						$self.find('button').removeClass('btn--unfollow');
						$self.find('button').addClass('btn--follow');
					}
					else if ($self.find('button').hasClass('btn--follow')){
						$self.find('button').removeClass('btn--follow');
						$self.find('button').addClass('btn--unfollow');
					}
				}
		});
		return false;

	 });

	 /*like*/
	$('.like-form').on('submit',function(e){
		e.preventDefault();
		const like_form_url = $(this).attr('action');
		let btn 		= $(this).find('button')[0];
		var post_id 	 = $(this).find('input[name="post_id"]')[0].value;
		var like_count = $(this).parents('.parent-wrap').find('.like-para span')[0];
		var like_text	= $(this).find('.like-text')[0];
		console.log(like_text.textContent);
		console.log(like_count);

		let request_data = {
			'post_id':post_id,
			'csrf_token':csrftoken
		}
		$self = $(this)

		$.ajax({
				url : like_form_url,
				data: request_data,
				type: 'POST',
				cache: false,
				success : function(response){
					if(response.liked == true){
						// console.log('unlike');
						like_count.textContent = parseInt(response.likes_count);
						like_text.textContent = 'UnLike';
						btn.innerHTML = "<i class='la la-thumbs-down unliked la-like--action-icon'></i>";

					}
					else{
						// console.log('like');
						like_text.textContent = 'Like';
						like_count.textContent = parseInt(response.likes_count);
						btn.innerHTML = "<i class='la la-thumbs-up liked la-like--action-icon'></i>";
					}
				}
		});
		return false;		

	});


});