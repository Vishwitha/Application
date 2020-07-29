
from producer import producer_app
import uuid

class KafkaPublisher:

    """KafkaPublisher class to pushlish the message

    to kafka
    """

    def push_message(self, message):

        """
        push the message to kafka

        :param message
        """
        producer_app.config.producer.send(producer_app.config["TOPIC_NAME"], message, headers=[('key', uuid.uuid4().bytes)])
        # threading.Timer(5, self.push_message(message)).start()
        print("finished")