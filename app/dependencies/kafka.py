from collections.abc import AsyncGenerator

from aiokafka import AIOKafkaProducer
from infrastructure.kafka.producer import producer


async def get_aiokafka_producer() -> AsyncGenerator[AIOKafkaProducer]:
    return producer
