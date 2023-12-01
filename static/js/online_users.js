$(document).ready(function(){
    console.log("se pudo");
    var onlineUsersDiv = $('#online-users-list');
    var noOnlineUsersMessage = $('#no-online-users-message');
    
    function updateOnlineUsers() {
        $.getJSON(onlineUsersUrl, function(data) {
            var users = data['users'];
            onlineUsersDiv.empty();
    
            if (users.length > 0) {
                for (var i = 0; i < users.length; i++) {
                    var userDiv = $('<div class="col-xl-6 col-lg-7 col-md-12"></div>');
                    var cardDiv = $('<div class="card profile-header"></div>');
                    var bodyDiv = $('<div class="body"></div>');
                    var rowDiv = $('<div class="row"></div>');
  
                    var col1Div = $('<div class="col-lg-4 col-md-4 col-12"></div>');
                    var profileImageDiv = $('<div class="profile-image float-md-right"></div>');
  
                    if (users[i].profile_picture) {
                        profileImageDiv.append('<img src="' + users[i].profile_picture + '" alt="' + users[i].username + '" class="user-image">');
                    } else {
                        profileImageDiv.append('<img src="/static/images/user_unknown.png" alt="' + users[i].username + '" class="user-image">');
                    }
  
                    col1Div.append(profileImageDiv);
  
                    var col2Div = $('<div class="col-lg-8 col-md-8 col-12"></div>');
                    col2Div.append('<h4 class="m-t-0 m-b-0"><strong>' + users[i].username + '</strong></h4>');
                    col2Div.append('<span class="job_post">' + (users[i].is_active ? 'Activo' : 'Inactivo') + '</span>');
                    col2Div.append('<p>' + users[i].biography + '</p>');
  
                    rowDiv.append(col1Div);
                    rowDiv.append(col2Div);
                    bodyDiv.append(rowDiv);
                    cardDiv.append(bodyDiv);
                    userDiv.append(cardDiv);
  
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
    setInterval(function() {
        checkFirstLoad();
        updateOnlineUsers();
    }, 5000);
  });
  