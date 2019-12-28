from functools import wraps
from functools import partial
import json
import pickle
import logging

config = {
    'pickle': {
        'dump': pickle.dump,
        'load': pickle.load,
        'open_read_file': lambda filename: open(filename, 'rb'),
        'open_write_file': lambda filename: open(filename, 'wb'),
    },
    'json': {
        'dump': json.dump,
        'load': json.load,
        'open_read_file': lambda filename: open(filename, 'r'),
        'open_write_file': lambda filename: open(filename, 'w'),
    },
    'csv': {
        'dump':
        lambda x, fp: fp.writelines('\n'.join(
            [','.join(map(lambda x: str(x), r)) for r in x])),
        'load':
        lambda fp: [l.strip().split(',') for l in fp.readlines() if l.strip()],
        'open_read_file':
        lambda filename: open(filename, 'r'),
        'open_write_file':
        lambda filename: open(filename, 'w'),
    },
}


def file_cache(file='cache.dump', type='pickle', filefunc=None):
    conf = config[type]
    dump = conf.get('dump')
    load = conf.get('load')
    open_read_file = conf.get('open_read_file')
    open_write_file = conf.get('open_write_file')

    def wrapperfunc(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            # dynamic file name generate
            fname = file
            if filefunc:
                fname = filefunc(*args, **kwds)
            # try:
            #     with open_read_file(file) as fp:
            #         ret = load(fp)
            #     if ret:
            #         return ret
            # except Exception as e:
            #     logging.debug(e)
            #     pass
            ret = load_file(fname, type)
            if ret:
                return ret
            ret = f(*args, **kwds)
            dump_file(fname, type, ret)
            return ret

        return wrapper

    return wrapperfunc


def load_file(file='cache.dump', type='pickle'):
    conf = config[type]
    load = conf.get('load')
    open_read_file = conf.get('open_read_file')
    try:
        with open_read_file(file) as fp:
            ret = load(fp)
        if ret:
            return ret
    except Exception as e:
        logging.debug(e)
        pass


def dump_file(file='cache.dump', type='pickle', data=''):
    conf = config[type]
    dump = conf.get('dump')
    open_write_file = conf.get('open_write_file')
    try:
        with open_write_file(file) as fp:
            dump(data, fp)
        return True
    except Exception as e:
        logging.debug(e)
        pass
    return False
