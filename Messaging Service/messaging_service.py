# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: messaging_service.py

DESCRIPTION:
    These samples demonstrate common scenarios like instantiating a client,
    creating a queue, and sending and receiving messages.

USAGE:
    python3 messaging_service.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_STORAGE_CONNECTION_STRING - the connection string to your storage account
"""

import os, uuid, time

class MessagingService(object):

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    def create_client_with_connection_string(self):
        # Instantiate the QueueServiceClient from a connection string
        from azure.storage.queue import QueueServiceClient
        queue_service = QueueServiceClient.from_connection_string(conn_str=self.connection_string)

        # Get queue service properties
        properties = queue_service.get_service_properties()

    def queue_and_messages_example(self):
        # Create a unique name for the queue
        #queue_name = "messagequeue-" + str(uuid.uuid4())
        queue_name = "messagequeue"

        # Instantiate the QueueClient from a connection string
        from azure.storage.queue import QueueClient
        queue_client = QueueClient.from_connection_string(conn_str=self.connection_string, queue_name=queue_name)

        # Create the queue
        queue_client.create_queue()

        try:
            # Send messages
            queue_client.send_message("I'm using queues!")
            queue_client.send_message("This is my second message")

            # Receive the messages
            response = queue_client.receive_messages(messages_per_page=2)

            # Print the content of the messages
            for message in response:
                print(message.content)

        finally:
            # [START delete_queue]
            #queue_client.delete_queue()
            print("Delete the queue.")
    
    def sender_queue_and_messages(self):
        # Create a unique name for the queue
        queue_name = "messagequeue"
        create_number_of_messages = 3

        # Instantiate the QueueClient from a connection string
        from azure.storage.queue import QueueClient
        queue_client = QueueClient.from_connection_string(conn_str=self.connection_string, queue_name=queue_name)

        # Create the queue
        #queue_client.create_queue()
        # Clearing the Screen
        os.system('clear')

        try:
            for message in list(range(create_number_of_messages)):
                message = str(uuid.uuid4())
                # Send messages
                queue_client.send_message(message)
                # Simulate processing the requests
                print(f"Sender: Requesting stock trade. {message}")
                time.sleep(2)
            
        finally:
            # [START delete_queue]
            #queue_client.delete_queue()
            print(f"Sender: Messages sent\n\n")

    def receiver_queue_and_messages(self):
        # Create a unique name for the queue
        queue_name = "messagequeue"

        # Simulate latency
        print(f"\n\nSimulate latency of 3 seconds.\n\n")
        time.sleep(3)

        # Instantiate the QueueClient from a connection string
        from azure.storage.queue import QueueClient
        queue_client = QueueClient.from_connection_string(conn_str=self.connection_string, queue_name=queue_name)

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
                print("Receiver: Stock trade request complete. Dequeueing message: " + message.content)
                queue_client.delete_message(message.id, message.pop_receipt)

        finally:
            # [START delete_queue]
            #queue_client.delete_queue()
            print("Receiver: Delete the queue.\n\n\n")
            print(f"Compleleted {count} stock trade request(s).")
            

if __name__ == '__main__':
    sample = MessagingService()
    sample.create_client_with_connection_string()
    #sample.queue_and_messages_example()
    sample.sender_queue_and_messages()
    sample.receiver_queue_and_messages()