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
        self.numeric_data = data
        return True
    
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "processing failed"
        return f"Processing data: {data}"

    def format_output(self, result: str) -> str:
        total = 0
        count = 0
        average = 0
        print(result, end="")
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

    def __init__(self) -> None:
        print("Initializing Text Processor...")
        self.txt_data = ""

    def validate(self, data: Any) -> bool:
        try:
            data += ""
        except TypeError:
            print("Invalid text data")
            return False
        self.txt_data = data
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "processing failed"
        return (f'Processing data: "{data}"')

    def format_output(self, result: str) -> str:
        words = 0
        chars = 0

        print(result, end="")
        for s in self.txt_data:
            chars += 1
            if s == " ":
                words += 1
        words += 1
        format = f"Processed text: {chars} characters, {words} words"
        return super().format_output(format)


class LogProcessor(DataProcessor):
    pass


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    n = NumericProcessor()
    n_data = [1, 2, 3, 4, 5]
    print(n.process(n_data))
    flag = n.validate(n_data)
    if flag:
        print("Validation: Numeric data verified")
    else:
        print("Validation: Numeric data verification failed")
    print(n.format_output("Output: "))
    t_data = "Hello Nexus World"
    print()
    t = TextProcessor()
    print(t.process(t_data))
    if t.validate(t_data):
        print("Validation: Text data verified")
    else:
        print("Validation: Text data verification failed")
    print(t.format_output("Output: "))
    print()
    


if __name__ == "__main__":
    main()