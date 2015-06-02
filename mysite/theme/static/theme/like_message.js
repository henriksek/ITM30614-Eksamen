

$(document).ready(function() {
    $(".like_message").click(
        function(event){
            event.preventDefault();
            var messageid = $(this).attr("data-messageid");
            var clicked_element = $(this);
            $.ajax({
                url: "/message_app/like_message/" + messageid
            })
            .done(function(data) {
                var total_likes = data['total_likes'];
                var like_counter = $(".like_counter." + messageid);
                /*console.log(typeof like_counter);
                console.log(like_counter);
                console.log(total_likes);*/
                like_counter.html(total_likes);
            });
        }
    )
});