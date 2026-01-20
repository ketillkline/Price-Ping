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
        case "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm-password")

            if not username or not password or not confirm_password:
                return render(request, template_name, {"errors": "Please fill in all required fields"})

            if password != confirm_password:
                return render(request, template_name, {"errors": "Passwords must match"})

            User = get_user_model()
            user = User.objects.create_user(username=username, password=password)


def recovery_view(request: HttpRequest):
    template_name = "recovery.html"
    match request.method:
        case "GET":
            return render(request, template_name)
        case "POST":
            email = request.POST.get("email")

            if not email:
                return render(request, template_name, {"errors": "Please fill in all required fields"})


def reset_view(request: HttpRequest):
    template_name = "reset.html"
    match request.method:
        case "GET":
            return render(request, template_name)

        case "POST":
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm-password")

            if not password or not confirm_password:
                return render(request, template_name, {"errors": "Please fill in all required fields."})

            if password != confirm_password:
                return render(request, template_name, {"errors": "Passwords must match"})

