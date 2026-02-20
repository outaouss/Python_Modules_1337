from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None
                    ) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch if
                criteria.lower() in str(item).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stream_type = "System Events"
        if "Sensor" in type(self).__name__:
            stream_type = "Environmental Data"
        elif "Transaction" in type(self).__name__:
            stream_type = "Financial Data"

        return {
            "id": self.stream_id,
            "type": stream_type
        }


class StreamProcessor:
    def __init__(self):
        pass

    def run_unified_processing(self,
                               streams: List[DataStream],
                               mixed_data: Dict[str, List[Any]]) -> None:
        print("Batch 1 Results:")

        for stream in streams:
            data = mixed_data.get(stream.stream_id)
            count = len(data)

            if "Sensor" in type(stream).__name__:
                label = "readings"
                name = "Sensor"
            elif "Transaction" in type(stream).__name__:
                label = "operations"
                name = "Transaction"
            elif "Event" in type(stream).__name__:
                label = "events"
                name = "Event"
            else:
                print("Not Found !")

            print(f"- {name} data: {count} {label} processed")


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
        if not data_batch:
            return "No Data To Process"

        try:
            count = len(data_batch)
            detect = 0
            for check in data_batch:
                if type(check) is not str:
                    return "Error: The Data is Not A Text"
                if "error" in check.lower():
                    detect += 1
            return f"Event analysis: {count} events, {detect} error detected"
        except Exception:
            return "Error: While Parsing The Data !"


def stream_system() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    mixed_data = {
        "SENSOR_001": ["temp:22.5", "humidity:65", "pressure:1013"],
        "TRANS_001": ["buy:100", "sell:150", "buy:75"],
        "EVENT_001": ["login", "error", "logout"]
    }

    # Sensor Stream
    print("Initializing Sensor Stream...")
    data_sensor = mixed_data['SENSOR_001']
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.get_stats()['id']}, "
          f"Type: {sensor.get_stats()['type']}")
    print("Processing sensor batch:", f"[{', '.join(data_sensor)}]")
    print(sensor.process_batch(data_sensor))

    # Transaction Stream
    print("\nInitializing Transaction Stream...")
    data_transaction = mixed_data['TRANS_001']
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.get_stats()['id']}, "
          f"Type: {transaction.get_stats()['type']}")
    print("Processing Transaction batch:", f"[{', '.join(data_transaction)}]")
    print(transaction.process_batch(data_transaction))

    # Event Stream
    print("\nInitializing Event Stream...")
    data_event = mixed_data['EVENT_001']
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.get_stats()['id']}, "
          f"Type: {event.get_stats()['type']}")
    print("Processing event batch:", f"[{', '.join(data_event)}]")
    print(event.process_batch(data_event))

    # Stream Processing
    stream_processor = StreamProcessor()
    streams = [sensor, transaction, event]
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    stream_processor.run_unified_processing(streams, mixed_data)

    # filtering
    print("\nStream filtering active: High-priority data only")
    sensor_alerts = ["temp:50:critical", "pressure:high", "temp:55:critical"]

    critical_alerts = sensor.filter_data(sensor_alerts, "critical")
    large = transaction.filter_data(data_transaction, "150")

    print(f"Filtered results: {len(critical_alerts)} "
          f"critical sensor alerts, {len(large)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    try:
        stream_system()
    except Exception:
        print("Error: While Executing The 'strem_system' Function")
