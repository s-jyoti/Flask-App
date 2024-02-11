# Flask-App
This is a Flask application that allows you to view the content of text files. The application provides a single GET route to display the content of a specified file in an HTML page. You can also specify start and end line numbers using optional URL query parameters.


# Getting Started
Follow these steps to run the File Viewer Flask App on your local machine.

# Prerequisites
Python 3.x
Flask (install with pip install Flask)
Project Structure
plaintext
Copy code
app.py: This is the main Flask application file.
templates/: This folder should contain your HTML templates.
file_viewer.html: HTML template for rendering the file content.
error.html: HTML template for displaying error details.
file1.txt: The sample file which we want to display. Place file2.txt, file3.txt, and file4.txt in the same directory if you want to use those files as well.

# Running the Application
Open a terminal and navigate to the directory containing app.py.

Run the following command to start the Flask development server:

# bash
Copy code
python app.py
Visit http://127.0.0.1:5000/file_viewer/ in your web browser.

# Usage
Access the default file: http://127.0.0.1:5000/file_viewer/
Specify a file: http://127.0.0.1:5000/file_viewer/file2.txt
Specify start and end line numbers: http://127.0.0.1:5000/file_viewer/file3.txt?start_line=2&end_line=5

# Troubleshooting
If you encounter any issues, check the following:

Correct URL: Ensure you are entering the correct URL in your browser.
Route Definition: Confirm that the route defined in app.py matches the URL you are trying to access.
Run the Flask App: Make sure the Flask application is running without errors.
Debug Mode: Enable Flask debug mode for detailed error messages.

# Author
Jyoti Singh
