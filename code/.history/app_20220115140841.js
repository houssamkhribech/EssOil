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
      console.log(s);
      localStorage.setItem("matricule", converted.matricule); // Afin de sauvegarder les parametres de l'utilisateur localement sur le pc jusqu'a liberation
      localStorage.setItem("lastname", converted.lastname);
      localStorage.setItem("firstname", converted.firstname);
      localStorage.setItem("role", converted.role);
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
        localStorage.removeItem('matricule');
        localStorage.removeItem('lastname');
        localStorage.removeItem('firstname');
        localStorage.removeItem('role');
        location.reload(true /* forceReload: ne pas utiliser le cache */);
      },
    });
  });