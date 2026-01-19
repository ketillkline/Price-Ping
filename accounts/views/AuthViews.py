from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model


def login_view(request: HttpRequest):
    # take out set
    errors = set()
    template_name = "login.html"
    match request.method:
        case "GET":
            return render(request, template_name)
        case "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            if not username or not password:
                errors.add("Please fill in all required fields")
                return render(request, template_name, {"errors": errors})
            user = authenticate(request, username=username, password=password)
            if not user:
                errors.add("Account does not exist")
                return render(request, template_name, {"errors": errors})
            login(request, user)
            return redirect("dashboard")



def signup_view(request: HttpRequest):
    template_name = "signup.html"
    match request.method:
        case "GET":
            return render(request, template_name)