class Config(object):
    DEBUG = False
    DB_NAME = "messagedb"
    DB_HOST = "mysql"
    DB_USERNAME = "root"
    DB_PASSWORD = "Mess123"
    HOST_KAFKA ="kafka:9092"
    TOPIC_NAME = "Item1"
    NO_OF_PARTITIONS = 2
    GROUP_ID = "my_consumer"
    DB_TABLE = "message"

