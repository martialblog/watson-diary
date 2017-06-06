$(document).foundation();

$('#all_username').keydown(function(event) {
    if (event.keyCode == 13) {
      var reportAPI = "http://localhost:5000/v1/api/watson/data/"+$("#all_username").val()+"/reports";

      $('#all_entries tbody').empty();
      $.getJSON(reportAPI, function(data) {
        $.each(data, function(n, i) {
          console.log(i);
          $('#all_entries tbody').append('<tr class="child"><td>'+i.user+'</td><td>'+i.date+'</td><td>'+i.payload+'</td></tr>');
        });
      });

    };
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
