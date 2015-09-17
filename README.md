# ![logo](./staccato.png) staccato
Twitter API wrapper for Python 3

[![Circle CI](https://circleci.com/gh/minamorl/staccato.svg?style=svg)](https://circleci.com/gh/minamorl/staccato)

## Installation

    pip install staccato

## Example

```python
import staccato

# oauth1 authentication.
api = staccato.startup()
api.auth(consumer_key, consumer_secret, access_token_key, access_token_secret)

# update status
response = api.statuses_update(status="Hello, world!")

# response object is simply JSON-parsed value.
print(response)

# And you can also do this...
api.statuses_destroy(response['id'])
```

PIN-based auth (>=0.0.6)

```python
api = staccato.startup()
api.auth(consumer_key, consumer_secret)

url = api.generate_auth_url()
print(url)
pin = raw_input()

print(api.pin_auth(pin))

response = api.statuses_update(status="Hello, world!")
print(response)
api.statuses_destroy(response['id'])
```

## TODO:

- utility function of POST media/upload (chunked) for user convinience.
