from django.shortcuts import render

# Create your views here.

def predict(request):
    return render(request,'prediction.html')

def predict_chances(request):

    if request.POST.get('action')=='post':

        sepal_length=float(request.POST.get('sepal_length'))
        sepal_width=float(request.POST.get('sepal_width'))
        petal_length=float(request.POST.get('petal_length'))
        petal_width=float(request.POST.get('petal_width'))
