# <b>BitlyAPI</b>

- [<b>Installation</b>](#installation)
- [<b>Documentation</b>](#documentation)
- [<b>Examples</b>](#examples)
  - [<b>Short Url</b>](#short-url)
  - [<b>Version</b>](#version)
- [<b>Copyright</b>](#copyright)

<br>

# <b>Installation</b>

```shell
pip install bitly-api-python
```

<br>

# <b>Documentation</b>

You can read our Documention on https://api.ksprojects.me/docs

<br>

# <b>Examples</b>

## <b>Short Url</b>

```python
from BitlyAPI import shorten_url

url = "https://github.com/Krishna-Singhal"

shortened_url = shorten_url(url)
print(shortened_url)
```

#### <b>Parameters</b>

Parameter | description
--------- | -----------
`url` | Long url

<br>

## <b>Version</b>

```python
from BitlyAPI import __version__

print(__version__)
```

# <b>Copyright</b>

Copyright (C) 2022 by Krishna-Singhal, < https://github.com/Krishna-Singhal >.

All rights reserved.
