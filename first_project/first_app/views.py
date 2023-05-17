from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np


def index(request) :
    return render(request,'index.html')
def about(request) :
    return render(request,'about.html')
def contact(request) :
    return render(request,'contact.html')
def detector(request) :
    return render(request,'detector.html')


def result(request):
    cls = joblib.load('finalized_model.sav')
    lis = [
        float(request.GET['Age']),
        float(request.GET['Total_Bilirubin']),
        float(request.GET['Direct_Bilirubin']),
        float(request.GET['Alkaline_Phosphotase']),
        float(request.GET['Alamine_Aminotransferase']),
        float(request.GET['Aspartate_Aminotransferase']),
        float(request.GET['Total_Protiens']),
        float(request.GET['Albumin']),
        float(request.GET['Albumin_and_Globulin_Ratio'])
    ]

    lis = np.array(lis).reshape(1, -1)
    ans = cls.predict(lis)[0]

    if ans == 0:
        result_message = "You don't have any liver disease. You are healthy."
    else:
        result_message = "You have been predicted to have a liver disease. We recommend consulting a doctor or taking a medical check-up for further evaluation and advice."

    return render(request, "result.html", {'result_message': result_message})
