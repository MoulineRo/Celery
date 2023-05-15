import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from polls.forms import PhoneForm, SmsForm
from polls.models import Approved, Phone
from .tasks import send_phone, smss


def phone(request):
    if request.method == "GET":
        form = PhoneForm()
        context = {"form": form}
        return render(request, "phone.html", context)
    elif request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            send_phone.delay()
            return HttpResponseRedirect(reverse("sms"))
        return render(request, 'phone.html', {'form': form})


def sms(request):
    if request.method == "GET":
        form = SmsForm()
        context = {"form": form}
        return render(request, "sms.html", context)
    if request.method == "POST":
        form = SmsForm(request.POST)
        if form.is_valid():
            form.save()
            smss.delay()
            time.sleep(1)
            if Approved.objects.latest('id').phone == Phone.objects.latest('id').phone:
                if Approved.objects.latest('id').approved == 'approved':
                    return HttpResponse(' All is ok')
        return render(request, 'sms.html', {'form': form})
