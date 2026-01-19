from django.http import HttpRequest
from django.shortcuts import render, redirect
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


def login_view(request: HttpRequest):
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


def signup_view(request: HttpRequest):
    template_name = "signup.html"
    match request.method:
        case "GET":
            return render(request, template_name)