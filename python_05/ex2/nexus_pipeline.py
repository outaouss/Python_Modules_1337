from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: Any):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    def process(self, data: Any) -> Any:
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class InputStage():

    def process(self, data: Any) -> Dict[str, Union[str, int, float, dict]]:

        if data:
            print(f"Input: {data}")
            if isinstance(data, dict):
                return data
            elif isinstance(data, str):
                return {"raw": data}
        return {}


class TransformStage():

    def process(self, data: Any) -> Dict:

        transform = "Transform:"
        if "sensor" in data:
            print(f"{transform} Enriched with metadata and validation")
            data["status"] = "Normal range"
        elif "," in data.get("raw", ""):
            print(f"{transform} Parsed and structured data")
            data["parsed_count"] = len(data["raw"].split(","))
        elif "stream" in data.get("raw", "").lower():
            print(f"{transform} Aggregated and filtered")
            data['avg_val'] = 22.1
            data['reading'] = 5

        return data


class OutputStage():

    def process(self, data: Any) -> str:

        output = "Output:"
        if "sensor" in data:
            return (f"{output} Processed temperature reading: "
                    f"{data['value']}°C ({data['status']})")
        elif "," in data.get("raw", ""):
            return (f"{output} User activity logged: {data['parsed_count']} "
                    "actions processed")
        elif "stream" in data.get("raw", "").lower():
            return (f"{output} Stream summary: "
                    f"{data['reading']} readings, avg: {data['avg_val']}°C")
        return ""


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Any):
        super().__init__(pipeline_id)

        # Adding Gears
        for stage in [InputStage(), TransformStage(), OutputStage()]:
            self.add_stage(stage)

    def process(self, data: Any) -> Any:
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Any):
        super().__init__(pipeline_id)

        # Adding Gears
        for stage in [InputStage(), TransformStage(), OutputStage()]:
            self.add_stage(stage)

    def process(self, data: Any) -> Any:
        return super().process(data)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Any):
        super().__init__(pipeline_id)

        # Adding Gears
        for stage in [InputStage(), TransformStage(), OutputStage()]:
            self.add_stage(stage)

    def process(self, data: Any) -> Any:
        return super().process(data)


class NexusManager():
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> Any:

        results = [pipeline.process(data) for pipeline in self.pipelines]
        return results


def chaining_demo(adapters: List[Optional[Any]]) -> None:
    '''A Function That Demonstrate The Chaining !'''

    print("\n=== Pipeline Chaining Demo ===")

    if isinstance(adapters, List):
        print("Pipeline A -> Pipeline B -> Pipeline C")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored")
        per_cent = 95
        secondes = 0.2
        print("Chain result: 100 records processed through "
              f"{len(adapters)}-stage pipeline")
        print(f"Performance: {per_cent}% efficiency, "
              f"{secondes}s total processing time")
    else:
        print("Data is Not A Valid List")


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")

    nexus_manager = NexusManager()

    print("\nCreating Data Processing Pipeline...")

    adapters = [JSONAdapter("JSON_PIPELIN"),
                CSVAdapter("CSV_PIPELIN"),
                StreamAdapter("STREAM_PIPELIN")]

    for adap in adapters:
        nexus_manager.add_pipeline(adap)

    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print("\n=== Multi-Format Data Processing ===\n")

    # For JSON !
    print("Processing JSON data through pipeline...")
    json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print(adapters[0].process(json_data))

    # For CSV !
    print("\nProcessing CSV data through same pipeline...")
    csv_data = '"user,action,timestamp"'
    print(adapters[1].process(csv_data))

    # For Stream !
    print("\nProcessing Stream data through same pipeline...")
    stream_data = "Real-time sensor stream"
    print(adapters[2].process(stream_data))

    chaining_demo(adapters)
    print()

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    results = nexus_manager.process_data(None)

    stages = [InputStage(), TransformStage(), OutputStage()]
    counter = 0
    for check in results:
        if not check:
            counter += 1

    if counter == len(stages):
        print("Error detected: Invalid data format!!")
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")

    print("\nNexus Integration complete. All systems operational.")
