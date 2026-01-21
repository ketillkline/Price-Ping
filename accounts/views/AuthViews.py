from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


def login_view(request: HttpRequest):
    template_name = "login.html"
    match request.method:
        case "GET":
            return render(request, template_name)
        case "POST":
            username = request.POST.get("username").strip()
            password = request.POST.get("password")

            if not username or not password:
                return render(request, template_name, {"errors": "Please fill in all required fields"})
            user = authenticate(request, username=username, password=password)
            if not user:
                return render(request, template_name, {"errors": "Account does not exist"})
            login(request, user)
            return redirect("dashboard")



def signup_view(request: HttpRequest):
    template_name = "signup.html"
    match request.method:
        case "GET":
            return render(request, template_name)
        case "POST":
            username = request.POST.get("username").strip()
            email = request.POST.get("email").strip()
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm-password")

            if not username or not password or not confirm_password:
                return render(request, template_name, {"errors": "Please fill in all required fields", "username": username,
                                                       "email": email})
            try:
                validator = EmailValidator()
                validator(email)
            except ValidationError as e:
                return render(request, template_name, {"errors": e, "username": username})

            if password != confirm_password:
                return render(request, template_name, {"errors": "Passwords must match", "username": username,
                                                       "email": email})
            if User.objects.filter(username=username, email=email).exists():
                return render(request, template_name, {"errors": f"Account under '{username}' already exists!"})
            
            user = User.objects.create_user(username=username, password=password, email=email)
            return redirect("/login/")


def recovery_view(request: HttpRequest):
    template_name = "recovery.html"
    match request.method:
        case "GET":
            return render(request, template_name)
        case "POST":
            email = request.POST.get("email").strip()
            try:
                validator = EmailValidator()
                validator(email)
            except ValidationError as e:
                return render(request, template_name, {"errors": e})

            if not email:
                return render(request, template_name, {"errors": "Please fill in all required fields"})
            
            if User.objects.filter(email=email).exists():
                return redirect('reset', email=email)
            return render(request, template_name, {"errors": f"Account under '{email}' does not exist."})






def reset_view(request: HttpRequest, email: str):
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

            
            user = User.objects.get(email=email)

def logout_view(request: HttpRequest):
    logout(request)
    return redirect("login")
