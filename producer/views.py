from flask import jsonify, request

from producer import producer_app
from producer.producer import KafkaPublisher


@producer_app.route('/message/push', methods=['POST'])
def create_message():
    """ To create a message and push to Kafka"""
    print("received message")
    request_data = request.get_json()
    producer_obj = KafkaPublisher()
    producer_obj.push_message(request_data["message"])
    return jsonify({'message':'SUCCESS'})