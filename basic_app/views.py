from django.shortcuts import render
from . import form
import pandas as pd  # libreria que permite manipular archivos
import matplotlib.pyplot as plt  # libreria para graficar datos
import numpy as np  # provee multidimensional soporte para objetos
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from django.core.mail import send_mail


# Create your views here.


def index(request):
    return render(request, 'index.html')


def training_model(array_to_train):
    df = pd.read_csv("./mastitis.csv")  # cargar los datos sobre mastitis
    df = df.set_index('ID_muestra')
    feature_col_names = ['ED',
                         'DEL',
                         'NP',
                         'PL',
                         'CE',
                         'CCS',
                         'SCCS']
    predicted_class_name = ['Resultado']
    X = df[feature_col_names].values
    y = df[predicted_class_name].values
    split_test_size = 0.30
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size, random_state=45)
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train.ravel())
    nb_predict_test = nb_model.predict(X_test)
    print("Accuracy: {0:.4f}".format(metrics.accuracy_score(y_test, nb_predict_test)))
    print("Confusion matrix")
    print("{0}".format(metrics.confusion_matrix(y_test, nb_predict_test)))
    print("")
    print("Classification Report")
    print(metrics.classification_report(y_test, nb_predict_test))
    # using the passed data to predict
    nb_predict_test = nb_model.predict([array_to_train])
    print(nb_predict_test)


def form_view(request):
    form_to_fill = form.Decease()
    if request.method == 'POST':
        form_to_fill = form.Decease(request.POST)

        if form_to_fill.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            array_of_values = [
                int(form_to_fill.cleaned_data['ED']),
                int(form_to_fill.cleaned_data['DEL']),
                int(form_to_fill.cleaned_data['NP']),
                int(form_to_fill.cleaned_data['PL']),
                int(form_to_fill.cleaned_data['CE']),
                int(form_to_fill.cleaned_data['CCS']),
                int(form_to_fill.cleaned_data['SCCS']),
            ]
            training_model(array_of_values)
            prediction_result_view(request, "test")

    return render(request, 'form_view.html', {'form': form_to_fill})


def prediction_result_view(request, pred="waiting data"):
    print("this was called", pred)
    return render(request, 'result.html', {"result": "pred"})
