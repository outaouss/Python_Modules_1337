from typing import Any, List, Union, Protocol
from abc import ABC


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def process(self, data: Any) -> Any:
        pass

    def add_stage(self, stage: ProcessingStage):
        pass


class InputStage():
    def process(self, data: Any) -> Any:
        pass


class TransformStage():
    def process(self, data: Any) -> Any:
        pass


class OutputStage():
    def process(self, data: Any) -> str:
        pass


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
        pass

    def process_data(self, data: Any) -> Any:
        pass
