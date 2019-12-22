# simple_file_cache
Python Simple cache based on pickle or json file





## Usage

```python
data = { "hi":"hello" }

# usage 1: as a file cache
@file_cache(file='export.json', type='json')
def do_job():
  return data

# usage 2: load file as fast as
rs = load_file(file='export.json', type='json')

# usage 3: dump file as fast as
rs = dump_file(file='export.json', type='json', data=data)
```

