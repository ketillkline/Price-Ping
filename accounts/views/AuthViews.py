from django.http import HttpRequest
from django.shortcuts import render, redirect

def login_view(request: HttpRequest):
    template_name = "login.html"
    match request.method:
        case "GET":
            return render(request, template_name)
def signup_view(request: HttpRequest):
    template_name = "signup.html"
    match request.method:
        case "GET":
            return render(request, template_name)