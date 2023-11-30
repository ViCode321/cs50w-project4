$(document).ready(function () {
    console.log("se pudo");
    var onlineUsersDiv = $('#online-users-list');
    var noOnlineUsersMessage = $('#no-online-users-message');

    function updateOnlineUsers() {
        $.getJSON(onlineUsersUrl, function (data) {
            var users = data['users'];
            onlineUsersDiv.empty();

            if (users.length > 0) {
                onlineUsersDiv.append('<h3>Usuarios:</h3>');
                for (var i = 0; i < users.length; i++) {
                    var userDiv = $('<div class="user">' + users[i].username + '</div>');
                    if (users[i].is_active) {
                        userDiv.addClass('active');
                    } else {
                        userDiv.addClass('inactive');
                    }
                    onlineUsersDiv.append(userDiv);
                }
            } else {
                noOnlineUsersMessage.show().text('No hay usuarios en este momento.');
            }
        });
    }

    var firstLoad = true;

    function checkFirstLoad() {
        if (firstLoad) {
            noOnlineUsersMessage.show().text('Cargando...');
            firstLoad = false;
        }
    }

    checkFirstLoad();
    updateOnlineUsers();
    setInterval(function () {
        checkFirstLoad();
        updateOnlineUsers();
    }, 5000);
});
