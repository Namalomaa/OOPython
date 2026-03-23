#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any

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

    def __init__(self):
        print("Initializing Numeric Processor...")
        self.numeric_data = []

    def validate(self, data: Any) -> bool:
        try:
            data += 0
        except TypeError:
            try:
                for item in data:
                    item += 0
            except TypeError:
                print("Invalid numeric data")
                return False 
        self.numeric_data = [data]
        print("Validation: Numeric data verified")
        return True
    
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "processing failed"
        print(f"Processing data: {data}")
        return "processing complete"


    def format_output(self, result: str) -> str:
        total = 0
        count = 0
        average = 0
        if not self.validate(self.numeric_data):
            return "formatting failed"
        for i in self.numeric_data:
            total += i
            count += 1
        if count > 0:
            average = total / count
        base = f"Processed {count} numeric values, sum={total}, avg={average:.1f}"
        super().format_output(base)
        return base
    


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            data + ""
            print("Validation: Text data verified")
        except TypeError:
            print("Invalid text data")
            return False
        return True


class LogProcessor(DataProcessor):
    pass


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    n = NumericProcessor()
    n_data = [1, 2, 3, 4, 5]
    n.process(n_data)
    n.validate(n_data)
    n.format_output(n_data)

if __name__ == "__main__":
    main()