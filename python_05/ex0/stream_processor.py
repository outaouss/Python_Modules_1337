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
            if isinstance(data, int):
                count = 1
                sum_num = data
            else:
                count = len(data)
                sum_num = sum(data)
            average = sum_num / count
            return self.format_output(f"Processed {count} numeric vlues, "
                                      f"sum={sum_num}, avg={average}")
        else:
            return "The Provided Data Cannot Be Processed"

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, int):
                return True
            for d in data:
                int(d)
            return True
        except (ValueError, TypeError):
            return False


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data):
            count = len(data)
            words = len(data.split())
            return self.format_output(f"Processed test: {count} "
                                      f"charachters, {words} words")
        else:
            return "The Provided Data Cannot Be Processed"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    # Numeric Process !
    print("Initializing Numeric Processor...")
    try:
        data = [1, 2, 3, 4, 5]
    except NameError:
        print("Error: NameError Raised !")
        exit()
    numbers = NumericProcessor()
    if numbers.validate(data):
        print("Processing data:", data)
        print("Validation: Numeric data verified")
    print(numbers.process(data), "\n")

    # Text Process !
    print("Initializing Text Processor...")
    try:
        data_str = "Hello Nexus World"
    except NameError:
        print("Error: NameError Raised !")
        exit()
    charachters = TextProcessor()
    if charachters.validate(data_str):
        print(f'Processing data: "{data_str}"')
        print("Validation: Text data verified")
    print(charachters.process(data_str), "\n")

    # Log Process !
    print("Initializing Log Processor...")
