// Add a submit event listener to the form with the id 'loginForm'
document.getElementById('loginForm').addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get the values of the username and password input fields
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Display an alert with the login details
    alert('Login clicked! Username: ' + username + ', Password: ' + password);
});
