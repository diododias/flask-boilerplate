import json
import inspect
from base64 import b64encode
from hashlib import md5
from flask_caching import Cache, function_namespace


class ResourceCache(Cache):
    def _memoize_make_cache_key(self,
                                make_name=None,
                                timeout=None,
                                forced_update=None,
                                hash_method=None,
                                source_check=None):
        def make_cache_key(f, *args, **kwargs):
            fname, _ = function_namespace(f)
            if callable(make_name):
                altfname = make_name(fname)
            else:
                altfname = fname

            updated = altfname + json.dumps(dict(
                args=self._extract_self_arg(f, args),
                kwargs=kwargs), sort_keys=True)

            return b64encode(
                md5(updated.encode('utf-8')).digest()
            )[:16].decode('utf-8')

        return make_cache_key

    @staticmethod
    def _extract_self_arg(f, args):
        argspec_args = inspect.getargspec(f).args
        if argspec_args and argspec_args[0] in ('self', 'cls'):
            return args[1:]
        return args


cache = ResourceCache(config={
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': 'redis://localhost:6379/0',
        'CACHE_DEFAULT_TIMEOUT': 300
    })

