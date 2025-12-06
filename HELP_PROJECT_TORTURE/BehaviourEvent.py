import random

# List with each question. Weighting system assuming answer is yes or maximum
questions = [
    {"question": "Do you help others without being asked?", "weight": 4, "type": "yesno"},
    {"question": "Do you feel bad after hurting someone's feelings?", "weight": 5, "type": "yesno"},
    {"question": "Do you tell the truth even when you might get in trouble?", "weight": 5, "type": "yesno"},
    {"question": "Do you include kids who are left out?", "weight": 4, "type": "yesno"},
    {"question": "When someone is sad, do you try to help them?", "weight": 5, "type": "yesno"},
    {"question": "Do you say thank you when someone helps you?", "weight": 3, "type": "yesno"},
    {"question": "Do you follow rules even when nobody is watching?", "weight": 5, "type": "yesno"},
    {"question": "How often do you share your things?", "weight": 3, "type": "scale_1_5"},
    {"question": "How much do you care if your actions hurt others?", "weight": 5, "type": "scale_1_5"},
    {"question": "When you make a mistake, do you try to fix it?", "weight": 4, "type": "yesno"},
    
    {"question": "Do you lie to avoid trouble?", "weight": -5, "type": "yesno"},
    {"question": "Do you enjoy teasing or humiliating others?", "weight": -5, "type": "yesno"},
    {"question": "Do you break rules for fun?", "weight": -4, "type": "yesno"},
    {"question": "Do you blame others for things you did?", "weight": -4, "type": "yesno"},
    {"question": "Do you enjoy getting away with bad behavior?", "weight": -5, "type": "yesno"},
    {"question": "Have you ever hurt someone on purpose?", "weight": -6, "type": "yesno"},
    {"question": "How often do you get angry and act without thinking?", "weight": -4, "type": "scale_1_5"},
    {"question": "How often do you ignore rules when they annoy you?", "weight": -3, "type": "scale_1_5"},
    {"question": "How much do you care about being fair?", "weight": 4, "type": "scale_1_5"},
    {"question": "If you find something that isn't yours, do you keep it?", "weight": -5, "type": "yesno"}
]


