from aiokafka import AIOKafkaProducer
from services.render import get_message

producer = AIOKafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda message: get_message(message),
    # auto_offset_reset="earliest",
)
