from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "dashboard.html"
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return render (request, self.template_name)
    def post(self, request, *args, **kwargs):
        pass
