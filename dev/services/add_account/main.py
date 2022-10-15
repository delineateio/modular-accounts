# -*- coding: utf-8 -*-
"""Implementation of an API service that raises an event"""

import uuid
import json
from datetime import date
import functions_framework
import flask
import bleach
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()


class Account:
    """This class represents an account"""

    def __init__(self, data):
        self.__dict__ = data
        self.unique_id = uuid.uuid4()
        self.code = data["code"].upper()
        self.short_name = data["short_name"]
        self.full_name = data["full_name"]
        self.email = add_email(self.short_name)
        self.opened = date.today()


@functions_framework.http
def main(request: flask.Request):
    """Entry point for the API to add the account

    Args:
        request (flask.request): The HTTP request object

    Returns:
        flask.response: The API response object
    """
    if request.method != "POST":
        return flask.Response(status=405)

    try:
        account = Account(request.get_json())
        body = json.dumps(account.__dict__, default=str)
        raise_add_account_event(account)
        return flask.Response(bleach.clean(body), mimetype='application/json', status=201)

    # pylint: disable=locally-disabled, broad-except
    except Exception:
        return flask.Response(status=500)


def add_email(name: str):
    """Adds an email address by making an http call

    Args:
        name (name): Name of the account to create the email address for

    Returns:
        str: The email address
    """
    name = name.lower()
    # pylint: disable=locally-disabled, fixme
    # TODO: lookup the domain name from a config file
    # TODO: Make an external API call to create the email address
    return f"{name}@delineate.io"


def raise_add_account_event(account: Account):
    """Raises an event indicating that the account has been created

    Args:
        account (account): The account to include on the event
    """
    topic_path = publisher.topic_path("delineateio", "test-topic")
    data_str = json.dumps(account.__dict__, default=str)
    data = data_str.encode("utf-8")
    publisher.publish(topic_path, data)
