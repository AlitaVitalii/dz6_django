from django.shortcuts import get_object_or_404, render

from .forms import PersonCreateForm, TriangleForm
from .models import Person


def triangle(request):
    form = TriangleForm(request.GET)
    if form.is_valid():
        cat1 = form.cleaned_data['cathetus1']
        cat2 = form.cleaned_data['cathetus2']
        gip = round((cat1**2 + cat2**2)**0.5, 2)
        return render(request, 'example.html', {'form': form, 'gip': gip})

    else:
        form = TriangleForm()

    return render(request, 'example.html', {'form': form})


def person_create(request):
    if request.method == "POST":
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            form.save()
            temp = "Person created"
            return render(request, "application/index.html", {'temp': temp})

    else:
        form = PersonCreateForm()
    return render(request, "application/person_create.html", {'form': form})


def person_update(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonCreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            temp = "Person updated"
            return render(request, "application/index.html", {'temp': temp})
    else:
        form = PersonCreateForm(instance=obj)
    return render(request, "application/person_update.html", {'form': form, "obj": obj})
