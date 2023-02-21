from application.tasks import send_email_task

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmailForm, PersonCreateForm, TriangleForm
from .models import Person


def email_form(request):
    form = EmailForm(request.GET)
    if form.is_valid():
        email = form.cleaned_data['email']
        text = form.cleaned_data['text']
        date = form.cleaned_data['date']
        send_email_task.apply_async((
            email,
            text
        ), eta=date)
        messages.add_message(request, messages.SUCCESS, 'Message sent')

        return redirect('email-name')

    elif request.GET:
        return render(request, 'email.html', {'form': form})

    else:
        form = EmailForm()

    return render(request, 'email.html', {'form': form})


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
