import os
import datetime
import base64
import stat
from .file_info import FileInfo, Capabilities, todict


def get_info(root, path='/'):
    root, path, p = merge_root_and_path(root, path)
    st = os.stat(p)

    info = FileInfo()

    info.id = encode_base64s(path)

    info.createdTime = cvt_timestamp_to_isoformat(st.st_ctime)
    info.modifiedTime = cvt_timestamp_to_isoformat(st.st_mtime)

    info.type = type_name_by_stat(st)
    if info.type == 'file':
        info.size = st.st_size

    if path != '/':
        info.capabilities = Capabilities.CommonCapabities()
        info.name = os.path.basename(path)
        info.parentId = encode_base64s(os.path.dirname(path))

        # path must be '/' + 'a/b/c' 
        tokens = path.split('/')[:-1]
        ancs = []
        ancs_path = '/'
        for t in tokens:
            ancs_path = os.path.join(ancs_path, t)
            ancs.append(get_info(root, ancs_path))
        info.ancestors = ancs
    else:
        info.capabilities = Capabilities.RootCapabilities()
        info.name = os.path.basename(root)

    return info


def get_children(root, path='/'):
    root, path, p = merge_root_and_path(root, path)

    result = []
    for n in os.listdir(p):
        child = os.path.join(path, n)
        result.append(get_info(root, child))
    return result


def merge_root_and_path(root, path):
    if root is None or len(path) == 0:
        root = '/'
    if path is None or len(path) == 0:
        path = '/'

    path = add_firt_segment(path)
    path = remove_last_segment(path)
    root = remove_last_segment(root)

    # path -> /a/b/c(O), a/b/c/(X), /a/b/c/(X), a/b/c(X)
    # root -> /root(O), /root/(X)
    return root, path, os.path.join(root, path[1:])


def type_name_by_stat(st):
    if stat.S_ISDIR(st.st_mode):
        return 'dir'
    else:
        return 'file'


def add_firt_segment(p):
    if p is None or len(p) == 0:
        return '/'
    return p if p[0] == '/' else '/' + p

def remove_last_segment(p):
    if p is None or len(p) == 0:
        return ''
    elif len(p) > 1 and p[-1] == '/':
        return p[:-1]
    else:
        return p


def cvt_timestamp_to_isoformat(stamp):
    '''
    Convert a timestamp to a string of isoformat
    '''
    return datetime.datetime.fromtimestamp(stamp).isoformat()[:-3]+'Z'


def remove_file(path):
    if os.path.exists(path):
         os.remove(path)


# TODO: below functions divide from this script.

def encode_base64(s):
    '''
    Convert a string to bytes of base64.
    '''
    b = s.encode()
    return base64.urlsafe_b64encode(b)


def decode_base64(s):
    '''
    Convert a string to bytes of base64.
    '''
    b = s.encode()
    return base64.urlsafe_b64decode(b)


def encode_base64s(s):
    '''
    Convert a string to bytes of base64.
    '''
    b = encode_base64(s)
    return str(b, encoding='utf-8')


def decode_base64s(s):
    '''
    Convert a string to bytes of base64.
    '''
    b = decode_base64(s)
    return str(b, encoding='utf-8')


if __name__ == "__main__":
    p = "/Users/hansaemlee/Documents/temp"
    ro = "/Users/hansaemlee/Documents/temp"
    pa = "비행기/META-INF/container.xml"
    a = os.stat(p)

    #2020-10-20T13:15:30.218Z
    print(cvt_timestamp_to_isoformat(a.st_atime))
    print(to_base64_str(p))
    print(stat.filemode(a.st_mode))
    print(type_name_by_stat(a))
    print(a)
    ed = get_info(ro, pa)
    print(ed)
    import json
    # print(json.dumps(todict(ed), ensure_ascii=False, allow_nan=False))
    print(ed.toJson())

    cd = todict(get_children(ro))
    # print(json.dumps(cd, ensure_ascii=False, allow_nan=False))

    # print(add_firt_segment('/'))
    # print(add_firt_segment(''))
    # print(add_firt_segment('/a/b/c'))
    # print(add_firt_segment('a/b/c'))
    # print(add_firt_segment('/a'))
    # print(add_firt_segment('a/'))
    # print('\n\n')

    # print(remove_last_segment('/'))
    # print(remove_last_segment(''))
    # print(remove_last_segment('/a/b/c'))
    # print(remove_last_segment('a/b/c'))
    # print(remove_last_segment('a/b/c/'))
    # print(remove_last_segment('/a'))
    # print(remove_last_segment('a/'))

    b = '/'
    b = add_firt_segment(b)
    b = remove_last_segment(b)
    print(b)

    b = 'a/b/c'
    b = add_firt_segment(b)
    b = remove_last_segment(b)
    print(b)

    b = 'a/b/c/'
    b = add_firt_segment(b)
    b = remove_last_segment(b)
    print(b)

    b = '/a/b/c'
    b = add_firt_segment(b)
    b = remove_last_segment(b)
    print(b)

    b = '/a/b/c/'
    b = add_firt_segment(b)
    b = remove_last_segment(b)
    print(b)
