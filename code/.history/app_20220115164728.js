$("#btn-login").click(function () {
  $.ajax({
    type: "POST",
    url: "/login",
    data: JSON.stringify({
      username: $("#username").val(),
      password: $("#password").val(),
    }),
    success: function (s) {
      console.log("ok")
    },
    error: function () {
      alert("Mauvais mot de passe !");
    },
  });
});


$("#btn-logout").click(function () {
    
    $.ajax({
      type: "POST",
      url: "/logout",
      success: function (s) {
        console.log("ok")
      },
    });
  });

$("#btn-addUser").click(function () {
  console.log($("#role").val());
  

  $.ajax({
    type: "POST",
    url: "/add-user",
    data: JSON.stringify({
      role: $("#role").val(),
      lastname: $("#lastname").val(),
      firstname: $("#firstname").val(),
      matricule: $("#matricule").val(),
      mail: $("#mail").val(),
      password: $("#password").val(),
    }),
    success: function (s) {
      console.log("ok");
    },
    error: function () {
      alert("erreur interne");
    },
  });
});

$("#btn-addExperiment").click(function () {


  $.ajax({
    type: "POST",
    url: "/add-experiment",
    data: JSON.stringify({
      uid: $("#uid").val(),
      waterVolume: $("#waterVolume").val(),
      hydrolatVolume: $("#hydrolatVolume").val(),
      pressure: $("#pressure").val(),
      temperature: $("#temperature").val(),
      plantType: $("#plantType").val(),
      plantRef: $("#plantRef").val(),
      plantMass: $('#plantMass').val(),
      oilMass: $('#oilMass').val(),
      storage: $('#storage').val(),
      storageDate: $('#storageDate').val(),
      storageCondition: $('#storageCondition').val(),
    }),
    success: function (s) {
      console.log("ok");
    },
    error: function () {
      alert("erreur interne");
    },
  });
});


function RefreshListBox(){
  $.ajax({
      type: "GET",
      url: "get-all-listbox",
      success: function (answer) {
        data = JSON.parse(answer);
        console.log(data);
        $("#role").empty();
        $('#role').append('<option value="" selected="" disabled="">' + 'Sélectionner un rôle' + '</option>');
        for (var i = 0; i < data[0].length; i++) {
          $('#role').append('<option>' + data[0][i] + '</option>');
        }
        
        $("#plantType").empty();
        $('#plantType').append('<option value="" selected="" disabled="">' + 'Sélectionner une plante' + '</option>');
        for (var i = 0; i < data[1].length; i++) {
          $('#plantType').append('<option>' + data[1][i] + '</option>');
        }
        $("#storage").empty();
        $('#storage').append('<option value="" selected="" disabled="">' + 'Sélectionner un emplacement' + '</option>');
        for (var i = 0; i < data[2].length; i++) {
          $('#storage').append('<option>' + data[2][i] + '</option>');
        }*/
      },
      error: function () {
        alert("Erreur interne!");
      },
    });
}

$(document).ready(function(){
  RefreshListBox();

});