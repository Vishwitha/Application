from flask import jsonify
from consumer import consumer_app
from consumer.consumer import kafkaMessageConsumer


@consumer_app.route('/message/count')
def get_message_count():
    """gets the message count from the message entries in db"""

    receiver = kafkaMessageConsumer()
    mess_count = receiver.get_message_count()
    return jsonify({'message count': mess_count})



