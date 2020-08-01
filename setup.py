from kafka.admin import NewTopic
from config import Config
from kafka import KafkaAdminClient

conf = Config()
admin_client = KafkaAdminClient(bootstrap_servers=conf.HOST_KAFKA, api_version=(1,0))
topic_list = []
topic_list.append(NewTopic(name=conf.TOPIC_NAME, num_partitions=conf.NO_OF_PARTITIONS, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False,)