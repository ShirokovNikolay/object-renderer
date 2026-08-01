import json

from aiokafka import AIOKafkaProducer
from core.constants import kafka_topic
from core.interfaces.services import AbstractRenderService
from pydantic import BaseModel
from schemas.render import RenderCreate


def get_message[T: BaseModel](message_data: T) -> bytes:
    message_dict = message_data.model_dump()
    serialized_value = json.dumps(message_dict)
    encoded_serialized_value = serialized_value.encode()
    return encoded_serialized_value


class RenderService(AbstractRenderService):
    def __init__(self, producer: AIOKafkaProducer) -> None:
        self.producer = producer

    async def send_event_render_model(self, create_render_data: RenderCreate) -> None:
        await self.producer.send(
            topic=kafka_topic.create_project,
            value=create_render_data,
        )
