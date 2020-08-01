import json

from flask import Flask
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

from config import Config

producer_app = Flask(__name__)

conf = Config()
producer_app.config.from_object(conf)
# producer_app.config.admin_client = KafkaAdminClient(bootstrap_servers="127.0.0.1:9092")
# admin_client = KafkaAdminClient(bootstrap_servers="127.0.0.1:9092", api_version=(1,0))
# topic_list = []
# # topic_list.append(NewTopic(name=producer_app.config["TOPIC_NAME"], num_partitions=producer_app.config["NO_OF_PARTITIONS"], replication_factor=1))
# producer_app.config.admin_client.create_topics(new_topics=topic_list, validate_only=False,)
producer_app.config.producer = KafkaProducer(bootstrap_servers="127.0.0.1:9092",
                                              value_serializer=lambda v: json.dumps(v).encode('utf-8'))
from producer import views
