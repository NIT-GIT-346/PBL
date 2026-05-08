import asyncio
import logging
import random
from datetime import datetime
from typing import Dict, List

logger = logging.getLogger(__name__)


class KafkaSimulator:
    """Simulates Apache Kafka streaming for clinical data pipeline."""

    def __init__(self):
        self.topics = {
            "patient-vitals": [],
            "lab-results": [],
            "diagnosis-events": [],
            "alert-notifications": [],
        }
        self.is_running = False
        self.message_count = 0

    async def start(self):
        self.is_running = True
        logger.info("Kafka simulator started. Streaming clinical data...")

    async def stop(self):
        self.is_running = False
        logger.info("Kafka simulator stopped.")

    async def produce_message(self, topic: str, message: Dict):
        if topic not in self.topics:
            self.topics[topic] = []
        self.topics[topic].append(
            {
                "offset": self.message_count,
                "timestamp": datetime.utcnow().isoformat(),
                "data": message,
            }
        )
        self.message_count += 1
        logger.debug(f"Produced message to {topic}: offset={self.message_count - 1}")

    async def consume_messages(self, topic: str, limit: int = 10) -> List[Dict]:
        messages = self.topics.get(topic, [])
        return messages[-limit:]

    def get_stats(self) -> Dict:
        return {
            "is_running": self.is_running,
            "total_messages": self.message_count,
            "topics": {k: len(v) for k, v in self.topics.items()},
        }


kafka_service = KafkaSimulator()
