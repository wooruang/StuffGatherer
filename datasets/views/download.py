from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.conf import settings

import os
import json
import mimetypes
import zipfile
import urllib

from common.fs import files, ziplib
from common.string import random
from common.image.annotation import annotation
from common.image import image
from core import paths


@method_decorator(csrf_exempt, name='dispatch')
class Download(View):
    def get(self, request, *args, **kwargs):
        root = paths.datasets_root()
        items = request.GET.getlist('items')

        if len(items) == 0:
            return HttpResponse(status=400)
        elif len(items) == 1:
            annotation = request.GET.get('annotype')
            if annotation:
                return self.makeFileResponseWithAnnotation(root, items[0], annotation)
            else:
                return self.makeFileResponse(root, items[0])
        else:
            temp_file_name = random.get_random_string(10) + '.zip'
            return self.zipFile(temp_file_name, root, items)

    @staticmethod
    def makeFileResponse(root, item):
        path = files.decode_base64s(item)

        root, path, file_url = files.merge_root_and_path(root, path)
        filename = os.path.basename(path)

        # print(file_url)
        if os.path.exists(file_url):
            with open(file_url, 'rb') as fh:
                quote_file_url = urllib.parse.quote(filename.encode('utf-8'))
                response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
                response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
                return response
        raise Http404

    @staticmethod
    def makeFileResponseWithAnnotation(root, item, annoType):
        path = files.decode_base64s(item)
        root, path, file_url = files.merge_root_and_path(root, path)
        filename = os.path.basename(path)
        
        # print(file_url)

        anno_url = files.replace_extension(file_url, 'json')

        if os.path.exists(anno_url):
            img = annotation.readAndDrawImageByAnnotationWithCoco(file_url, anno_url)
            img_ext = files.get_extension(file_url)
            ret, img_buf = image.encode_image(img, img_ext)
            quote_file_url = urllib.parse.quote(filename.encode('utf-8'))
            response = HttpResponse(img_buf.tostring(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response

        elif os.path.exists(file_url):
            with open(file_url, 'rb') as fh:
                quote_file_url = urllib.parse.quote(filename.encode('utf-8'))
                response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
                response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
                return response
        raise Http404

    @staticmethod
    def zipFile(zip_path, root, items):
        paths.make_datasets_cache_dir_if_not_exist()
        ps = []
        for i in items:
            ps.append(files.decode_base64s(i))
        cache_zip = paths.path_with_datasets_cache_root(zip_path)

        ziplib.do_zip(cache_zip, root, ps)

        print(cache_zip)

        if os.path.exists(cache_zip):
            with open(cache_zip, 'rb') as fh:
                quote_file_url = urllib.parse.quote(zip_path.encode('utf-8'))
                response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(cache_zip)[0])
                response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            
            files.remove_file(cache_zip)
            return response
        
        raise Http404
