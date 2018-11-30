import hashlib
import os


def get_ts(path):
    return [getattr(os.path, 'get'+m)(path) for m in ['ctime', 'mtime']]

def get_path(url, dirpath):
    dirpath = os.path.join(dirpath, hashlib.sha256(url.encode()).hexdigest())

    latest_ts = None
    latest_file = os.path.join(dirpath, 'latest')
    if os.path.exists(dirpath):
        for f in os.listdir(dirpath):
            if f.startswith('.'):
                continue
            path = os.path.join(dirpath, f)
            ts = sorted(get_ts(path))[-1]

            if latest_ts is None:
                latest_ts = ts
                latest_file = path
            else:
                if latest_ts < ts:
                    latest_ts = ts
                    latest_file = path
    return latest_file
