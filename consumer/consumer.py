import uuid

from consumer import consumer_app


class KafkaMessageConsumer:
    """kafkaMessageConsumer class to push the message

    received from producer to db and have the count
    """

    def listener(self):
        print("entered listen")
        consumer_app.config.consumer.subscribe(topics=[consumer_app.config["TOPIC_NAME"]])
        for msg in consumer_app.config.consumer:
            print(msg)
            push_to_db_query = "INSERT IGNORE INTO " + consumer_app.config["DB_TABLE"] + "(MESS_ID, TOPIC) VALUES ('" + \
                               str(uuid.UUID(bytes=msg.headers[0][1])) + "', '" + msg.topic + "')"
            consumer_app.config.cursor.execute(push_to_db_query)
            consumer_app.config.db_connection.commit()


    def get_message_count(self):
        consumer_app.config.cursor.execute("USE " + consumer_app.config["DB_NAME"] + "")
        count_query = "SELECT COUNT(*) FROM " + consumer_app.config["DB_TABLE"] + ""
        print(count_query)
        count = consumer_app.config.cursor.execute(count_query)
        result = consumer_app.config.cursor.fetchone()[0]
        return result
