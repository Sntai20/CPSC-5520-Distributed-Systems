"""
# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

FILE: messaging_service.py

DESCRIPTION:
    This program demonstrates common scenarios like instantiating a client,
    creating a queue, and sending and receiving messages.

USAGE:
    python3 messaging_service.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_STORAGE_CONNECTION_STRING - the connection string to your storage account
"""

import os
import uuid
import time
from azure.storage.queue import QueueServiceClient
from azure.storage.queue import QueueClient

class MessagingService(object):
    """Simple Messaging Service class used to send and receive messages to an Azure Queue."""

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    def create_client_with_connection_string(self):
        """Instantiate the QueueServiceClient from a connection string"""
        queue_service = QueueServiceClient.from_connection_string(conn_str=self.connection_string)

        # Clearing the Screen
        os.system('clear')

        queue_list = queue_service.list_queues(name_starts_with = "message")
        for queue in queue_list:
            print(f"Found queue named {queue.name} " +
                    f"Approximate Message Count {queue.approximate_message_count}\n\n")

    def sender_queue_and_messages(self):
        """
        Instantiate the QueueClient from a connection string
        and create the stock trade request, then send the messages
        to the queue.
        """
        queue_name = "messagequeue"
        create_number_of_messages = 3

        queue_client = QueueClient.from_connection_string(
                            conn_str=self.connection_string,
                            queue_name=queue_name)

        try:
            for message in list(range(create_number_of_messages)):
                # Generate a Stock Trade request message.
                message = str(uuid.uuid4())
                # Send messages
                queue_client.send_message(message)
                # Simulate processing the requests
                print(f"Sender: Requesting stock trade. {message}")
                time.sleep(2)

        finally:
            print("Sender: Messages sent\n\n")

    def receiver_queue_and_messages(self):
        """
        Instantiate the QueueClient from a connection string,
        then receive the stock trade request messages from the queue.
        """
        # Create a unique name for the queue
        queue_name = "messagequeue"

        # Simulate latency
        print("\n\nSimulate 3 seconds of latency.\n\n")
        time.sleep(3)

        # Instantiate the QueueClient from a connection string
        queue_client = QueueClient.from_connection_string(
                            conn_str=self.connection_string,
                            queue_name=queue_name)

        count = 0

        try:
            # Receive the messages
            messages = queue_client.receive_messages(messages_per_page=2)

            # Get the queue length
            properties = queue_client.get_queue_properties()
            count = properties.approximate_message_count

            # Print the content of the message, then dequeue.
            for message in messages:
                # Simulate processing the requests
                print(f"Receiver: Processing stock trade request. {message.content}")
                time.sleep(1)
                print(f"Receiver: Request completed. Dequeueing message: {message.content}")
                queue_client.delete_message(message.id, message.pop_receipt)

        finally:
            print("Receiver: Delete the queue.\n\n\n")
            print(f"Compleleted {count} stock trade request(s).")

if __name__ == '__main__':
    demo = MessagingService()
    demo.create_client_with_connection_string()
    demo.sender_queue_and_messages()
    demo.receiver_queue_and_messages()
