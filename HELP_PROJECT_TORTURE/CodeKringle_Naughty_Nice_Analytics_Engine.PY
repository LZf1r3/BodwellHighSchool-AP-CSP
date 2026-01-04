"""
AP Computer Science Christmas Project
Naughty/Nice Analytics System for the North Pole

T
"""

import random
import os

class Child:
    """Child class to store all child data."""
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender  # "M", "F", or "X"
        self.responses = []  # List of (question, answer, points) tuples
        self.score = 0
        self.category = ""  # "evil", "naughty", "nice", "angelic"
        self.gift = ""
    
    def __str__(self):
        return f"{self.name} ({self.gender}): {self.score} pts -> {self.category} -> {self.gift}"


# Behavior questions with weighted points
# Format: (question, points_for_yes)
BEHAVIOR_QUESTIONS = [
    ("How often did this child help others this year? (frequently/rarely/never)", 15, -5, -15),
    ("How often did they lie to parents or teachers?", -20, -5, 5),
    ("Did they share toys with siblings or friends?", 12, -3, -8),
    ("Did they complete homework assignments on time?", 8, -2, -10),
    ("Did they say mean things to others?", -15, -5, 8),
    ("Did they volunteer or help in the community?", 18, -2, -8),
    ("Did they break things on purpose?", -18, -3, 10),
    ("Did they apologize when they made mistakes?", 10, -2, -6),
    ("Did they stand up for others being bullied?", 16, -4, -10),
    ("Did they waste food or resources?", -10, -3, 8),
]

# Category thresholds
CATEGORY_THRESHOLDS = {
    "evil": (-999, -40),
    "naughty": (-40, 20),
    "nice": (20, 70),
    "angelic": (70, 999)
}

# Target percentage ranges for global constraints
TARGET_PERCENTAGES = {
    "nice": (50, 80),
    "angelic": (0, 20),
    "naughty": (10, 40),
    "evil": (0, 10)
}

# Gift inventory: (name, quantity, gender_compatibility, bias_weight)
# gender_compatibility: "M", "F", "X", or "ALL"
# bias_weight: higher = more likely (out of 100)
GIFT_INVENTORY = [
    # Nice/angelic toys
    ("Remote Control Car", 3, "M", 50),
    ("Doll Set", 3, "F", 50),
    ("LEGO Set", 4, "ALL", 30),
    ("Art Supplies", 3, "ALL", 20),
    ("Bike", 2, "ALL", 40),
    ("Video Game Console", 2, "ALL", 60),  # High bias (favorite)
    ("Soccer Ball", 4, "ALL", 15),
    ("Science Kit", 3, "ALL", 25),
    # Naughty gifts
    ("Coal", 10, "ALL", 100),
    ("Socks", 10, "ALL", 80),
    ("Chores List", 10, "ALL", 60),
    # Evil gifts
    ("Krampus Warning", 5, "ALL", 100),
]

