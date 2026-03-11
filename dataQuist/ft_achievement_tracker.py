#!/usr/bin/env python3

def main():
    print("=== Achievement Tracker System ===\n")
    alice = {"first_kill", "level_10", "treasure_hunter",
             "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}

    charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon",
               "perfectionist"}

    players = [
        alice,
        bob,
        charlie
    ]

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()

    print("=== Acheivements Analytics ===")
    unique_achievements = set()
    unique_achievements = unique_achievements.union(*players)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print()
    common_achievements = set.intersection(*players)
    print(f"Common to all players: {common_achievements}")
    rare_achievements = set()
    achievement_counts = {}

    for player in players:
        for achievement in player:
            if achievement in achievement_counts:
                achievement_counts[achievement] += 1
            else:
                achievement_counts[achievement] = 1

    for achievement in achievement_counts:
        if achievement_counts[achievement] == 1:
            rare_achievements = rare_achievements.union({achievement})

    print(f"Rare achievements (1 player): {rare_achievements}")
    print()
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
