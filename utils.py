import os
import uuid


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4().hex, ext)
    return os.path.join(instance.__class__.__name__.lower(), filename)
