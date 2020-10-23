from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.conf import settings

import json

from core import paths
from common.fs import files


@method_decorator(csrf_exempt, name='dispatch')
class FilesId(View):
    def get(self, request, file_id, *args, **kwargs):
        root = paths.datasets_root()
        path = files.decode_base64s(file_id)
        data = files.get_info(root, path)
        return JsonResponse(data.toDict())
