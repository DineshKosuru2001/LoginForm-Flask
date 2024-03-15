# LoginForm-Flask
Created a web application that allows user to input data, validate it, store it in a database, retrieve it, and displayed it in table format.

# These requirements must be installed
Python 3.x installed on your system.
Flask and Flask-MySQLDB libraries installed (pip install flask flask-mysqldb).
MySQL database server installed and running.


# Setup
# Clone this repository to your local machine:
 => git clone <repository-url>

# Navigate to the project directory:
 => cd <project-directory>
 
# Create a virtual environment (optional but recommended):
=> python -m venv venv

# Activate the virtual environment:

# On Windows:
 => venv\Scripts\activate
# On macOS/Linux:
 => source venv/bin/activate

# Install dependencies:
 => pip install -r requirements.txt

# Configure MySQL:'
 => Ensure MySQL server is running.
 => Create a database named login.
 => Create a table named users with columns id (auto-increment), name, email, age, and date.

# Run the application:
 => python app.py

# Access the application in your web browser at http://127.0.0.1:5000.

# Usage
 # Adding a User:
  => Navigate to the homepage (http://127.0.0.1:5000) and fill out the form with your information (name, email, age, date), then click "Submit".
 # Viewing Users:
  => Navigate to /users to view a table containing all users' information.

  
# Project Structure
  app.py: Contains the Flask application and routes.
  templates/: Directory containing HTML templates.
  index.html: Template for the user input form.
  users.html: Template for displaying user information.
  static/: Directory containing static files (CSS, JavaScript).
  requirements.txt: File listing all Python dependencies.





