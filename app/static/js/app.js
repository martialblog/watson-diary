$(document).foundation();

// $('#user_list ul').empty();
$.getJSON('http://localhost:5000/v1/api/watson/users', function(data) {
  $.each(data, function(n, i) {

    var username = i._id;
    console.log(username);

    $('#user_list').append('<li class="child">'+ username +'</li>');
  });

});

$("#new_button").click(function() {

  var reportAPI = "http://localhost:5000/v1/api/watson/data/"+$("#new_username").val()+"/reports/"+$("#new_date").val();

  $.ajax({
    type: 'PUT',
    dataType: 'json',
    url: reportAPI,
    headers: {"X-HTTP-Method-Override": "PUT"}
  });
});
