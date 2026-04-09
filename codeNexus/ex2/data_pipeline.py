#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any
from typing import Protocol


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
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:

        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in stream: "
                      f"{element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            total = len(proc.p_data)
            remaining = len(proc.p_data) - proc.index

            if isinstance(proc, NumericProcessor):
                print(f"Numeric Processor: total {total} items processed, "
                      f"remaining {remaining} on processor")
            elif isinstance(proc, TextProcessor):
                print(f"Text Processor: total {total} items processed, "
                      f"remaining {remaining} on processor")
            elif isinstance(proc, LogProcessor):
                print(f"Log Processor: total {total} items processed, "
                      f"remaining {remaining} on processor")
        
        def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
            for proc in self.processors:
                accumulated = []
                for _ in range(nb):
                    try:
                        accumulated.append(proc.output())
                    except IndexError:
                        break
                if accumulated:
                    plugin.process_output(accumulated)

class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts = []
        for rank, value in data:
            parts.append(f'"item_{rank}": "{value}"')
        print("JSON Output:")
        print("{" + ", ".join(parts) + "}")

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()
    print("\nRegistering processors...")
    ds.register_processor(NumericProcessor())
    
