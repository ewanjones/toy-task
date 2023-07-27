from django.shortcuts import render

import json

from django.http import HttpResponse
from django.views import View


class Hello(View):
    def get(request, *args, **kwargs) -> HttpResponse:
        return HttpResponse(json.dumps({"success": True}), content_type="application/json")

