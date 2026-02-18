from typing import Any, List, Optional, Union, Dict
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        pass

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None
                    ) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class StreamPocessor:
    def __init__(self):
        pass

    def run_unified_processing(self,
                               streams: List[DataStream],
                               mixed_data: Dict[str, List[Any]]):
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "No Data To Process."

        try:
            temp_values = []
            for item in data_batch:
                key, val = item.split(':')
                if key.strip() == "temp":
                    temp_values.append(float(val))

            if not temp_values:
                return "No temperature data found in batch."

            average = sum(temp_values) / len(temp_values)
            return (f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: {average}°C")

        except (ValueError, IndexError):
            return "Error: While Parsing The Data !"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "No Data To Process"

        try:
            count = len(data_batch)
            net_flow = 0
            for item in data_batch:
                key, value = item.split(':')
                if key.strip() == "buy":
                    net_flow -= int(value)
                elif key.strip() == "sell":
                    net_flow += int(value)
            return (f"Transaction analysis: {count} operations, "
                    f"net flow: +{abs(net_flow)} units")
        except (ValueError, IndexError):
            return "Error: While Parsing The Data !"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        pass
