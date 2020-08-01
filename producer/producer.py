import threading
import time
import uuid

from producer import producer_app


class KafkaPublisher:

    """KafkaPublisher class to pushlish the message

    to kafka
    """

    def push_message(self, message):

        """
        push the message to kafka

        :param message
        """
        x = threading.Thread(target=self.send_message, args=(message,))
        x.start()

    def send_message(self, message):
        while True:
            producer_app.config.producer.send(producer_app.config["TOPIC_NAME"], message,
                                              headers=[('key', uuid.uuid4().bytes)])
            time.sleep(3)
            print("message sent")