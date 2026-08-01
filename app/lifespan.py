import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from infrastructure.kafka.consumer import consume_messages, consumer
from infrastructure.kafka.producer import producer


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:  # noqa: ARG001
    """
    Действия до старта приложения.
    """
    await producer.start()

    asyncio.create_task(consume_messages(consumer))
    yield
    """
    Действия при завершении работы приложения.
    """
