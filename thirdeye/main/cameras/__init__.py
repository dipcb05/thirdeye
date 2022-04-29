import os
import glob

from django.utils import importlib


BACKEND_PATTERN = '*.py'


def iter_backends():
    """Iterates over all camera backend modules."""
    # Get a directory listing of all the backends
    for path in glob.glob('%s/%s' % (os.path.dirname(__file__), BACKEND_PATTERN)):
        # Remove the leading directory name
        path = os.path.basename(path)
        # Skip __init__.py and it's ilk.
        if path.startswith('__'):
            continue
        # Remove the extension
        path = os.path.splitext(path)[0]
        yield importlib.import_module('%s.%s' % (__name__, path))


def iter_cameras(module):
    for name in dir(module):
        klass = getattr(module, name)
        if hasattr(klass, 'make') and hasattr(klass, 'model'):
            yield klass


def get_backend(camera):
    """Finds a camera backend that supports the given make/model."""
    # Asks each available backend if this make/model is supported.
    for module in iter_backends():
        for klass in iter_cameras(module):
            if ((getattr(klass, 'make', '').lower() == camera.make and
                 camera.model in getattr(klass, 'models', []))):
                return klass(camera)
    raise NotSupportedError(camera)


class NotSupportedError(Exception):
    """Raised when no backend supporting the given camera can be found."""
    def __init__(self, camera):
        super(NotSupportedError, self).__init__('No backend available for %s' % camera)
