from django.shortcuts import render
from .models import Check
from django.contrib import messages

# Create your views here.
def checkup(request):
    if request.method == 'POST':
        message_2 = request.POST['dry cough']
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

        a = Check.objects.create(
            cough=dry_cough, fever=fever, Tiredness=tiredness,
            chest_pain=chest_pain, breathing_problem=breathing,
            other_symptoms=other_symptoms)
        if Check.is_severe(a):
            a.save()
            display = "you need to get tested"
            messages.error(request, "You need to get tested")
        else:
            display = "You seem to be fine"
        return render(request, 'covidcheck/checkpage.html', {'display': display, 'message': messages})

    else:
        return render(request, 'covidcheck/mainpage.html')