# ASCII Art for gifts
GIFT_ART = {
    "Remote Control Car": """
          ______
         /|_||_\`.__
        (   _    _ _\
        =`-(_)--(_)-' 
    """,
    "Doll Set": """
    ╔═══════╗
    ║  👗   ║
    ║  🎀   ║
    ╚═══════╝
    """,
    "LEGO Set": """
    ╔═══════╗
    ║  🧱   ║
    ║  🧱🧱 ║
    ╚═══════╝
    """,
    "Art Supplies": """
                     ,
                   ,'|
                  (  ;   ,\
            _..-'';,'._,','
         ,-' ,-. //,-,:\'.
       ,' _  `-'// >',',-.\
     ,'  (_)   //,','  `-' :
    /,-.      //','     _  |
   : `-'    _//,'      (_) |
   :       (//')     _     ;
    `._.,-. `-'  _  (_)   /
      ,','/;.   (_)     ,'
     `-' //  \       _.'
        //    `-..-''  

    """,
    "Bike": """
    ╔═══════╗
    ║  🚲   ║
    ║  ⚙️   ║
    ╚═══════╝
    """,
    "Video Game Console": """
    ╔═══════╗
    ║  🎮   ║
    ║  ⚡   ║
    ╚═══════╝
    """,
    "Soccer Ball": """
    ╔═══════╗
    ║  ⚽   ║
    ║      ║
    ╚═══════╝
    """,
    "Science Kit": """
    ╔═══════╗
    ║  🔬   ║
    ║  ⚗️   ║
    ╚═══════╝
    """,
    "Coal": """
    ╔═══════╗
    ║  ⚫   ║
    ║  ⚫⚫  ║
    ╚═══════╝
    """,
    "Socks": """
    ╔═══════╗
    ║  🧦   ║
    ║  🧦   ║
    ╚═══════╝
    """,
    "Chores List": """
    ╔═══════╗
    ║  📋   ║
    ║  ✓✓✓  ║
    ╚═══════╝
    """,
    "Krampus Warning": """
  ,/         \.
 ((           ))
  \`.       ,'/
   )')     (`(
 ,'`/       \,`.
(`-(         )-')
 \-'\,-'"`-./`-/
  \-')     (`-/
  /`'       `'\
 (  _       _  )
 | ( \     / ) |
 |  `.\   /,'  |
 |    `\ /'    |
 (             )
  \           /
   \         /
    `.     ,'
      `-.-'

    """,
    "IOU": """
    ╔═══════╗
    ║  💳   ║
    ║  IOU  ║
    ╚═══════╝
    """
}

# Global list to store all children
children = []
gift_inventory = {}  # name -> current_quantity


def initialize_inventory():
    """Initialize gift inventory from GIFT_INVENTORY."""
    global gift_inventory
    gift_inventory = {}
    for name, quantity, gender, bias in GIFT_INVENTORY:
        gift_inventory[name] = {
            "quantity": quantity,
            "gender": gender,
            "bias": bias,
            "original_quantity": quantity
        }


def calculate_behavior_score(child, simulate=False):
    """
    Calculate behavior score for a single child.
    Includes: question responses + name-based modifiers + RNG modifier
    """
    score = 0
    child.responses = []
    
    # Ask all behavior questions
    for question, yes_points, sometimes_points, no_points in BEHAVIOR_QUESTIONS:
        if simulate:
            # Simulate: 60% yes, 25% sometimes, 15% no for positive questions
            # For negative questions, reverse
            if yes_points > 0:
                rand = random.random()
                if rand < 0.15:
                    answer = "no"
                    points = no_points
                elif rand < 0.40:
                    answer = "sometimes"
                    points = sometimes_points
                else:
                    answer = "frequently"
                    points = yes_points
            else:
                rand = random.random()
                if rand < 0.60:
                    answer = "no"
                    points = no_points
                elif rand < 0.85:
                    answer = "sometimes"
                    points = sometimes_points
                else:
                    answer = "frequently"
                    points = yes_points
        else:
            while True:
                answer = input(f"{question} (frequently/sometimes/never): ").lower().strip()
                if answer in ["frequently", "sometimes", "never", "f", "s", "n"]:
                    if answer in ["frequently", "f"]:
                        answer = "frequently"
                        points = yes_points
                    elif answer in ["sometimes", "s"]:
                        answer = "sometimes"
                        points = sometimes_points
                    else:
                        answer = "never"
                        points = no_points
                    break
        
        score += points
        child.responses.append((question, answer, points))
    
    # Apply name-based modifiers
    name = child.name.upper()
    
    # Rule 1: Double letters (e.g., "ANNA", "BILLY")
    has_double_letter = False
    for i in range(len(name) - 1):
        if name[i] == name[i + 1] and name[i].isalpha():
            has_double_letter = True
            break
    if has_double_letter:
        score += 5  # Bonus for double letters
    
    # Rule 2: Unique letters (no repeats)
    unique_letters = set([c for c in name if c.isalpha()])
    if len(unique_letters) == len([c for c in name if c.isalpha()]):
        score -= 4  # Penalty for all unique letters
    
    # Rule 3: Lucky first letter (A, J, S)
    lucky_letters = {"A", "J", "S"}
    if name and name[0] in lucky_letters:
        score += 6  # Bonus for lucky first letter
    
    # Apply RNG modifier (-3 to +3)
    rng_modifier = random.randint(-3, 3)
    score += rng_modifier
    
    child.score = score
    return score


