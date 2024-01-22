from django.shortcuts import render
from django.http import HttpResponse
from .hrtpredict import predict_heart_disease
import numpy as np

# Create your views here.
def home(request):
    
    return render(request,'home.html')

def predict(request):
    if request.method == 'POST':
        input_data = [int(request.POST['age']), int(request.POST['gender']), float(request.POST['height']),
                       float(request.POST['weight']), float(request.POST['Systolic blood pressure']), float(request.POST['Diastolic blood pressure']), 
                       float(request.POST['cholesterol']), float(request.POST['glucose']), int(request.POST['smoking']),
                         int(request.POST['alcoholic']), int(request.POST['Physical activity'])]
        
        data_array = np.asarray(input_data )
        arr = data_array.reshape(1,-1)
        prediction = predict_heart_disease(arr)
        return render(request, 'result.html', {'prediction': prediction})
    return render(request, 'predict.html')

# age, gender, height, weight, Systolic blood pressure, Diastolic blood pressure, cholesterol, glucose, smoking, alcoholic, Physical activity.

def comment(request):
    
    return render(request,'contact.html')