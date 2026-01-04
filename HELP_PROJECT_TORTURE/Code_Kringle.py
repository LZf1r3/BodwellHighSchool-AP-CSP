#!/usr/bin/env python3
"""
AP Computer Science Christmas Project
Naughty/Nice Analytics System (In-Memory Only)
"""

import random
from dataclasses import dataclass
from enum import Enum
from collections import Counter


# -----------------------------
# Enums & Constants
# -----------------------------

class Category(Enum):
    EVIL = (-999, "👹")
    NAUGHTY = (0, "😈")
    NICE = (20, "😇")
    ANGELIC = (40, "🌟")

    def __init__(self, threshold, emoji):
        self.threshold = threshold
        self.emoji = emoji


QUESTIONS = [
    ("Helped others", 5),
    ("Shared toys", 4),
    ("Did homework", 3),
    ("Lied", -6),
    ("Was respectful", 5),
]


GIFTS = {
    Category.ANGELIC: ["Drone", "Game Console", "Bike"],
    Category.NICE: ["Board Game", "Puzzle", "Soccer Ball"],
    Category.NAUGHTY: ["Socks", "Coal"],
    Category.EVIL: ["Krampus Visit"]
}


# -----------------------------
# Data Model
# -----------------------------

@dataclass
class Child:
    name: str
    gender: str
    score: int
    category: Category
    gift: str


# -----------------------------
# Core Engine
# -----------------------------

class SantaEngine:
    def __init__(self):
        self.children = []

    # -------------------------
    # Scoring
    # -------------------------

    def calculate_score(self, answers, name):
        score = 0

        # weighted behavior questions
        for i in range(len(QUESTIONS)):
            score += answers[i] * QUESTIONS[i][1]

        # name rule: double letters bonus
        lname = name.lower()
        for i in range(len(lname) - 1):
            if lname[i] == lname[i + 1]:
                score += 4
                break

        # RNG twist
        score += random.randint(-3, 3)
        return score

    def categorize(self, score):
        for cat in sorted(Category, key=lambda c: c.threshold, reverse=True):
            if score >= cat.threshold:
                return cat
        return Category.EVIL

    # -------------------------
    # Gift Assignment
    # -------------------------

    def assign_gift(self, category):
        return random.choice(GIFTS[category])

    # -------------------------
    # Assessment
    # -------------------------

    def assess_child(self, name, gender):
        answers = [random.randint(0, 1) for _ in QUESTIONS]
        score = self.calculate_score(answers, name)
        category = self.categorize(score)
        gift = self.assign_gift(category)

        child = Child(
            name=name,
            gender=gender,
            score=score,
            category=category,
            gift=gift
        )

        self.children.append(child)
        return child

    # -------------------------
    # Reporting
    # -------------------------

    def list_children(self):
        print("\n=== CHILD LIST ===")
        for c in self.children:
            print(
                f"{c.name:<12} {c.category.emoji} "
                f"{c.category.name:<8} "
                f"Score: {c.score:>3} "
                f"Gift: {c.gift}"
            )

    def print_summary(self):
        if not self.children:
            print("No data to summarize.")
            return

        total = len(self.children)
        counts = Counter(c.category for c in self.children)

        print("\n=== SUMMARY REPORT ===")
        print("Total children:", total)

        for cat in Category:
            count = counts.get(cat, 0)
            percent = (count / total) * 100
            print(f"{cat.emoji} {cat.name:<10}: {count:2} ({percent:5.1f}%)")

        most_common = Counter(c.gift for c in self.children).most_common(1)[0][0]
        print("Most common gift:", most_common)


# -----------------------------
# Main Program
# -----------------------------

def main():
    random.seed()

    engine = SantaEngine()

    print("\n🎄 SANTA'S NAUGHTY/NICE SYSTEM 🎅")

    while True:
        print("\n1. Assess a child")
        print("2. View all children")
        print("3. View summary")
        print("4. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Child name: ").strip()
            gender = input("Gender (M/F/X): ").strip().upper()

            child = engine.assess_child(name, gender)
            print("\nResult:")
            print("Name:", child.name)
            print("Score:", child.score)
            print("Category:", child.category.name)
            print("Gift:", child.gift)

        elif choice == "2":
            engine.list_children()

        elif choice == "3":
            engine.print_summary()

        elif choice == "4":
            print("🎅 Merry Christmas! 🎄")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
