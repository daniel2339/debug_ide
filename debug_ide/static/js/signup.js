


const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value


function signup(){

    console.log(csrftoken)

    username = document.getElementById('username').value
    email = document.getElementById('email').value
    password = document.getElementById('password').value
    passwordcheck =document.getElementById('passwordcheck').value

    if(username == '' ||email == ''||password == ''|| passwordcheck ==''){
        alert('請輸入正確資料');
        return
    }

    if(password != passwordcheck){
        alert('請確認密碼！');
        return
    }

    $.ajax({
        url   :"/debug_ide/signupData",
        type  : "POST",
        async : true,
        accept: "application/json",
        headers: {"X-CSRFToken" : csrftoken},
        data  : {
            'username' : username,
            'email' : email,
            'password' :password,
            'passwordcheck':passwordcheck
        },
        success: function (data, textStatus, jqXHR) {
            alert('註冊成功')
            window.location.replace("/debug_ide")
        },
        error: function(){
            alert('註冊失敗')
        }
    });
}