from json import loads

from aiokafka import AIOKafkaConsumer
from core.constants import kafka_topic

consumer = AIOKafkaConsumer(
    kafka_topic.create_project,
    bootstrap_servers="kafka:9092",
    group_id="app",
    value_deserializer=lambda message: loads(message.decode("utf-8")),
)


async def consume_messages(consumer: AIOKafkaConsumer):
    await consumer.start()
    async for message in consumer:
        print("СООБЩЕНИЕ:", message.value)
        await consumer.commit()
