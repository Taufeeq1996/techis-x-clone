////////////////////////////
// LIKES
////////////////////////////

$(function() {
  // Global valuable
  var is_liked = false;

  // Clicked like icon
  $('.js-like').click(function() {
      var tweet_id = $(this).data('tweet-id');
      var like_count_obj = $(this).parent().find('.js-like-count');
      var like_count = Number(like_count_obj.html());
      var heart_icon_obj = $(this).find('img');
      var heart_icon_url = heart_icon_obj.attr('src');

      if (heart_icon_url == JS_ICON_HEART_GRAY) {
        // It has not been liked
        // Increase the count of likes
        $.ajax({
          url: '/tweetLikeAdd/' + tweet_id + '/',
          type: 'POST',
          data: {},
          headers: {'X-CSRFToken' : JS_CSRFTOKEN}
        })
        // Successful
        .done((data) => {
            // Increase
            var new_like_count = like_count + 1;
            like_count_obj.html(new_like_count);

            // Change the icon 
            heart_icon_obj.attr('src', JS_ICON_HEART_BLUE);
        })
        // Failure
        .fail((data) => {
            alert('Error');
            console.log(data);
        });
      } else {
        // It has been liked
        // Decrease the count of likes
        $.ajax({
            url: '/tweetLikeSubtract/' + tweet_id + '/',
              type: 'POST',
              data: {},
              headers: {'X-CSRFToken' : JS_CSRFTOKEN}
            })
            // Successful
            .done((data) => {
                // Decrease
                var new_like_count = like_count - 1;
                like_count_obj.html(new_like_count);

                // Change the button to blue
                heart_icon_obj.attr('src', JS_ICON_HEART_GRAY);
            })
            // Failure
            .fail((data) => {
                alert('Error');
                console.log(data);
            });
      }
  });

});