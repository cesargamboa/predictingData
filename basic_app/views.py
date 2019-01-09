from django.shortcuts import render
from . import form
# Create your views here.


def index(request):
    return render(request, 'index.html')

def form_view(request):
    form_to_fill = form.Decease()
    if request.method == 'POST':
        form_to_fill = form.Decease(request.POST)

        if form_to_fill.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("Num1: " + str(form_to_fill.cleaned_data['num1']))
            print("Num2: " + str(form_to_fill.cleaned_data['num2']))
            print("Num3: " + str(form_to_fill.cleaned_data['num3']))
            print("Num4: " + str(form_to_fill.cleaned_data['num4']))
            print("Num5: " + str(form_to_fill.cleaned_data['num5']))
            print("Num6: " + str(form_to_fill.cleaned_data['num6']))

    return render(request, 'form_view.html', { 'form' : form_to_fill})
