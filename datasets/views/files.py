from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator

import json

from core import paths
from common.fs import files


@method_decorator(csrf_exempt, name='dispatch')
class Files(View):
    def get(self, request, *args, **kwargs):
        data = files.get_info(paths.datasets_root())
        return JsonResponse(data.toDict())
