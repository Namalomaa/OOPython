#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self):
        self.p_data = []
        self.index = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if self.index >= len(self.p_data):
            raise IndexError("no more data available")
        value = self.p_data[self.index]
        rank = self.index
        self.index += 1
        return (rank, value)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(value, (int, float)) for value in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for value in data:
                self.p_data.append(str(value))
        else:
            self.p_data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(value, str) for value in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for value in data:
                self.p_data.append(value)
        else:
            self.p_data.append(data)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        required_keys = {"log_level", "log_message"}
        if isinstance(data, dict):
            return (
                set(data.keys()) == required_keys
                and all(isinstance(data[k], str) for k in required_keys))

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and set(item.keys()) == required_keys
                and all(isinstance(item[k], str) for k in required_keys)
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                log = f"{item['log_level']}: {item['log_message']}"
                self.p_data.append(log)
        else:
            log = f"{data['log_level']}: {data['log_message']}"
            self.p_data.append(log)


class DataStream:

    def __init__(self):
        print("Initilize Data Stream...")
        self.items = 0
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        handeled = False
        for element in stream:
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    self.processed += 1
                    handeled = True
            if not handeled:    
                print("DataStream error - Can't process element in stream"
                      f" {element}")
                

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        for e in self.processors:
            if isinstance(e, NumericProcessor):
                print(f"Numeric Processor: total"
                      f" {len(self.processed) + len(self.remainder)}"
                      f"items proccesed, remaining "
                  f"{len(self.remainder)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    stream = DataStream()
    print("Registering Numeric Processor")
    n_proc = NumericProcessor()
    stream.register_processor(n_proc)
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()
    # print(f"Stream.proc {stream.processors}")


