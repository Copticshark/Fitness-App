from flask import Flask, render_template, request

# Create an instance of the Flask class, which will act as the web server
app = Flask(__name__)

# Define the main route ("/") for the homepage
@app.route('/')
def home():
    # Render the 'index.html' template when the user visits the home page
    return render_template('index.html')

# Run the application in debug mode if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
