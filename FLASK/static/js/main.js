
function validateForm() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const age = parseInt(document.getElementById("age").value);
    const date = document.getElementById("date").value;

    let isValid = true;

    if (name === "") {
        document.getElementById("nameError").innerText = "Name is required";
        isValid = false;
    } else {
        document.getElementById("nameError").innerText = "";
    }

    if (email === "") {
        document.getElementById("emailError").innerText = "Email is required";
        isValid = false;
    } else {
        document.getElementById("emailError").innerText = "";
    }

    if (isNaN(age)) {
        document.getElementById("ageError").innerText = "Age is required";
        isValid = false;
    } else if( age <=0) {
        document.getElementById("ageError").innerText = "Age must be positive";
        isValid = false;
    } else {
        document.getElementById("ageError").innerText = "";

    }

    if (date === "") {
        document.getElementById("dateError").innerText = "Date is required";
        isValid = false;
    } else {
        document.getElementById("dateError").innerText = "";
    }

    return isValid;
}
    