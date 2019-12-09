from file_cache import file_cache


@file_cache(type='json')
def test():
    return {'test':'case'}

print(test())

