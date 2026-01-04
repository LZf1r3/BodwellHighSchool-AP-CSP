#!/usr/bin/env python3
"""
Naughty/Nice List - Christmas Gift Assignment Program
Simple version without fancy libraries.
"""

import random
import statistics
from datetime import datetime
import os


# Categories with thresholds and emojis
CATEGORIES = {
    "godly": {"threshold": 80, "emoji": "🌟"},
    "nice": {"threshold": 40, "emoji": "😇"},
    "neutral": {"threshold": -20, "emoji": "😐"},
    "naughty": {"threshold": -60, "emoji": "😈"},
    "diabolical": {"threshold": float('-inf'), "emoji": "👹"}
}

# Gift categories and their assigned items with values
GIFTS = {
    "godly": [
        {"name": "Golden Halo", "value": 10000},
        {"name": "Unicorn", "value": 9500},
        {"name": "Private Island", "value": 15000},
        {"name": "Lifetime Cookie Supply", "value": 8000}
    ],
    "nice": [
        {"name": "Bike", "value": 500},
        {"name": "Video Game Console", "value": 600},
        {"name": "Books Collection", "value": 200},
        {"name": "Art Supplies Set", "value": 150},
        {"name": "Soccer Ball + Equipment", "value": 100}
    ],
    "neutral": [
        {"name": "Socks (3 pairs)", "value": 20},
        {"name": "Pencils Set", "value": 10},
        {"name": "Notebook", "value": 15},
        {"name": "Sweater", "value": 50}
    ],
    "naughty": [
        {"name": "Coal (Premium Grade)", "value": -10},
        {"name": "Stick", "value": -5},
        {"name": "Lump of Coal", "value": -10},
        {"name": "Nothing", "value": 0}
    ],
    "diabolical": [
        {"name": "Krampus Visit", "value": -1000},
        {"name": "Eternal Timeout", "value": -500},
        {"name": "Coal Mine Tour", "value": -300},
        {"name": "Bad Dreams Package", "value": -800}
    ]
}

# Questions with point values and categories
QUESTIONS = [
    ("Did you help your parents with chores without being asked?", 10, "responsibility"),
    ("Did you share your toys with siblings or friends?", 8, "kindness"),
    ("Did you say 'please' and 'thank you' regularly?", 5, "respect"),
    ("Did you do your homework on time?", 7, "responsibility"),
    ("Did you lie to your parents?", -10, "honesty"),
    ("Did you hit or push someone?", -15, "respect"),
    ("Did you break something on purpose?", -12, "respect"),
    ("Did you steal candy or toys?", -20, "honesty"),
    ("Did you help someone who was hurt or sad?", 12, "kindness"),
    ("Did you clean your room without complaining?", 6, "responsibility"),
    ("Did you throw a tantrum in public?", -8, "respect"),
    ("Did you say mean things to others?", -10, "kindness"),
    ("Did you volunteer or donate to charity?", 15, "kindness"),
    ("Did you take care of a pet responsibly?", 8, "responsibility"),
    ("Did you cheat on a test or game?", -12, "honesty"),
    ("Did you apologize when you did something wrong?", 10, "honesty"),
    ("Did you ignore your parents when they called you?", -7, "respect"),
    ("Did you stand up for someone being bullied?", 15, "courage"),
    ("Did you waste food on purpose?", -8, "respect"),
    ("Did you read books for fun?", 5, "responsibility"),
    ("Did you help with household tasks voluntarily?", 9, "responsibility"),
    ("Did you comfort a crying friend?", 11, "kindness"),
    ("Did you destroy someone else's property?", -18, "respect"),
    ("Did you tell the truth even when it was hard?", 12, "honesty"),
    ("Did you defend someone who couldn't defend themselves?", 14, "courage")
]

CATEGORY_NAMES = ["kindness", "responsibility", "honesty", "respect", "courage"]


