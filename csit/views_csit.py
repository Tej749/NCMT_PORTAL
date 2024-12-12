''' views of CSIT modules'''

import logging

from django.shortcuts import render, redirect
from .models import Csit_2080, Csit_2079, Csit_2078, Csit_2077
from django.contrib import messages

logger = logging.getLogger("django")

# Create your views here.
'''CSIT home page function'''
def home(request):
    return render(request, "csit/base.html")

# Batch 2080
def csit80(request):
    da = Csit_2080.objects.all().order_by('id')
    return render(request, "csit/csit80.html", {'da':da})

def formcsit80(request):
    try:
        if request.method == "POST":
            data = request.POST
            name = data.get("name")
            dob = data.get("dob")
            symbol = data.get("symbol")
            reg = data.get("reg")
            mob = data.get("mob")
            add = data.get("add")
            guardian = data.get("guardian")
            prof = data.get("prof")
            mobs = data.get("mobs")
            Csit_2080.objects.create(name=name, dob=dob, symbol=symbol,
                                     reg=reg, mob=mob, add=add, guardian=guardian,
                                     prof=prof, mobs=mobs)
            messages.success(request, "Data successfully saved...")
            return redirect('/csit/csit80')
        return render(request, "csit/formcsit80.html")
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return redirect('/csit/csit80')


def editcsit80(request, pk):
    if request.method == "POST":
        datb = request.POST
        name = datb.get("name")
        dob = datb.get("dob")
        symbol = datb.get("symbol")
        reg = datb.get("reg")
        mob = datb.get("mob")
        add = datb.get("add")
        guardian = datb.get("guardian")
        prof = datb.get("prof")
        mobs = datb.get("mobs")
        db = Csit_2080.objects.get(id=pk)
        db.name = name
        db.dob = dob
        db.symbol = symbol
        db.reg = reg
        db.mob = mob
        db.add = add
        db.guardian = guardian
        db.prof = prof
        db.mobs = mobs
        db.save()
        return redirect('/csit/csit80')
    dm = Csit_2080.objects.get(id=pk)
    return render(request, "csit/editcsit80.html", {'dm':dm})

def delcsit80(request, pk):
    Csit_2080.objects.get(id=pk).delete()
    return redirect("/csit/csit80")

# Batch CSIT 2079

def csit79(request):
    da = Csit_2079.objects.all().order_by('id')
    return render(request, "csit/csit79.html", {'da':da})

def formcsit79(request):
    try:
        if request.method == "POST":
            data = request.POST
            name = data.get("name")
            dob = data.get("dob")
            symbol = data.get("symbol")
            reg = data.get("reg")
            mob = data.get("mob")
            add = data.get("add")
            guardian = data.get("guardian")
            prof = data.get("prof")
            mobs = data.get("mobs")
            Csit_2079.objects.create(name=name, dob=dob, symbol=symbol,
                                     reg=reg, mob=mob, add=add, guardian=guardian,
                                     prof=prof, mobs=mobs)
            messages.success(request, "Data successfully saved.")
            return redirect('/csit/csit79')
        return render(request, "csit/formcsit79.html")
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return redirect('/csit/csit79')


def editcsit79(request, pk):
    if request.method == "POST":
        datb = request.POST
        name = datb.get("name")
        dob = datb.get("dob")
        symbol = datb.get("symbol")
        reg = datb.get("reg")
        mob = datb.get("mob")
        add = datb.get("add")
        guardian = datb.get("guardian")
        prof = datb.get("prof")
        mobs = datb.get("mobs")
        db = Csit_2079.objects.get(id=pk)
        db.name = name
        db.dob = dob
        db.symbol = symbol
        db.reg = reg
        db.mob = mob
        db.add = add
        db.guardian = guardian
        db.prof = prof
        db.mobs = mobs
        db.save()
        return redirect("/csit/csit79")
    dm = Csit_2079.objects.get(id=pk)
    return render(request, "csit/editcsit79.html", {'dm':dm})

