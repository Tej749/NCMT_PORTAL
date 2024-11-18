from timeit import default_timer

from django.shortcuts import render, redirect
from .models import Bca_2080, Bca_2079, Bca_2078, Bca_2077

# Create your views here.

def home(request):
    return render(request, "bca/base.html")


# BCA 2080
def bca80(request):
    da = Bca_2080.objects.all()
    return render(request, "bca/bca80.html", {'da':da})

def formbca80(request):
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
        Bca_2080.objects.create(name=name, dob=dob, symbol=symbol, reg=reg, mob=mob, add=add, guardian=guardian, prof=prof, mobs=mobs)
        return redirect('/bca/bca80')
    return render(request, "bca/formbca80.html")

def editbca80(request, pk):
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
        dt = Bca_2080.objects.get(id=pk)
        dt.name = name
        dt.dob = dob
        dt.symbol = symbol
        dt.reg = reg
        dt.mob = mob
        dt.add = add
        dt.guardian = guardian
        dt.prof = prof
        dt.mobs = mobs
        dt.save()
        return redirect('/bca/bca80')
    dm = Bca_2080.objects.get(id=pk)
    return render(request, "bca/editbca80.html", {'dm':dm})

def delbca80(request, pk):
    Bca_2080.objects.get(id=pk).delete()
    return redirect("/bca/bca80")

# BCA 2079

def bca79(request):
    da = Bca_2079.objects.all()
    return render(request, "bca/bca79.html", {'da':da})

def formbca79(request):
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
        Bca_2079.objects.create(name=name, dob=dob, symbol=symbol, reg=reg, mob=mob, add=add, guardian=guardian, prof=prof, mobs=mobs)
        return redirect('/bca/bca79')
    return render(request, "bca/formbca79.html")

def editbca79(request, pk):
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
        db = Bca_2079.objects.get(id=pk)
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
        return redirect("/bca/bca79")
    dm = Bca_2079.objects.get(id=pk)
    return render(request, "bca/editbca79.html", {'dm':dm})

def delbca79(request, pk):
    Bca_2079.objects.get(id=pk).delete()
    return redirect("/bca/bca79")

# BCA 2078

def bca78(request):
    da = Bca_2078.objects.all()
    return render(request, "bca/bca78.html", {'da':da})

def formbca78(request):
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
        Bca_2078.objects.create(name=name, dob=dob, symbol=symbol, reg=reg, mob=mob, add=add, guardian=guardian, prof=prof, mobs=mobs)
        return redirect('/bca/bca78')
    return render(request, "bca/formbca78.html")

def editbca78(request, pk):
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
        dt = Bca_2078.objects.get(id=pk)
        dt.name = name
        dt.dob = dob
        dt.symbol = symbol
        dt.reg = reg
        dt.mob = mob
        dt.add = add
        dt.guardian = guardian
        dt.prof = prof
        dt.mobs = mobs
        dt.save()
        return redirect('/bca/bca78')
    dm = Bca_2078.objects.get(id=pk)
    return render(request, "bca/editbca78.html", {'dm':dm})

def delbca78(request, pk):
    Bca_2078.objects.get(id=pk).delete()
    return redirect("/bca/bca78")

# BCA 2077

def bca77(request):
    da = Bca_2077.objects.all()
    return render(request, "bca/bca77.html", {'da':da})

def formbca77(request):
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
        Bca_2077.objects.create(name=name, dob=dob, symbol=symbol, reg=reg, mob=mob, add=add, guardian=guardian, prof=prof, mobs=mobs)
        return redirect('/bca/bca77')
    return render(request, "bca/formbca77.html")

def editbca77(request, pk):
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
        dt = Bca_2077.objects.get(id=pk)
        dt.name = name
        dt.dob = dob
        dt.symbol = symbol
        dt.reg = reg
        dt.mob = mob
        dt.add = add
        dt.guardian = guardian
        dt.prof = prof
        dt.mobs = mobs
        dt.save()
        return redirect('/bca/bca77')
    dm = Bca_2077.objects.get(id=pk)
    return render(request, "bca/editbca77.html", {'dm':dm})

def delbca77(request, pk):
    Bca_2077.objects.get(id=pk).delete()
    return redirect("/bca/bca77")



