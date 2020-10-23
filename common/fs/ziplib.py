import zipfile
import os
from common.fs import files

def do_zip(zip_path, root, fs):
    z = zipfile.ZipFile(zip_path, 'w')

    for f in fs:
        r, p, dest = files.merge_root_and_path(root, f)
        z.write(dest, arcname=os.path.basename(p))

    z.close()
