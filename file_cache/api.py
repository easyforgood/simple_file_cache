from functools import wraps
from functools import partial
import json
import pickle
config = {
        'pickle':{
            'dump': pickle.dump,
            'load': pickle.load,
            'open_read_file': lambda filename: open(filename,'rb' ),
            'open_write_file': lambda filename: open(filename,'wb' ),
            },
        'json':{
            'dump': json.dump,
            'load': json.load,
            'open_read_file': lambda filename: open(filename,'r' ),
            'open_write_file': lambda filename: open(filename,'w' ),
            },
}

def file_cache(file='cache.dump',type='pickle'):
    conf = config[type]
    dump = conf.get('dump')
    load = conf.get('load')
    open_read_file = conf.get('open_read_file')
    open_write_file = conf.get('open_write_file')
    def wrapperfunc(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            try:
                with open_read_file(file) as fp:
                    ret = load(fp)
                if ret:
                    return ret
            except:
                pass
            ret = f(*args, **kwds)
            with open_write_file(file) as fp:
                dump(ret,fp)
            return ret
        return wrapper
    return wrapperfunc
