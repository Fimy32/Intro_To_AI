class Goal:
    def __init__(self, description):
        self.description = description



class Query:
    def __init__(self, goaladvancement: bool, question: str, answer: str):
        self.advancement = goaladvancement
        self.question = question
        self.answer = answer

    def ask(self):
        if self.advancement:
            if not input(self.question.lower() + "?") == self.answer.lower():
                print("1")
                return False
            else:
                print("2")
                return True
        else:
            if input(self.question.lower() + "?") == self.answer.lower():
                print("3")
                return True
            else:
                print("4")
                return False


class YesNoQuery(Query):
    def __init__(self, yesno):
        if yesno.lower == "yes":
            self.answer = "YES"
        else:
            self.answer = "NO"


class Database:
    def __init__(self, queries: list[Query], goal: Goal):
        self.queries = queries
        self.goal = goal
        self.likeliness = 0

    def add_query(self,):
        print("Welcome to Query Builder. Please answer the following questions!")
        self.queries.append(Query(input("Does correct answer advance the goal?"),
                                input("What is your query?"),
                                input("What is the correct answer?")))

    def calculate_likelihood(self):
        self.likeliness = 0
        for query in self.queries:
            if not query.ask():
                self.likeliness += 100/len(self.queries)
            print(self.likeliness)

    def expert_system(self):
        if self.likeliness == 100:
            print("It is", self.goal)

        else:
            print("It isn't",self.goal)

    def statistic_system(self):
       if self.likeliness < 50:
           print(self.goal, "is not met at a",self.likeliness,"% likeliness")
       else:
           print(self.goal, "is met at a", self.likeliness, "% likeliness")