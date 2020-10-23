from django.urls import path

from .views.files import Files
from .views.files_id import FilesId
from .views.files_children import FilesChildren
from .views.download import Download

urlpatterns = [
    path('files', Files.as_view()),
    path('files/', Files.as_view()),
    path('files/<file_id>', FilesId.as_view()),
    path('files/<file_id>/', FilesId.as_view()),
    path('files/<file_id>/children', FilesChildren.as_view()),
    path('files/<file_id>/children/', FilesChildren.as_view()),
    # path('files/<file_id>/search', Files.as_view()),
    # path('files/<file_id>/search/', Files.as_view()),
    path('download', Download.as_view()),
    path('download/', Download.as_view()),
]
