#!/usr/bin/env python3
import sys


def main() -> None:
    print("===Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            scores = [int(score) for score in sys.argv[1:]]
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}\n")
        except ValueError:
            print("Error: All scores must be integers.")
            return


if __name__ == "__main__":
    main()
