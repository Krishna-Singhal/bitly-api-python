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
from BitlyAPI import shorten_urls

urls = ["https://github.com/Krishna-Singhal", "...", "..."]

response = shorten_url(urls)

# print all shotened urls
for i in response:
    print(i.long_url, i.short_url, i.status_txt)
```

#### <b>Parameters</b>

Parameter | description
--------- | -----------
`urls` | List of Long urls

<br>

## <b>Version</b>

```python
from BitlyAPI import __version__

print(__version__)
```

# <b>Copyright</b>

Copyright (C) 2022 by Krishna-Singhal, < https://github.com/Krishna-Singhal >.

All rights reserved.
