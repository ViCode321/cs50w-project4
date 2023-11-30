$(document).ready(function(){
    console.log("se pudo")
    var onlineUsersDiv = $('#online-users-list');
    var noOnlineUsersMessage = $('#no-online-users-message');

    function updateOnlineUsers() {
        $.getJSON(onlineUsersUrl, function(data) {
            var onlineUsers = data['online_users'];
            onlineUsersDiv.empty();

            if (onlineUsers.length > 0) {
                onlineUsersDiv.append('<h3>Usuarios en línea:</h3>');
                for (var i = 0; i < onlineUsers.length; i++) {
                    onlineUsersDiv.append('<p>' + onlineUsers[i] + '</p>');
                }
                noOnlineUsersMessage.hide();
            } else {
                noOnlineUsersMessage.show().text('No hay usuarios en línea en este momento.');
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
    setInterval(function() {
        checkFirstLoad();
        updateOnlineUsers();
    }, 5000);
});
