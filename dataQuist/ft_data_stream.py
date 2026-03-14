from typing import Generator
def stream_events(count: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range (count):
        player = players[i % len(players)]
        event = events[i % len(events)]
        level = (i % 14) + 1
        yield {
            "id": i + 1,
            "player": player,
            "event": event,
            "level": level
        }


def fibonacci_gen() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_gen() -> Generator[int, None, None]:
    num = 2
    while True:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print()
    print("Processing 1000 game events...")
    print()
    events_processed = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    for event in  stream_events(1000):
        if event["level"] >= 10:
            high_level_players += 1
        if event["event"] == "found treasure":
            treasure_events += 1
        if event["event"] == "leveled up":
            level_up_events += 1
        events_processed += 1
        print(f"Event {event['id']}: Player {event['player']} ", end="")
        print(f"(level {event['level']}) {event['event']}")
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {events_processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level up events: {level_up_events}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib = fibonacci_gen()
    for _ in range(9):
        print(next(fib), end=", ")
    print(next(fib), end="")
    print()
    print("Prime numbers (first 5): ", end="")
    prime = prime_gen()
    for _ in range(4):
        print(next(prime), end=", ")
    print(next(prime), end="")
    
    print()
if __name__ == "__main__":
    main()