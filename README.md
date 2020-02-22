[![Build Status](https://travis-ci.com/adrenalin/helpers.svg?branch=master)](https://travis-ci.com/adrenalin/helpers) [![Coverage Status](https://coveralls.io/repos/github/adrenalin/helpers/badge.svg)](https://coveralls.io/github/adrenalin/helpers)

## get_connection_string

Get connection string for the given arguments

Examples

```
get_connection_string(
  protocol='https',
  username='tester',
  password='passwd',
  host='example.net',
  port='443'
  name='test-resource'
)
>>> 'https://tester:passwd@example.net:443/test-resource'

get_connection_string(
  protocol='postgresql',
  username='postgres',
  host='localhost',
  name='test-db'
)
>>> 'postgresql://postgres@localhost/test-db'

```

## get_recursive_filelist

## get_relative_module_path

## get_value

Get value from a dictionary or return default if not defined

```
get_value(obj, path=None, default=None):
```

Examples

```
obj = {
  'foo': {
    'bar': 'value'
  }
}

get_value(obj, 'foo.bar') == 'value'
>>> 'value'

get_value(obj, 'foo.foo')
>>> None

get_value(obj, 'foo.foo', 'my_default_value')
>>> 'my_default_value'
```


## merge

Deep merge two or more dictionaries or lists

Examples

```
merged = merge(dict1, dict2, dict3)
```
