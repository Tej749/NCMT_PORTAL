import logging

from django.shortcuts import render, redirect
from .models import Staff

from django.contrib import messages
logger = logging.getLogger("django")

# Create your views here.

def main(request):
    return render(request, "org/main.html")

def signup(request):
    return render(request, "org/signup.html")

def home(request):
    return render(request, "org/base.html")

def staff(request):
    dm = Staff.objects.all().order_by('id')
    return render(request, "org/staff.html", {'dm':dm})

def form(request):
    try:
        if request.method == "POST":
            data = request.POST
            appt = data.get("appt")
            name = data.get("name")
            add = data.get("add")
            citizen = data.get("citizen")
            mob = data.get("mob")
            marital = data.get("marital")
            Staff.objects.create(appt=appt, name=name, add=add, citizen=citizen, mob=mob, marital=marital)
            messages.success(request, "Data successfully saved..")
            return redirect('/org/staff')
        return render(request, "org/form.html")
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return redirect("/org/staff")

def edit(request, pk):
    if request.method == "POST":
        data = request.POST
        appt = data.get("appt")
        name = data.get("name")
        add = data.get("add")
        citizen = data.get("citizen")
        mob = data.get("mob")
        marital = data.get("marital")
        dc = Staff.objects.get(id=pk)
        dc.appt = appt
        dc.name = name
        dc.add = add
        dc.citizen = citizen
        dc.mob = mob
        dc.marital = marital
        dc.save()
        return redirect("/org/staff")

    dm = Staff.objects.get(id=pk)
    return render(request, "org/edit.html", {'dm':dm})

def delstaff(request, pk):
    Staff.objects.get(id=pk).delete()
    return redirect("/org/staff")



