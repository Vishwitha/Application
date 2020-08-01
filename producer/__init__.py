import json

from flask import Flask
from kafka import KafkaProducer

from config import Config

producer_app = Flask(__name__)

conf = Config()
producer_app.config.from_object(conf)
producer_app.config.producer = KafkaProducer(bootstrap_servers=producer_app.config["HOST_KAFKA"],
                                             value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                             api_version=(1, 10))
from producer import views