class Assessment:
    """Individual child assessment record."""
    
    def __init__(self, name, score, category, gift, timestamp, category_scores, answers):
        self.name = name
        self.score = score
        self.category = category
        self.gift = gift
        self.timestamp = timestamp
        self.category_scores = category_scores
        self.answers = answers
    
    def to_dict(self):
        """Convert to dictionary for serialization."""
        return {
            "name": self.name,
            "score": self.score,
            "category": self.category,
            "gift": self.gift,
            "timestamp": self.timestamp,
            "category_scores": self.category_scores,
            "answers": self.answers
        }


class SantaEngine:
    """Naughty/Nice Analytics Engine."""
    
    def __init__(self, data_file="santa_data.txt"):
        self.data_file = data_file
        self.assessments = []
        self.load_data()
    
    def ask_questions(self, num_questions=10):
        """Ask random questions and calculate total score with category breakdown."""
        selected_questions = random.sample(QUESTIONS, min(num_questions, len(QUESTIONS)))
        total_score = 0
        category_scores = {cat: 0 for cat in CATEGORY_NAMES}
        answers = []
        
        print("\n" + "="*70)
        print("🎅 SANTA'S BEHAVIORAL ASSESSMENT 🎄")
        print("="*70)
        print("Answer YES (y) or NO (n) to each question.")
        print("Type 'skip' to skip a question (0 points).\n")
        
        for i, (question, points, q_category) in enumerate(selected_questions, 1):
            while True:
                answer = input(f"{i}. {question}\n   Your answer (y/n/skip): ").lower().strip()
                if answer in ['y', 'yes']:
                    total_score += points
                    category_scores[q_category] += points
                    answers.append({
                        "question": question,
                        "answer": "yes",
                        "points": points,
                        "category": q_category
                    })
                    break
                elif answer in ['n', 'no']:
                    answers.append({
                        "question": question,
                        "answer": "no",
                        "points": 0,
                        "category": q_category
                    })
                    break
                elif answer == 'skip':
                    answers.append({
                        "question": question,
                        "answer": "skip",
                        "points": 0,
                        "category": q_category
                    })
                    print("   ⏭️  Skipped")
                    break
                else:
                    print("   Please answer 'y', 'n', or 'skip'")
        
        return total_score, category_scores, answers

    def categorize_score(self, score):
        """Categorize a score using thresholds."""
        for cat_name in ["godly", "nice", "neutral", "naughty", "diabolical"]:
            if score >= CATEGORIES[cat_name]["threshold"]:
                return cat_name
        return "diabolical"

    def assign_gift(self, category):
        """Assign a random gift based on category."""
        return random.choice(GIFTS[category])

    def analyze_results(self):
        """Analytics with statistics."""
        if not self.assessments:
            print("\n❌ No data to analyze yet!")
            return
        
        total = len(self.assessments)
        scores = [a.score for a in self.assessments]
        
        # Category distribution
        category_counts = {}
        for a in self.assessments:
            category_counts[a.category] = category_counts.get(a.category, 0) + 1
        
        # Category scores aggregation
        category_performance = {cat: [] for cat in CATEGORY_NAMES}
        for assessment in self.assessments:
            for cat, score in assessment.category_scores.items():
                category_performance[cat].append(score)
        
        # Display analytics
        print("\n" + "="*70)
        print("📊 NAUGHTY/NICE ANALYTICS REPORT 📊")
        print("="*70)
        print(f"Total Children Assessed: {total}")
        print(f"Assessment Period: {self.assessments[0].timestamp} to {self.assessments[-1].timestamp}")
        print()
        
        # Category Distribution
        print("🎁 Category Distribution:")
        print("-" * 70)
        for cat_name in ["godly", "nice", "neutral", "naughty", "diabolical"]:
            count = category_counts.get(cat_name, 0)
            percentage = (count / total) * 100 if total > 0 else 0
            bar = "█" * int(percentage / 2)
            emoji = CATEGORIES[cat_name]["emoji"]
            print(f"{emoji} {cat_name.upper():12} | {count:3} ({percentage:5.1f}%) {bar}")
        
        print("-" * 70)
        
        # Score Statistics
        print("\n📈 Score Statistics:")
        print(f"   Average Score: {statistics.mean(scores):.2f}")
        print(f"   Median Score:  {statistics.median(scores):.2f}")
        if len(scores) > 1:
            print(f"   Std Deviation: {statistics.stdev(scores):.2f}")
        else:
            print(f"   Std Deviation: N/A")
        print(f"   Highest Score: {max(scores)} 🏆")
        print(f"   Lowest Score:  {min(scores)} 💀")
        print(f"   Score Range:   {max(scores) - min(scores)}")
        
        # Behavioral Category Performance
        print("\n🎯 Behavioral Category Performance (Average Scores):")
        print("-" * 70)
        for cat, scores_list in category_performance.items():
            if scores_list:
                avg = statistics.mean(scores_list)
                trend = "✅" if avg > 0 else "⚠️" if avg == 0 else "❌"
                print(f"   {trend} {cat.capitalize():15}: {avg:6.2f}")
        
        # Gift Value Analytics
        total_gift_value = sum(a.gift['value'] for a in self.assessments)
        avg_gift_value = total_gift_value / total
        print("\n💰 Gift Value Analytics:")
        print(f"   Total Gift Value:   ${total_gift_value:,.2f}")
        print(f"   Average Gift Value: ${avg_gift_value:,.2f}")
        print(f"   Most Valuable Gift: ${max(a.gift['value'] for a in self.assessments):,.2f}")
        
        # Top/Bottom Performers
        print("\n🌟 Top 3 Performers:")
        top_performers = sorted(self.assessments, key=lambda x: x.score, reverse=True)[:3]
        for i, a in enumerate(top_performers, 1):
            print(f"   {i}. {a.name}: {a.score} pts ({a.category.upper()})")
        
        if len(self.assessments) >= 3:
            print("\n💀 Bottom 3 Performers:")
            bottom_performers = sorted(self.assessments, key=lambda x: x.score)[:3]
            for i, a in enumerate(bottom_performers, 1):
                print(f"   {i}. {a.name}: {a.score} pts ({a.category.upper()})")
        
        print("="*70)

    def display_result(self, assessment):
        """Display individual assessment result."""
        category_info = CATEGORIES[assessment.category]
        
        print("\n" + "="*70)
        print("🎁 ASSESSMENT RESULT 🎁")
        print("="*70)
        print(f"Child: {assessment.name}")
        print(f"Timestamp: {assessment.timestamp}")
        print(f"\nTotal Score: {assessment.score} points")
        print(f"Category: {category_info['emoji']} {assessment.category.upper()}")
        print(f"\nGift Assigned: {assessment.gift['name']}")
        print(f"Gift Value: ${assessment.gift['value']:,.2f}")
        
        # Category breakdown
        print("\n📊 Behavioral Breakdown:")
        for cat, score in assessment.category_scores.items():
            indicator = "✅" if score > 0 else "⚠️" if score == 0 else "❌"
            print(f"   {indicator} {cat.capitalize():15}: {score:+3d} points")
        
        print("="*70)

    def assess_child(self, name, num_questions=10):
        """Conduct full assessment for a child."""
        score, category_scores, answers = self.ask_questions(num_questions)
        category = self.categorize_score(score)
        gift = self.assign_gift(category)
        
        assessment = Assessment(
            name=name,
            score=score,
            category=category,
            gift=gift,
            timestamp=datetime.now().isoformat(),
            category_scores=category_scores,
            answers=answers
        )
        
        self.assessments.append(assessment)
        self.save_data()
        return assessment
    
    def view_all_results(self):
        """Display all assessment results in a table format."""
        if not self.assessments:
            print("\n❌ No children assessed yet!")
            return
        
        print("\n" + "="*70)
        print("📋 ALL ASSESSMENT RESULTS 📋")
        print("="*70)
        print(f"{'Name':<20} {'Score':>6} {'Category':<12} {'Gift':<30}")
        print("-" * 70)
        
        for a in self.assessments:
            category_info = CATEGORIES[a.category]
            print(f"{a.name:<20} {a.score:>6} {category_info['emoji']} {a.category.upper():<9} {a.gift['name']:<30}")
        
        print("="*70)
    
    def export_to_text(self, filename=None):
        """Export all assessments to text file."""
        if not self.assessments:
            print("\n❌ No data to export!")
            return
        
        if filename is None:
            filename = f"santa_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        export_data = {
            "export_date": datetime.now().isoformat(),
            "total_assessments": len(self.assessments),
            "assessments": [a.to_dict() for a in self.assessments]
        }
        
        with open(filename, 'w') as f:
            f.write(repr(export_data))
        
        print(f"\n✅ Data exported successfully to {filename}")
    
    def save_data(self):
        """Save assessments to persistent storage."""
        data = [a.to_dict() for a in self.assessments]
        with open(self.data_file, 'w') as f:
            f.write(repr(data))
    
    def load_data(self):
        """Load assessments from persistent storage."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    content = f.read().strip()
                    if content:
                        data = eval(content)
                        self.assessments = [Assessment(**item) for item in data]
                        print(f"✅ Loaded {len(self.assessments)} previous assessments")
                    else:
                        self.assessments = []
            except Exception as e:
                print(f"⚠️  Warning: Could not load previous data: {e}")
                self.assessments = []
        else:
            self.assessments = []
    
    def search_child(self, name):
        """Search for assessments by child name."""
        results = [a for a in self.assessments if name.lower() in a.name.lower()]
        
        if not results:
            print(f"\n❌ No assessments found for '{name}'")
            return
        
        print(f"\n🔍 Found {len(results)} assessment(s) for '{name}':")
        print("="*70)
        for a in results:
            category_info = CATEGORIES[a.category]
            print(f"\n📅 {a.timestamp}")
            print(f"   Score: {a.score} | Category: {category_info['emoji']} {a.category.upper()}")
            print(f"   Gift: {a.gift['name']}")
        print("="*70)


def main():
    """Main program loop."""
    engine = SantaEngine()
    
    print("\n" + "="*70)
    print("🎄✨ SANTA'S NAUGHTY/NICE ANALYTICS ENGINE ✨🎅")
    print("="*70)
    print("Help Santa determine who gets what gifts this Christmas!")
    print("="*70)
    
    while True:
        print("\n📋 Main Menu:")
        print("  1. 🧒 Assess a child")
        print("  2. 📊 View comprehensive analytics")
        print("  3. 📋 View all results")
        print("  4. 🔍 Search for a child")
        print("  5. 💾 Export data to text file")
        print("  6. 🗑️  Clear all data")
        print("  7. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            name = input("\n👤 Enter child's name: ").strip()
            if not name:
                print("❌ Name cannot be empty!")
                continue
            
            try:
                num_questions = int(input(f"📝 Number of questions (1-{len(QUESTIONS)}): ").strip() or "10")
                num_questions = max(1, min(num_questions, len(QUESTIONS)))
            except ValueError:
                num_questions = 10
            
            assessment = engine.assess_child(name, num_questions)
            engine.display_result(assessment)
            
        elif choice == "2":
            engine.analyze_results()
            
        elif choice == "3":
            engine.view_all_results()
            
        elif choice == "4":
            search_name = input("\n🔍 Enter child's name to search: ").strip()
            if search_name:
                engine.search_child(search_name)
            else:
                print("❌ Name cannot be empty!")
        
        elif choice == "5":
            custom_name = input("\n💾 Enter filename (or press Enter for auto-generated): ").strip()
            engine.export_to_text(custom_name if custom_name else None)
        
        elif choice == "6":
            confirm = input("\n⚠️  Are you sure you want to clear all data? (yes/no): ").strip().lower()
            if confirm == "yes":
                engine.assessments = []
                engine.save_data()
                print("✅ All data cleared!")
            else:
                print("❌ Cancelled")
                
        elif choice == "7":
            print("\n🎅 Thank you for helping Santa! Merry Christmas! 🎄✨\n")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🎅 Goodbye! Merry Christmas! 🎄")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please report this issue to Santa's IT department! 🎅")