def delcsit79(request, pk):
    Csit_2079.objects.get(id=pk).delete()
    return redirect("/csit/csit79")

# Batch CSIT 2078

def csit78(request):
    da = Csit_2078.objects.all().order_by('id')
    return render(request, "csit/csit78.html", {'da':da})

def formcsit78(request):
    try:
        if request.method == "POST":
            data = request.POST
            name = data.get("name")
            dob = data.get("dob")
            symbol = data.get("symbol")
            reg = data.get("reg")
            mob = data.get("mob")
            add = data.get("add")
            guardian = data.get("guardian")
            prof = data.get("prof")
            mobs = data.get("mobs")
            Csit_2078.objects.create(name=name, dob=dob, symbol=symbol,
                                     reg=reg, mob=mob, add=add, guardian=guardian,
                                     prof=prof, mobs=mobs)
            messages.success(request, "Data successfully saved.")
            return redirect('/csit/csit78')
        return render(request, "csit/formcsit78.html")
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return redirect("/csit/csit78")

def editcsit78(request, pk):
    if request.method == "POST":
        datb = request.POST
        name = datb.get("name")
        dob = datb.get("dob")
        symbol = datb.get("symbol")
        reg = datb.get("reg")
        mob = datb.get("mob")
        add = datb.get("add")
        guardian = datb.get("guardian")
        prof = datb.get("prof")
        mobs = datb.get("mobs")
        db = Csit_2078.objects.get(id=pk)
        db.name = name
        db.dob = dob
        db.symbol = symbol
        db.reg = reg
        db.mob = mob
        db.add = add
        db.guardian = guardian
        db.prof = prof
        db.mobs = mobs
        db.save()
        return redirect("/csit/csit78")
    dm = Csit_2078.objects.get(id=pk)
    return render(request, "csit/editcsit78.html", {'dm':dm})

def delcsit78(request, pk):
    Csit_2078.objects.get(id=pk).delete()
    return redirect("/csit/csit78")

# Batch CSIT 2077

def csit77(request):
    da = Csit_2077.objects.all().order_by('id')
    return render(request, "csit/csit77.html", {'da':da})

def formcsit77(request):
    try:
        if request.method == "POST":
            data = request.POST
            name = data.get("name")
            dob = data.get("dob")
            symbol = data.get("symbol")
            reg = data.get("reg")
            mob = data.get("mob")
            add = data.get("add")
            guardian = data.get("guardian")
            prof = data.get("prof")
            mobs = data.get("mobs")
            Csit_2077.objects.create(name=name, dob=dob, symbol=symbol,
                                     reg=reg, mob=mob, add=add, guardian=guardian,
                                     prof=prof, mobs=mobs)
            messages.success(request, "Data successfully saved.")
            return redirect('/csit/csit77')
        return render(request, "csit/formcsit77.html")
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return redirect("/csit/csit77")

def editcsit77(request, pk):
    if request.method == "POST":
        datb = request.POST
        name = datb.get("name")
        dob = datb.get("dob")
        symbol = datb.get("symbol")
        reg = datb.get("reg")
        mob = datb.get("mob")
        add = datb.get("add")
        guardian = datb.get("guardian")
        prof = datb.get("prof")
        mobs = datb.get("mobs")
        print(name, guardian, reg, mob, add, prof, mobs, dob)
        db = Csit_2077.objects.get(id=pk)
        db.name = name
        db.dob = dob
        db.symbol = symbol
        db.reg = reg
        db.mob = mob
        db.add = add
        db.guardian = guardian
        db.prof = prof
        db.mobs = mobs

        print(db.guardian, db.name, db.prof)
        db.save()
        return redirect('/csit/csit77')
    dm = Csit_2077.objects.get(id=pk)
    return render(request, "csit/editcsit77.html", {'dm':dm})

def delcsit77(request, pk):
    Csit_2077.objects.get(id=pk).delete()
    return redirect("/csit/csit77")
