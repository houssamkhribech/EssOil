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
        }
      },
      error: function () {
        alert("Erreur interne!");
      },
    });
}
function RefreshExperiments() {
  $.ajax({
    type: "GET",
    url: "get-experiments",
    success: function (answer) {
      experiments = JSON.parse(answer);
      $("#experiments-table").empty();
      var row = $("<tr>");
        row.append($('<th scope="col">').text('uid'));
        row.append($('<th>').text('Eau [mL]'));
        row.append($('<th>').text('Hydrolat [mL]'));
        row.append($('<th>').text('Pression [mbar]'));
        row.append($('<th>').text('Température [°C]'));
        row.append($('<th>').text('Plante'));
        row.append($('<th>').text('Référence'));
        row.append($('<th>').text('Masse plante [g]'));
        row.append($('<th>').text('Masse huile [g]'));
        row.append($('<th>').text('Stockage'));
        row.append($('<th>').text('Date'));
        //row.append($('<th>').text('Remarque'));

        
        $("#experiments-table").append(row);
      for (var i = 0; i < experiments.length; i++) {
        row = $("<tr>");
        row.append($('<td>').text(experiments[i][0]));
        row.append($('<td>').text(experiments[i][1]));
        row.append($('<td>').text(experiments[i][2]));
        row.append($('<td>').text(experiments[i][3]));
        row.append($('<td>').text(experiments[i][4]));
        row.append($('<td>').text(experiments[i][5]));
        row.append($('<td>').text(experiments[i][6]));
        row.append($('<td>').text(experiments[i][7]));
        row.append($('<td>').text(experiments[i][8]));
        row.append($('<td>').text(experiments[i][9]));
        row.append($('<td>').text(experiments[i][10]));
        //row.append($('<td>').text(experiments[i][11]));

        $("#experiments-table").append(row);
      }
    },
    error: function () {
      alert("Erreur interne!");
    },
  });
}


function RefreshUsers() {
  $.ajax({
    type: "GET",
    url: "get-users",
    success: function (answer) {
      users = JSON.parse(answer);
      $("#users-table").empty();
      var row = $("<tr>");
        row.append($('<th>').text('user_id'));
        row.append($('<th>').text('Role'));
        row.append($('<th>').text('Matricule'));
        row.append($('<th>').text('Nom'));
        row.append($('<th>').text('Prénom'));
        row.append($('<th>').text('E-mail'));


        
        $("#users-table").append(row);
      for (var i = 0; i < users.length; i++) {
        row = $("<tr>");
        row.append($('<td>').text(users[i][0]));
        row.append($('<td>').text(users[i][1]));
        row.append($('<td>').text(users[i][2]));
        row.append($('<td>').text(users[i][3]));
        row.append($('<td>').text(users[i][4]));
        row.append($('<td>').text(users[i][5]));
      

        $("#users-table").append(row);
      }
    },
    error: function () {
      alert("Erreur interne!");
    },
  });
}

$(document).ready(function(){
  RefreshListBox();
  RefreshExperiments();
  RefreshUsers();
});