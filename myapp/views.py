from django.shortcuts import render
from myapp.models import water
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import redirect


def formareg(request):
    if request.method == "POST":
        data = request.POST
        newUser = User.objects.create_user(data["Name"],data["email"] , data["psw"])
        newUser.save()
        return HttpResponse(f'Пользователь {data["Name"]} успешно создан')
    else :
        return render(request,"formareg.html")


def login(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username = data["Name"],
        password = data["psw"])
        if user is not None:
            request.session["is_login"] = user.username
            return HttpResponse(f"Привет ,{user.password}")
        else :
            return HttpResponse(f"Неверный пароль")
    else:
        return render(request,"login.html")            


def index(request):
    name = request.session.get("is_login" , "no log")
    if name != "no log":
        res = water.objects.all()
        if request.method == "POST":
            data = request.POST
            new = water(name = data["field1"],color = data["field2"] , cost = data["field3"] ,count = data["field4"], volume = data["field5"])
            new.save()

            return render(request , "index.html" , {"prod":res,"username":name})
        
        else :
            return render(request, "index.html" , {"prod":res,"username":name})    
    else:
        return redirect(login)


    
# Create your views here.
