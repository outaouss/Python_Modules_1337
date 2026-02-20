from typing import Any, List, Dict, Union, Optional
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

    def process(self, data: Union[int, List[int]]) -> str:

        if self.validate(data):

            if isinstance(data, int):
                count = 1
                sum_num = data

            else:
                count = len(data)
                sum_num = sum(data)
            average = sum_num / count

            return self.format_output(f"Processed {count} numeric values, "
                                      f"sum={sum_num}, avg={average}")

        else:
            return "The Provided Data is Not Numeric"

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
            return self.format_output(f"Processed text: {count} "
                                      f"characters, {words} words")

        else:
            return "The Provided Data is Not A Text"

    def validate(self, data: Any) -> bool:

        if isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:

        if self.validate(data):
            splited_data = data.split(':')

            try:

                first = splited_data[0]
                seconde = splited_data[1]
                return self.format_output(f"{first.upper()} "
                                          f"level detected: {seconde.strip()}")

            except IndexError:
                print("Error: IndexError Raised !")
        else:
            return "The Provided Data Cannot be A Log Text"

    def validate(self, data: Any) -> bool:

        if isinstance(data, str):
            splited_log = data.split()
            short = splited_log[0]

            if "error:" in short.lower() or "info:" in short.lower() or \
               "warning" in short.lower():
                if splited_log[1] == "":
                    return False

                return True

        return False

    def format_output(self, result: str) -> str:

        if "error" in result.lower():
            return f"Output: [ALERT] {result}"

        elif "info" in result.lower():
            return f"Output: [INFO] {result}"

        elif "warning" in result.lower():
            return f"Output: [WARNING] {result}"

        return super().format_output(result)


def main_test() -> Optional[str] | Dict:

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Numeric Process !

    print("Initializing Numeric Processor...")

    data_num = [1, 2, 3, 4, 5]
    numbers = NumericProcessor()

    if numbers.validate(data_num):
        print("Processing data:", data_num)
        print("Validation: Numeric data verified")

    print(numbers.process(data_num), "\n")

    # Text Process !

    print("Initializing Text Processor...")

    data_str = "Hello Nexus World"
    characters = TextProcessor()

    if characters.validate(data_str):
        print(f'Processing data: "{data_str}"')
        print("Validation: Text data verified")
    print(characters.process(data_str), "\n")

    # Log Process !

    print("Initializing Log Processor...")

    data_log = "ERROR: Connection timeout"
    log = LogProcessor()

    if log.validate(data_log):
        print(f'Processing data: "{data_log}"')
        print("Validation: Log entry verified")

    print(log.process(data_log), "\n")

    print("=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    # Demonstrate All

    num_format = NumericProcessor()
    print(num_format.process([2, 2, 2]))

    text_format = TextProcessor()
    print(text_format.process("Oussama 1337"))

    log_format = LogProcessor()
    print(log_format.process("INFO: System ready"))

    print("\nFoundation systems online. Nexus ready for advanced streams.")

    val = 15

    if val == 16:
        return "Val Returned Correct"
    elif val == 33:
        return {}
    else:
        return None


if __name__ == "__main__":
    main_test()
