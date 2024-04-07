const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // Check if email and password match the expected values
    if (email === "admin_@gmail.com" && password === "p") {
        //alert("Login successful!");
        // Redirect to another page or perform other actions upon successful login
        window.location.href = "landing.html"; // Uncomment this line to redirect
    } else {
        var errorMessage = "Incorrect email or password. Please try again.";
        document.getElementById('error-message').innerText = errorMessage;
    }
}
