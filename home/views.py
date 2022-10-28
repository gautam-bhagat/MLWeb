from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Create your views here.

MODEL_PATH = "static/model/"

def home(request):
    return render(request,"index.html")
    
def admissionpred(request):
    if request.method=="GET":
        return render(request, "admissionprediction.html")

def admissionpredres(request):
    if request.method=="POST":
        gre = int(request.POST.get("gre"))
        toefl = int(request.POST.get("toefl"))
        rating = float(request.POST.get("rating"))
        lor = int(request.POST.get("lor"))
        cgpa = float(request.POST.get("cgpa"))
        # [gre,toefl,unirating,lor,cgpa]

        lis=[]
        lis.append(gre)
        lis.append(toefl)
        lis.append(rating)
        lis.append(lor)
        lis.append(cgpa)

        modelUrl = MODEL_PATH+"admission_prediction.sav"
        predictionModel = pickle.load(open(modelUrl,'rb'))
        output = predictionModel.predict([lis])
        output = output[0]*100
        roundfigure = round(output,2)
        cxt = {"admissionchance" : roundfigure}
        return render(request, "admissionpredictionres.html",cxt)
    