class Children:
    """Represents a child with questionnaire-based behavior assessment"""
    
    # Defining unchangeable values for each child
    def __init__(self, _name, _gender, _age=None, _location=None):
        self.name = _name
        self.gender = _gender
        self.age = _age
        self.location = _location
        self.category = None
        self.behaviour_score = None
        self.answers = []
    
    def take_questionnaire(self, auto_answer=False):
        """
        Have the child take the questionnaire
        auto_answer: if True, generates random answers for simulation
        """
        self.answers = []
        total_score = 0
        
        print(f"\n{'='*60}")
        print(f"Questionnaire for {self.name}")
        print(f"{'='*60}\n")
        
        for i, q in enumerate(questions, 1):
            print(f"Question {i}/{len(questions)}:")
            print(f"  {q['question']}")
            
            if auto_answer:
                # Generate random answer for simulation
                if q['type'] == 'yesno':
                    answer = random.choice(['yes', 'no'])
                    print(f"  Answer: {answer}")
                else:  # scale_1_5
                    answer = random.randint(1, 5)
                    print(f"  Answer: {answer}/5")
            else:
                # Get user input
                if q['type'] == 'yesno':
                    answer = input("  Answer (yes/no): ").strip().lower()
                    while answer not in ['yes', 'no', 'y', 'n']:
                        answer = input("  Please answer yes or no: ").strip().lower()
                    if answer == 'y':
                        answer = 'yes'
                    elif answer == 'n':
                        answer = 'no'
                else:  # scale_1_5
                    answer = input("  Answer (1-5, where 5 is most): ").strip()
                    while not answer.isdigit() or int(answer) not in range(1, 6):
                        answer = input("  Please enter a number from 1 to 5: ").strip()
                    answer = int(answer)
            
            # Calculate score for this question
            question_score = self._calculate_question_score(q, answer)
            total_score += question_score
            
            # Store the answer
            self.answers.append({
                "question": q['question'],
                "answer": answer,
                "score": question_score
            })
            
            print()
        
        self.behaviour_score = total_score
        self.category = self._determine_category()
        
        return total_score
    
    def _calculate_question_score(self, question, answer):
        """Calculate score for a single question"""
        weight = question['weight']
        
        if question['type'] == 'yesno':
            # For positive weights: yes = full weight, no = 0
            # For negative weights: yes = full weight (negative), no = 0
            if answer in ['yes', 'y']:
                return weight
            else:
                return 0
        else:  # scale_1_5
            # Scale the answer (1-5) to the weight
            # For positive weights: higher answer = higher score
            # For negative weights: higher answer = more negative score
            return weight * (answer / 5.0)
    
    def _determine_category(self):
        """Determine the child's category based on their score"""
        if self.behaviour_score is None:
            return "Not Assessed"
        
        # Calculate max possible score
        max_score = sum(abs(q['weight']) for q in questions if q['weight'] > 0)
        min_score = -sum(abs(q['weight']) for q in questions if q['weight'] < 0)
        
        # Normalize score to percentage
        total_range = max_score + abs(min_score)
        normalized = ((self.behaviour_score - min_score) / total_range) * 100
        
        if normalized >= 80:
            return "Very Nice ⭐"
        elif normalized >= 60:
            return "Nice ✓"
        elif normalized >= 40:
            return "Neutral ~"
        elif normalized >= 20:
            return "Naughty ⚠"
        else:
            return "Very Naughty ✗"
    
    def get_report(self):
        """Get a detailed report of the child's assessment"""
        if self.behaviour_score is None:
            return f"{self.name} has not been assessed yet."
        
        report = []
        report.append(f"{'='*60}")
        report.append(f"Assessment Report for {self.name}")
        report.append(f"{'='*60}")
        report.append(f"Gender: {self.gender}")
        if self.age:
            report.append(f"Age: {self.age}")
        if self.location:
            report.append(f"Location: {self.location}")
        report.append(f"Behavior Score: {self.behaviour_score:.2f}")
        report.append(f"Category: {self.category}")
        report.append("")
        
        # Analyze positive behaviors
        positive_answers = [a for a in self.answers if a['score'] > 0]
        negative_answers = [a for a in self.answers if a['score'] < 0]
        
        if positive_answers:
            report.append("Positive Behaviors:")
            for ans in sorted(positive_answers, key=lambda x: x['score'], reverse=True)[:5]:
                report.append(f"  ✅ {ans['question']}")
                report.append(f"     Answer: {ans['answer']} (Score: +{ans['score']:.2f})")
            report.append("")
        
        if negative_answers:
            report.append("Areas of Concern:")
            for ans in sorted(negative_answers, key=lambda x: x['score'])[:5]:
                report.append(f"  ❌ {ans['question']}")
                report.append(f"     Answer: {ans['answer']} (Score: {ans['score']:.2f})")
            report.append("")
        
        report.append(f"{'='*60}")
        
        return "\n".join(report)
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "location": self.location,
            "category": self.category,
            "behaviour_score": self.behaviour_score,
            "answers": self.answers
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Children object from dictionary"""
        child = cls(
            data['name'],
            data['gender'],
            data.get('age'),
            data.get('location')
        )
        child.category = data.get('category')
        child.behaviour_score = data.get('behaviour_score')
        child.answers = data.get('answers', [])
        return child


def simulate_questionnaire_for_child(name, gender, age=None, location=None):
    """Simulate a questionnaire for a child with random answers"""
    child = Children(name, gender, age, location)
    child.take_questionnaire(auto_answer=True)
    return child


def interactive_questionnaire():
    """Run an interactive questionnaire session"""
    print("\n🎅 Welcome to Santa's Behavior Assessment Questionnaire! 🎄\n")
    
    name = input("Child's name: ").strip()
    gender = input("Gender: ").strip()
    age_input = input("Age (optional, press Enter to skip): ").strip()
    age = int(age_input) if age_input.isdigit() else None
    location = input("Location (optional, press Enter to skip): ").strip() or None
    
    child = Children(name, gender, age, location)
    
    print("\nGreat! Now let's answer some questions.")
    print("Please answer honestly - Santa knows if you're telling the truth! 🎅")
    
    child.take_questionnaire(auto_answer=False)
    
    print("\n" + child.get_report())
    
    # Option to save
    save = input("\nWould you like to save this assessment? (yes/no): ").strip().lower()
    if save in ['yes', 'y']:
        import json
        filename = f"{name.replace(' ', '_')}_assessment.json"
        with open(filename, 'w') as f:
            json.dump(child.to_dict(), f, indent=2)
        print(f"✅ Assessment saved to {filename}")
    
    return child


def batch_simulation(num_children=5):
    """Simulate questionnaires for multiple children"""
    sample_names = [
        ("Emma Johnson", "Female", 8, "New York, USA"),
        ("Oliver Smith", "Male", 10, "London, UK"),
        ("Sophia Martinez", "Female", 7, "Madrid, Spain"),
        ("Lucas Brown", "Male", 9, "Toronto, Canada"),
        ("Mia Wilson", "Female", 11, "Sydney, Australia"),
        ("Noah Davis", "Male", 6, "Paris, France"),
        ("Isabella Garcia", "Female", 8, "Mexico City, Mexico"),
        ("Ethan Anderson", "Male", 10, "Berlin, Germany"),
        ("Ava Taylor", "Female", 7, "Tokyo, Japan"),
        ("Mason Thomas", "Male", 9, "São Paulo, Brazil"),
    ]
    
    children = []
    for i in range(min(num_children, len(sample_names))):
        name, gender, age, location = sample_names[i]
        child = simulate_questionnaire_for_child(name, gender, age, location)
        children.append(child)
    
    return children


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Santa's Questionnaire-Based Behavior Assessment"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run interactive questionnaire"
    )
    parser.add_argument(
        "--simulate",
        type=int,
        metavar="N",
        help="Simulate N children with random answers"
    )
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_questionnaire()
    elif args.simulate:
        print(f"\n🎅 Simulating questionnaires for {args.simulate} children...\n")
        children = batch_simulation(args.simulate)
        
        print("\n" + "="*60)
        print("SIMULATION RESULTS")
        print("="*60 + "\n")
        
        for child in children:
            print(f"{child.name}: Score = {child.behaviour_score:.2f}, Category = {child.category}")
        
        # Save to file
        import json
        with open("questionnaire_results.json", 'w') as f:
            json.dump([c.to_dict() for c in children], f, indent=2)
        print("\n✅ Results saved to questionnaire_results.json")
    else:
        print("Usage:")
        print("  Interactive mode: python3 questionnaire_system.py --interactive")
        print("  Simulation mode:  python3 questionnaire_system.py --simulate 5")


if __name__ == "__main__":
    main()