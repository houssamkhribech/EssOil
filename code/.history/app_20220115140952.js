$("#btn-login").click(function () {
  console.log($("#userName").val());
  console.log($("#password").val());
  $.ajax({
    type: "POST",
    url: "/login",
    data: JSON.stringify({
      username: $("#username").val(),
      password: $("#password").val(),
    }),
    success: function (s) {
      converted = JSON.parse(s);
      location.reload(true /* forceReload: ne pas utiliser le cache */);
    },
    error: function () {
      alert("Mauvais mot de passe !");
    },
  });
});


$("#btn-logout").click(function () {
    console.log(localStorage)
    $.ajax({
      type: "GET",
      url: "/logout",
      success: function (s) {
        location.reload(true /* forceReload: ne pas utiliser le cache */);
      },
    });
  });