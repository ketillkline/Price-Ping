from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, View):
    login_url = "/login/"
    template_name = "dashboard.html"
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return render (request, self.template_name)
    def post(self, request, *args, **kwargs):
        pass
