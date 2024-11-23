from flask import Flask, render_template, request
from Models.ai_model import predict_calories  # Import your AI function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get data from form (e.g., weight, height, goal, etc.)
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = int(request.form['age']) 
    gender = request.form['gender']
    goal = request.form['goal']

    # Use your AI model to predict calories or workout plan
    predicted_calories = predict_calories(weight, height, age, gender, goal)

    # Return results to the front-end (render a new template with results)
    return render_template("index.html", predicted_calories=predicted_calories)

if __name__ == '__main__':
    app.run(debug=True)
