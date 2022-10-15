# -*- coding: utf-8 -*-
"""This module sets up the testing topics and subscriptions"""
from google.cloud import pubsub_v1


def list_topics(project_id: str) -> None:
    """Lists the current topics

    Args:
        project_id (str): Project to list the topics for
    """
    publisher = pubsub_v1.PublisherClient()
    project_path = f"projects/{project_id}"

    for topic in publisher.list_topics(request={"project": project_path}):
        print(topic)


def create_topic(project_id: str, topic_id: str) -> None:
    """Create a topic in the project

    Args:
        project_id (str): Project identifier
        topic_id (str): The unique id of the topic
    """
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    topic = publisher.create_topic(request={"name": topic_path})
    print(f"Created topic: {topic.name}")


def create_push_subscription(
    project_id: str, topic_id: str, subscription_id: str, endpoint: str
) -> None:
    """Creates a push subscription in the project

    Args:
        project_id (str): Project identifier
        topic_id (str): The unique id of the topic
        subscription_id (str): The unique id of the subscription
        endpoint (str): The url of the endpoint to call
    """

    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(
        project_id, subscription_id)

    push_config = pubsub_v1.types.pubsub_gapic_types.PushConfig(
        push_endpoint=endpoint)

    with subscriber:
        subscription = subscriber.create_subscription(
            request={
                "name": subscription_path,
                "topic": topic_path,
                "push_config": push_config,
            }
        )

    print(f"Push subscription created: {subscription}.")
    print(f"Endpoint for subscription is: {endpoint}")


if __name__ == '__main__':
    create_topic("delineateio", "test-topic")
    create_push_subscription("delineateio", "test-topic",
                             "test-sub", "http://localhost:8081")
    list_topics("delineateio")
