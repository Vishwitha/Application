import threading

import mysql.connector
from flask import Flask
from kafka import KafkaConsumer
from config import Config

consumer_app = Flask(__name__)
from consumer.consumer import KafkaMessageConsumer
from consumer import views

conf = Config()
consumer_app.config.from_object(conf)

# intializing db
consumer_app.config.db_connection = mysql.connector.connect(user=consumer_app.config["DB_USERNAME"],
                                                            host=consumer_app.config["DB_HOST"],
                                                            password=consumer_app.config["DB_PASSWORD"])
consumer_app.config.cursor = consumer_app.config.db_connection.cursor()
consumer_app.config.cursor.execute("CREATE DATABASE IF NOT EXISTS " + consumer_app.config["DB_NAME"])

consumer_app.config.cursor.execute("USE " + consumer_app.config["DB_NAME"] + "")
consumer_app.config.cursor.execute("CREATE TABLE IF NOT EXISTS "+ consumer_app.config["DB_TABLE"]+" (MESS_ID varchar(36) NOT NULL PRIMARY KEY, "
                                   "TOPIC varchar(36) NOT NULL)")
consumer_app.config.consumer = KafkaConsumer(consumer_app.config["TOPIC_NAME"],
                                             bootstrap_servers=consumer_app.config["HOST_KAFKA"],
                                             group_id=consumer_app.config["GROUP_ID"],
                                             auto_offset_reset='earliest')

consumer = KafkaMessageConsumer()
x = threading.Thread(target=consumer.listener)
x.start()
