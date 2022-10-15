# -*- coding: utf-8 -*-
"""Handler for creating email addresses"""
import base64
import json


class EmailAddress:
    """This class represents an account"""

    def __init__(self, data):
        self.value = data["email"]


def subscribe(event, _):
    """Subscribes to an event trigger

    Args:
        event (_type_): Event data
        _ (_type_): _description_
    """
    data = base64.b64decode(event["data"]).decode()
    address = EmailAddress(json.loads(data))
    print(address.__dict__)
