from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.conf import settings

import json

from core import paths
from common.fs import files, file_info


@method_decorator(csrf_exempt, name='dispatch')
class FilesChildren(View):
    def get(self, request, file_id, *args, **kwargs):
        order_by = request.GET.get('orderBy', 'name')
        order_direction = request.GET.get('orderDirection', 'ASC')
        root = paths.datasets_root()
        path = files.decode_base64s(file_id)
        data = {'items': file_info.todict(files.get_children(root, path))}
        return JsonResponse(data, safe=False)
