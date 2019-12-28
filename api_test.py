from file_cache import file_cache, load_file


@file_cache(type='csv',filefunc=lambda dt: 'my_file_{}.csv'.format(dt))
def test(dt='2019-12-13'):
    print('do csv')
    return [[1]]



print(test(dt='2019-2323'))
rs= load_file(type='csv')
print(rs)
