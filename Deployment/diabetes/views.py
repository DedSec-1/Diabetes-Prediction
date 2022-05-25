import pickle

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@csrf_exempt
def diabetes_pre(request):
    template = loader.get_template('index.html')
    #pregnancies = request.POST.get("Pregnancies")
    #glucose = request.POST.get("Glucose")
    bloodpressure = request.POST.get("BloodPressure")
    #skinthickness = request.POST.get("SkinThickness")
    #insulin = request.POST.get("Insulin")
    BMI = request.POST.get("BMI")
    #DiabetesPedigreeFunction = request.POST.get("DiabetesPedigreeFunction")
    age = request.POST.get("Age")

    diabetes_data = [
        [int(bloodpressure), float(BMI),int(age)]]
    diabetes_model = pickle.load(open('diabetes_model', 'rb'))
    # diabetes_model = pd.read_pickle('r',"diabetes_model.pickle")
    prediction = diabetes_model.predict(
        diabetes_data)
    outcome = prediction


    if outcome == 1:
        result = "Diabetic"
    elif outcome == 0:
        result = "Not Diabetic"


    return HttpResponse(template.render({'result':result}))
