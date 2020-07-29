import uuid

from consumer import consumer_app


class kafkaMessageConsumer:
    """kafkaMessageConsumer class to push the message

    received from producer to db and have the count
    """

    def push_to_db(self):
        # print(message)
        # # messages = consumer_app.config.consumer.poll(timeout_ms=100, max_records=None, update_offsets=True)
        # if message is not None and bool(message):
        for msg in consumer_app.config.consumer:
            print(msg)
            push_to_db_query = "INSERT INTO " + consumer_app.config["DB_TABLE"] + "(MESS_ID, TOPIC) VALUES ('" + \
                               str(uuid.UUID(bytes=msg.headers[0][1])) + "', '" + msg.topic + "')"
            consumer_app.config.cursor.execute(push_to_db_query)
            consumer_app.config.db_connection.commit()

            # consumer_app.config.cursor.execute("USE " + consumer_app.config["DB_NAME"] + "")
            # consumer_app.config.db_connection.commit()

    # def poll(self):
    #     # messages = consumer_app.config.consumer.poll(timeout_ms=100, max_records=None, update_offsets=True)
    #     messages = consumer_app.config.consumer
    #     for msg in messages:
    #         print(msg)
    #         self.push_to_db(msg)


    def get_message_count(self):
        consumer_app.config.cursor.execute("USE " + consumer_app.config["DB_NAME"] + "")
        count_query = "SELECT COUNT(*) FROM " + consumer_app.config["DB_TABLE"] + ""
        print(count_query)
        count = consumer_app.config.cursor.execute(count_query)
        result = consumer_app.config.cursor.fetchone()[0]
        print(result)
        return result
