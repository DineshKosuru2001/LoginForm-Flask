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