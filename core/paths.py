import os

from django.conf import settings

from common.fs import files


def datasets_root():
    return settings.DATASETS_ROOT_PATH


def datasets_cache_root():
    return path_with_datasets_root(settings.DATASETS_CACHE_PATH)


def path_with_datasets_root(path):
    root = datasets_root()
    root, p, dest = files.merge_root_and_path(root, path)
    return dest


def path_with_datasets_cache_root(path):
    cache_path = datasets_cache_root()
    cache_path, p, dest = files.merge_root_and_path(cache_path, path)
    return dest


def make_datasets_cache_dir_if_not_exist():
    cache_path = datasets_cache_root()
    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
