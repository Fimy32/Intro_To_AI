class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion


class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = set()

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_fact(self, fact):
        self.facts.add(fact)

    def ask_user_for_fact(self, fact):
        response = input(f"Is the weather sunny {fact}? (yes/no): ").strip().lower()
        if response == 'yes':
            return fact
        else:
            return False

    def infer(self):
        asked_facts = set()
        response = False
        while not response and not isinstance(response, str):
            for rule in self.rules:
                for condition in rule.conditions:
                    if condition not in self.facts and condition not in asked_facts:
                        response = self.ask_user_for_fact(condition)
        print("As it is",response,", I advise you to")

# Example usage
if __name__ == "__main__":
    # Create an expert system
    es = ExpertSystem()
    # Add rules
    es.add_rule(Rule(["sunny"], "wear_sunglasses"))
    es.add_rule(Rule(["rainy"], "take_umbrella"))
    es.add_rule(Rule(["unbreathable atmosphere"], "try_not_to_die"))
    es.add_rule(Rule(["acid rainy"], "Don't_be_a_robot"))
    # Perform inference
    es.infer()
    # Print final facts
    print("Final facts:", es.facts)
