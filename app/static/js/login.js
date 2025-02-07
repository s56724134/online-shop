document.getElementById('show-signup').addEventListener('click', function (event) {
    event.preventDefault(); // 阻止連結的默認跳轉行為
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('sign-up-form').style.display = 'block';
});


document.getElementById('show-login-form').addEventListener('click', function (event) {
    event.preventDefault(); // 阻止連結的默認跳轉行為
    document.getElementById('login-form').style.display = 'block';
    document.getElementById('sign-up-form').style.display = 'none';
});

