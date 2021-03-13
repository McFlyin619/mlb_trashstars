var url = 'http://127.0.0.1:8000/api'
function comment() {
    var by = $('#by').val();
    var thread = $('#thread').val();
    var comment_body = $('#comment_body').val() 

    $.ajax({
        type: 'POST',
        url: url + '/comments/',
        dataType: 'json',
        contentType: 'application/json',
        data:{
            'by':by,
            'thread':thread,
            'comment_body':comment_body,
        },
        success: function(response){
            console.log('It Works',response);
        
        },
        error: function(errorDetails) {
            console.log('Something went wrong....', errorDetails);
        }
    })
}



function init() {
    console.log('comment.js loaded');

    $('#sendit').on('click',function(){
        comment();
    });
}

window.onload = init;