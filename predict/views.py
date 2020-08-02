from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
#import
# Create your views here.

def predict(request):
    return render(request,'prediction.html')

def predict_chances(request):

    if request.POST.get('action')=='post':

        sepal_length=float(request.POST.get('sepal_length'))
        sepal_width=float(request.POST.get('sepal_width'))
        petal_length=float(request.POST.get('petal_length'))
        petal_width=float(request.POST.get('petal_width'))

        model=pd.read_pickle(r'C:\Users\003560\Desktop\IrisPrediction\predict\new_model.pickle')
        result=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])

        classification=result[0]

        # Result.objects.create(sepal_length=sepal_length,sepal_width=sepal_width,
        # petal_length=petal_length,petal_width=petal_width,classification=classification)

        return JsonResponse({'result':classification,'sepal_length':sepal_length,
        'sepal_width':sepal_width,'petal_length':petal_length,'petal_width':petal_width},safe=False)
