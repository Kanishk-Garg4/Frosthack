from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Check, PinCity
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def checkup(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone']
        if request.POST['dry cough'] == "yes":
            dry_cough = True
        else:
            dry_cough = False
        if request.POST['tiredness'] == "yes":
            tiredness = True
        else:
            tiredness = False
        if request.POST['fever'] == "yes":
            fever = True
        else:
            fever = False
        other_symptoms = int(request.POST['other_symptoms'])
        if request.POST['chest-pain'] == "yes":
            chest_pain = True
        else:
            chest_pain = False
        if request.POST['breathing'] == "yes":
            breathing = True
        else:
            breathing = False

        patient = Check.objects.create(
            name=name, phone=phone_number,
            cough=dry_cough, fever=fever, Tiredness=tiredness,
            chest_pain=chest_pain, breathing_problem=breathing,
            other_symptoms=other_symptoms, date=timezone.now()
        )
        if Check.is_severe(patient):
            patient.save()
            display = "you need to get tested"
            return render(request, 'covidcheck/checkpage.html', {'display': display})
        else:
            display = "You seem to be fine"
        return render(request, 'covidcheck/mainpage.html', {'display': display})

    else:
        return render(request, 'covidcheck/mainpage.html')

def askpin(request):
    if request.method == 'POST':
        pin = request.POST['pin']
        if 100000 <= pin <= 1000000:
            messages.error(request, "invalid pin")
            return render(request, 'covidcheck/checkpage.html', messages)
        centres = PinCity.objects.filter(pin=pin)
        return render(request, 'covidcheck/checkpage.html', {'centers': centres})
    else:
        return render(request, 'covidcheck/checkpage.html')
