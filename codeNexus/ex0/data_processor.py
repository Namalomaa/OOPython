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


def main():
    n = NumericProcessor()
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")

    print("Trying to validate input '42': ", n.validate(42))
    print("Trying to validate input 'Hello': ", n.validate("Hello"))
    n_data = [1, 2, 3, 4, 5]
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        n.ingest("foo")
    except ValueError as e:
        print("Got exception:", e)
    print("Processing data:", n_data)
    try:
        n.ingest(n_data)
    except ValueError as e:
        print("Got exception:", e)

    print("Extracting 3 values...")
    for _ in range(3):
        try:
            rank, value = n.output()
            print(f"Numeric value {rank}: {value}")
        except IndexError as e:
            print("Got exception:", e)

    print("\nTesting Text Processor...")
    t = TextProcessor()
    t_data = ["Hello", "Nexus", "World"]
    print("Trying to validate input '42':", t.validate(42))
    print("processing data:", t_data)
    try:
        t.ingest(t_data)
    except ValueError as e:
        print("Got exception:", e)
    print("Extracting 1 value...")
    rank, value = t.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    lo = LogProcessor()
    l_data = [{"log_level": "NOTICE", "log_message": "Connection to server"},
              {"log_level": "ERROR", "log_message": "Unauthorized access!!"}]
    print("Trying to validate input 'Hello':", lo.validate("Hello"))
    print("Processing data:", l_data)
    try:
        lo.ingest(l_data)
    except ValueError as e:
        print("Got exception:", e)
    print("Extracting 2 values...")
    for _ in range(2):
        try:
            rank, value = lo.output()
            print(f"Log entry {rank}: {value}")
        except IndexError as e:
            print("Got exception:", e)


if __name__ == "__main__":
    main()
