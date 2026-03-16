#!/bir/usr/env python3

def main() -> None:
    print("=== Game Analytics Dashboard ===")
    print()

    info = {
        "alice": {"score": 2300, "status": True,
                  "achieve": ["first_kill", "level_10",
                              "treasure_hunter", "speed_demon",
                              "first_blood"]},
        "bob": {"score": 1800, "status": True,
                "achieve": ["first_kill", "level_10",
                            "boss_slayer", "collector", "first_blood"]},
        "charlie": {"score": 2150, "status": True,
                    "achieve": ["first_kill", "level_10", "boss_slayer",
                                "speed_demon"]},
        "diana": {"score": 2050, "status": False,
                  "achieve": ["boss_hunter", "first_kill",
                              "combo_king", "explorer"]},
    }

    print("=== List Comprehension Examples ===")
    scores = [info[name]["score"] for name in info]
    dub_scores = [score * 2 for score in scores]
    high_scores = [name for name in info if info[name]["score"] > 2000]
    active = [active for active in info if info[active]["status"]]
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {dub_scores}")
    print(f"Active players: {active}")
    print()

    print("=== Dict Comprehension Examples ===")
    p_score = {p: info[p]["score"] for p in info if info[p]["status"]}
    print(f"Player scores: {p_score}")
    score_cat = {
        "high": len([p for p in info if info[p]["score"] > 2100]),
        "meduim": len([[p for p in info if info[p]["score"] > 2000]]),
        "low": len([[p for p in info if info[p]["score"] > 2000]])
    }
    print(f"Score categories: {score_cat}")
    achievements_count = {p: len(info[p]["achieve"]) for p in info}
    print(f"Achievement counts: {achievements_count}")
    print()

    print("=== Set Comprehension Examples ===")
    players_set = {p for p in info}
    print(f"Unique players: {players_set}")
    achievements_set = {a for p in info for a in info[p]["achieve"]}
    print(f"Unique achievements: {achievements_set}")
    regions = [
            {"name": "alice", "region": "north"},
            {"name": "bob", "region": "east"},
            {"name": "charlie", "region": "east"},
            {"name": "diana", "region": "central"}
            ]
    active_regions = {reg["region"] for reg in regions}
    print(f"Active regions: {active_regions}")
    print()

    print("=== Combined Analysis ===")
    print(f"Total players: {len(info)}")
    print(f"Total unique achievements {len(achievements_set)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    top = max(info, key=lambda x: info[x]["score"])
    print(f"Top performer: {top} ({info[top]["score"]}", end="")
    print(f" points, {len(info[top]["achieve"])} achievements)")


if __name__ == "__main__":
    main()