def categorize_child(child):
    """
    Categorize a child into evil/naughty/nice/angelic based on score.
    """
    score = child.score
    
    if score >= CATEGORY_THRESHOLDS["angelic"][0]:
        child.category = "angelic"
    elif score >= CATEGORY_THRESHOLDS["nice"][0]:
        child.category = "nice"
    elif score >= CATEGORY_THRESHOLDS["naughty"][0]:
        child.category = "naughty"
    else:
        child.category = "evil"
    
    return child.category


def assign_gift(child):
    """
    Assign a gift to a child based on category, gender, and inventory.
    Uses biased random selection with inventory limits.
    """
    category = child.category
    gender = child.gender
    
    # Filter available gifts by category and gender
    available_gifts = []
    gift_weights = []
    
    if category in ["nice", "angelic"]:
        # Nice children get toys
        for gift_name, info in gift_inventory.items():
            if info["quantity"] > 0:
                # Check gender compatibility
                if info["gender"] == "ALL" or info["gender"] == gender:
                    available_gifts.append(gift_name)
                    gift_weights.append(info["bias"])
    
    elif category == "naughty":
        # Naughty children get coal, socks, etc.
        for gift_name, info in gift_inventory.items():
            if info["quantity"] > 0 and gift_name in ["Coal", "Socks", "Chores List"]:
                available_gifts.append(gift_name)
                gift_weights.append(info["bias"])
    
    else:  # evil
        # Evil children get Krampus warning
        if "Krampus Warning" in gift_inventory and gift_inventory["Krampus Warning"]["quantity"] > 0:
            available_gifts = ["Krampus Warning"]
            gift_weights = [100]
    
    # If no gifts available, give IOU
    if not available_gifts:
        child.gift = "IOU"
        return
    
    # Biased random selection based on weights
    total_weight = sum(gift_weights)
    if total_weight == 0:
        selected_gift = random.choice(available_gifts)
    else:
        rand = random.random() * total_weight
        cumulative = 0
        selected_gift = available_gifts[0]
        for i, weight in enumerate(gift_weights):
            cumulative += weight
            if rand <= cumulative:
                selected_gift = available_gifts[i]
                break
    
    child.gift = selected_gift
    # Decrease inventory
    gift_inventory[selected_gift]["quantity"] -= 1


