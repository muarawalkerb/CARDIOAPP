import joblib

#loading the saved prediction model.

def predict_heart_disease(data):
    model = joblib.load('heart_model.sav')
    prediction = model.predict(data)
    return prediction