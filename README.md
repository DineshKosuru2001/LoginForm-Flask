
# HTML code index.html => loginpage code

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login Page</title>

<link rel="stylesheet" href="static\css\style.css">


</head>
<body>

    <div class="login">

        <h2>Login</h2>
        <form id="loginForm"  method="post" action="/" onsubmit="return validateForm()" >
            <div class="form-control">
                
                <input type="text" id="name" name="name" placeholder="Enter Name*">
                <div id="nameError" class="error-message"></div>
            </div>

            <div class="form-control">
                
                <input type="email" id="email" name="email" placeholder="Enter Email*">
                <div id="emailError" class="error-message"></div>
            </div>

            <div class="form-control">
                
                <input type="number" id="age" name="age" placeholder="Enter Age*">
                <div id="ageError" class="error-message"></div>
            </div>

            <div class="form-control">
                
                <input type="date" id="date" name="date">
                <div id="dateError" class="error-message"></div>
            </div>
            
            <div class="btn">
                <button type="submit">Submit</button>
            </div>
        </form>


    </div>


    
    <script src="static\js\main.js" ></script>
    
  

</body>
</html>


# css => responsive css


body{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 97.5vh;
    background-color: blueviolet;
}

.login{
    background-color:whitesmoke;
    width: 100%;
    max-width: 400px;
    border-radius: 6px;
    
}

.login h2{
    text-align: center;
    color: blueviolet;
    font-weight: 800;
    
    
}

.login form .form-control, .login form .btn {
    text-align: center;
   
}

.form-control input{
    width: 100%;
    max-width: 300px;
    padding: 10px;
    border-radius: 6px;
    border: 1px solid blueviolet;
    margin-bottom: 20px;
}



.btn button{

    width: 100%;
    max-width: 100px;
    padding: 8px;
    border-radius: 6px;
    border: 1px solid blueviolet;
    margin-bottom: 30px;
    background-color: blueviolet;
    color: aliceblue;
    font-weight: 500;
    
}

.error-message {
    color: red;
    font-size: 14px;
    transform: translateY(-15px);
        
}


# JavaScript => validation code


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

# users.html ( users data in tabular format)

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Users</title>

<style>

body{
    display: flex;
    align-items: start;
    justify-content: center;
    height: 97.5vh;
    
}


.table-info h2{
    color: blueviolet;
    text-align: center;
    
}

.table-info table, tr, td, th {
    border: 1px solid blueviolet;
    border-collapse: collapse;
    padding: 10px;
  
    

}









</style>









</head>

<body>

<div class="table-info">

    <h2>Users</h2>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Age</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody>
            {% for u in userDetails %}
            <tr>
                <td>{{ u[0] }}</td>
                <td>{{ u[1] }}</td>
                <td>{{ u[2] }}</td>
                <td>{{ u[3] }}</td>
                <td>{{ u[4] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>


</div>


</body>
   

</html>

# flask, Python Code.
# This code is for connecting database to server.
# I used Xampp and MYSQL database.

from flask import Flask, render_template, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "login"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST']) 

def index():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        date = request.form['date']


        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users (name, email, age, date) VALUES (%s, %s, %s, %s)", (name, email, age, date))
        mysql.connection.commit()

        cur.close()

        return "success"
    
    return render_template("index.html")



@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM users ")

    if users>0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails )

    users = cur.fetchall()
    
    cur.close()
    
    return render_template('users.html', users="users")

  

    

    

if __name__ == "__main__":
    app.run(debug=True)



    



