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


function RefreshListBox(){
    
}