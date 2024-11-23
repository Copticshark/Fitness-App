# Pandas is a popular library used for data manipulation and analysis.
#  It is commonly used to load, clean, and organize data, making it easier
#  to use in machine learning models. In the ai_model.py file, pandas is
#  used to create a DataFrame, which is essentially a table of data that 
# can be processed and analyzed.
#scikit-learn is a machine learning library that provides tools to build 
# models such as linear regression, classification, clustering, etc. In the example,
#  LinearRegression is used to create a model that predicts calories based on input
#  features like weight, height, gender, and goal.
#Linear Regression: This is a simple machine learning algorithm used to predict a continuous
#  target variable (in this case, calories) based on input features.
#In the example, the model is trained with some dummy data (the data dictionary), and then
#  it predicts the calories based on the user's input.
import pandas as pd
from sklearn.linear_model import LinearRegression

# Example function that predicts calorie needs based on input features
def predict_calories(weight, height, gender, goal):
    # Dummy data to train the model (You would replace this with your own dataset)
    data = {
        'weight': [50, 60, 70, 80, 90],
        'height': [150, 160, 170, 180, 190],
        'age':[15, 25, 35, 55, 75],
        'gender': ['male', 'female', 'male', 'female', 'male'],
        'goal': ['lose', 'maintain', 'gain', 'lose', 'maintain'],
        'calories': [2000, 2200, 2500, 2100, 2400]  # Dummy calorie values
    }
    df = pd.DataFrame(data)

    # Preprocessing the input data
    gender_numeric = 1 if gender == 'male' else 0  # Encoding gender as numeric
    goal_numeric = 1 if goal == 'gain' else 0  # Simple encoding for goal

    # Define the features and target variable
    X = df[['weight', 'height', 'age', 'gender', 'goal']]  # Features
    X['gender'] = X['gender'].apply(lambda x: 1 if x == 'male' else 0)
    X['goal'] = X['goal'].apply(lambda x: 1 if x == 'gain' else 0)
    y = df['calories']  # Target variable

    # Train a Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # Prepare input data for prediction
    input_data = [[weight, height, gender_numeric, goal_numeric]]

    # Make prediction
    predicted_calories = model.predict(input_data)
    return predicted_calories[0]  # Return the predicted calorie value