def adjust_category_percentages(children_list):
    """
    Adjust categories to meet global percentage constraints.
    Finds borderline children and reassigns categories.
    """
    total = len(children_list)
    if total == 0:
        return
    
    # Calculate current percentages
    category_counts = {"evil": 0, "naughty": 0, "nice": 0, "angelic": 0}
    for child in children_list:
        category_counts[child.category] = category_counts.get(child.category, 0) + 1
    
    current_percentages = {}
    for cat in category_counts:
        current_percentages[cat] = (category_counts[cat] / total) * 100
    
    # Check which categories need adjustment
    adjustments_needed = []
    for cat in ["nice", "naughty", "evil", "angelic"]:
        min_target, max_target = TARGET_PERCENTAGES[cat]
        current = current_percentages.get(cat, 0)
        if current < min_target:
            adjustments_needed.append((cat, "increase", min_target - current))
        elif current > max_target:
            adjustments_needed.append((cat, "decrease", current - max_target))
    
    # Sort children by proximity to category boundaries
    # For each category needing adjustment, find borderline children
    for cat, direction, amount in adjustments_needed:
        if direction == "increase":
            # Need more in this category - find children in lower categories close to boundary
            candidates = []
            if cat == "nice":
                # Look for naughty children close to nice threshold (score near 20)
                for child in children_list:
                    if child.category == "naughty" and child.score >= 15:
                        candidates.append((child, abs(child.score - 20)))
            elif cat == "angelic":
                # Look for nice children close to angelic threshold (score near 70)
                for child in children_list:
                    if child.category == "nice" and child.score >= 65:
                        candidates.append((child, abs(child.score - 70)))
            elif cat == "naughty":
                # Look for nice children close to naughty threshold (score near 20)
                for child in children_list:
                    if child.category == "nice" and child.score <= 25:
                        candidates.append((child, abs(child.score - 20)))
            
            # Sort by proximity and reassign closest ones
            candidates.sort(key=lambda x: x[1])
            needed_count = int((amount / 100) * total)
            for i in range(min(needed_count, len(candidates))):
                candidates[i][0].category = cat
        
        elif direction == "decrease":
            # Need fewer in this category - move some to adjacent categories
            candidates = []
            if cat == "nice":
                # Move nice children with low scores to naughty
                for child in children_list:
                    if child.category == "nice" and child.score <= 30:
                        candidates.append((child, abs(child.score - 20)))
            elif cat == "angelic":
                # Move angelic children with lower scores to nice
                for child in children_list:
                    if child.category == "angelic" and child.score <= 75:
                        candidates.append((child, abs(child.score - 70)))
            elif cat == "naughty":
                # Move naughty children with higher scores to nice, or lower to evil
                for child in children_list:
                    if child.category == "naughty":
                        if child.score >= 15:
                            candidates.append((child, abs(child.score - 20)))
            
            # Sort and reassign
            candidates.sort(key=lambda x: x[1])
            needed_count = int((amount / 100) * total)
            for i in range(min(needed_count, len(candidates))):
                if cat == "nice":
                    candidates[i][0].category = "naughty"
                elif cat == "angelic":
                    candidates[i][0].category = "nice"
                elif cat == "naughty":
                    if candidates[i][0].score >= 15:
                        candidates[i][0].category = "nice"
                    else:
                        candidates[i][0].category = "evil"
    
    # Reassign gifts after category changes
    for child in children_list:
        assign_gift(child)


def generate_summary_statistics(children_list):
    """
    Generate and print summary statistics.
    Takes a list of children as parameter and uses iteration and selection.
    """
    total = len(children_list)
    if total == 0:
        print("\n❌ No children to analyze!")
        return
    
    # Count by category using iteration
    category_counts = {"evil": 0, "naughty": 0, "nice": 0, "angelic": 0}
    for child in children_list:
        category_counts[child.category] = category_counts.get(child.category, 0) + 1
    
    # Calculate percentages
    category_percentages = {}
    for cat in category_counts:
        category_percentages[cat] = (category_counts[cat] / total) * 100
    
    # Find most common gift
    gift_counts = {}
    for child in children_list:
        gift = child.gift
        gift_counts[gift] = gift_counts.get(gift, 0) + 1
    
    most_common_gift = max(gift_counts.items(), key=lambda x: x[1])[0] if gift_counts else "None"
    
    # Calculate leftover inventory
    leftover_inventory = []
    for gift_name, info in gift_inventory.items():
        if info["quantity"] > 0:
            leftover_inventory.append((gift_name, info["quantity"]))
    
    # Print statistics
    print("\n" + "="*70)
    print("📊 SUMMARY STATISTICS 📊")
    print("="*70)
    print(f"Total Children: {total}")
    print("\nCategory Distribution:")
    for cat in ["angelic", "nice", "naughty", "evil"]:
        count = category_counts.get(cat, 0)
        pct = category_percentages.get(cat, 0)
        print(f"  {cat.upper():10}: {count:3} children ({pct:5.1f}%)")
    
    print(f"\nMost Common Gift: {most_common_gift} ({gift_counts.get(most_common_gift, 0)} times)")
    
    print("\nLeftover Inventory:")
    if leftover_inventory:
        for gift_name, quantity in leftover_inventory:
            print(f"  {gift_name}: {quantity} remaining")
    else:
        print("  None - all gifts distributed!")
    
    print("="*70)


