# ![logo](./staccato.png) staccato
Twitter API wrapper for Python 3

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

