from main import logger, curdir, origdir, moddir
from lib import get_path

import os
import hashlib
import IPython


def request(flow):
    pass


def response(flow):
    url = flow.request.url
    orig_path = get_path(url, origdir)
    orig_dir_path = os.path.dirname(orig_path)
    if not os.path.exists(orig_dir_path):
        os.makedirs(orig_dir_path)
    with open(orig_path, 'wb') as fp:
        fp.write(flow.response.content)

    mod_path = get_path(url, moddir)
    if os.path.exists(mod_path):
        # rewrite response
        with open(mod_path, 'rb') as fp:
            flow.response.content = fp.read()
