from django.shortcuts import render
from django.views.generic import TemplateView

class KontaktView(TemplateView):
    template_name="kontakt.html"

class PatronView(TemplateView):
    template_name="patron.html"