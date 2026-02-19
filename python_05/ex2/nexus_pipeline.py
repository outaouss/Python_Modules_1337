from typing import Any, List, Union, Protocol, Dict
from abc import ABC


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id):
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
    def process(self, data: Any) -> Dict:
        print(f"Input: {data}")

        if data:
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
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        pass


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        pass


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        pass


class NexusManager():
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> Any:
        results = []
        for pipeline in self.pipelines:
            results.append(pipeline.process(data))
        return results
