from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data):
            count = len(data)
            sum_num = sum(data)
            average = sum_num / count
            return self.format_output(f"Processed {count} numeric vlues, "
                                      f"sum={sum_num}, avg={average}")
        else:
            return "The Provided Data Cannot Be Processed"

    def validate(self, data: Any) -> bool:
        try:
            for d in data:
                int(d)
            return True
        except (ValueError, TypeError):
            return False


# class TextProcessor(DataProcessor):

#     def process(self, data: Any) -> str:
#         pass

#     def validate(self, data: Any) -> bool:
#         pass


# class LogProcessor(DataProcessor):

#     def process(self, data: Any) -> str:
#         pass

#     def validate(self, data: Any) -> bool:
#         pass


if __name__ == "__main__":
    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    numbers = NumericProcessor()
    if numbers.validate(data):
        print("Processing data:", data)
        print("Validation: Numeric data verified")
    print(numbers.process(data))