def print_per_child_report(child):
    """Print detailed report for a single child."""
    print("\n" + "="*70)
    print(f"🎁 PER-CHILD REPORT: {child.name.upper()} 🎁")
    print("="*70)
    print(f"Name: {child.name}")
    print(f"Gender: {child.gender}")
    print(f"Behavior Score: {child.score} points")
    print(f"Final Category: {child.category.upper()}")
    print(f"Assigned Gift: {child.gift}")
    print("\nQuestion Responses:")
    for question, answer, points in child.responses:
        print(f"  - {question[:50]}...")
        print(f"    Answer: {answer} | Points: {points:+d}")
    print("\nGift ASCII Art:")
    art = GIFT_ART.get(child.gift, "")
    print(art)
    print("="*70)


def print_category_lists(children_list):
    """Print all children grouped by category."""
    categories = ["angelic", "nice", "naughty", "evil"]
    
    print("\n" + "="*70)
    print("📋 CHILDREN BY CATEGORY 📋")
    print("="*70)
    
    for category in categories:
        category_children = [c for c in children_list if c.category == category]
        if category_children:
            print(f"\n{category.upper()} ({len(category_children)} children):")
            print("-" * 70)
            for child in category_children:
                art_line = GIFT_ART.get(child.gift, "").split('\n')[1] if child.gift in GIFT_ART else ""
                print(f"  {child.name:<20} Score: {child.score:>4} | Gift: {child.gift}")
    print("="*70)


def main():
    """Main program."""
    global children
    
    initialize_inventory()
    
    print("\n" + "="*70)
    print("🎄 SANTA'S NAUGHTY/NICE ANALYTICS SYSTEM 🎅")
    print("="*70)
    print("AP Computer Science Christmas Project")
    print("="*70)
    
    while True:
        print("\nMenu:")
        print("  1. Add child manually")
        print("  2. Simulate 20 children")
        print("  3. View per-child reports")
        print("  4. View category lists")
        print("  5. Generate summary statistics")
        print("  6. Apply global percentage constraints")
        print("  7. Clear all data")
        print("  8. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            name = input("\nChild's name: ").strip()
            if name:
                while True:
                    gender = input("Gender (M/F/X): ").strip().upper()
                    if gender in ["M", "F", "X"]:
                        break
                    print("Please enter M, F, or X")
                
                child = Child(name, gender)
                calculate_behavior_score(child, simulate=False)
                categorize_child(child)
                assign_gift(child)
                children.append(child)
                print_per_child_report(child)
        
        elif choice == "2":
            print("\n🎲 Simulating 20 children...")
            children.clear()
            initialize_inventory()
            
            names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", 
                     "Henry", "Ivy", "Jack", "Kate", "Liam", "Mia", "Noah", 
                     "Olivia", "Paul", "Quinn", "Ruby", "Sam", "Tina"]
            genders = ["M", "F", "X"]
            
            for i, name in enumerate(names):
                gender = random.choice(genders)
                child = Child(name, gender)
                calculate_behavior_score(child, simulate=True)
                categorize_child(child)
                children.append(child)
            
            # Assign gifts
            for child in children:
                assign_gift(child)
            
            print(f"\n✅ Simulated {len(children)} children!")
            generate_summary_statistics(children)
        
        elif choice == "3":
            if not children:
                print("\n❌ No children added yet!")
            else:
                print("\nPer-Child Reports:")
                for child in children:
                    print_per_child_report(child)
        
        elif choice == "4":
            if not children:
                print("\n❌ No children added yet!")
            else:
                print_category_lists(children)
        
        elif choice == "5":
            generate_summary_statistics(children)
        
        elif choice == "6":
            if not children:
                print("\n❌ No children to adjust!")
            else:
                print("\n🔄 Applying global percentage constraints...")
                adjust_category_percentages(children)
                print("✅ Categories adjusted!")
                generate_summary_statistics(children)
        
        elif choice == "7":
            if input("\nClear all data? (yes): ").strip().lower() == "yes":
                children.clear()
                initialize_inventory()
                print("✅ All data cleared!")
        
        elif choice == "8":
            print("\n🎅 Thank you for using Santa's Analytics System! 🎄\n")
            break
        
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    os.system("clear")
    main()
    print("\n\n🎅 Goodbye! 🎄")