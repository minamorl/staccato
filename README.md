# staccato
Twitter api wrapper for python 3

## Installation

    pip install staccato

## Example

    import staccato

    api = staccato.startup()
    api.auth(consumer_key, consumer_secret, access_token_key, access_token_secret)

    api.statuses_update(status="Hello, world!")

