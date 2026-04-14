from datetime import datetime
import random
NAME = "Brandon Lee"
Course_Name = "Programming for Technology Professionals - KU_JAX_COP1034CD4-104062026"
Instructor_Name = "Professor Mora"
Assignment_Name = "Week 2 - Assignment #3"
currenttime = datetime.now()

print("====================================")
print(f"Name: {NAME}")
print(f"Course: {Course_Name}")
print("-------------------------------------")
print(f"Instructor: {Instructor_Name}")
print(f"Assignment: {Assignment_Name}")
print("-------------------------------------")
print(f"Current Time: {currenttime}")
print("====================================")


def magic8ball(question, responses=None):
    if responses is None:
        responses = [
            "Yes, of course!",
            "Without a doubt, yes.",
            "You can count on it.",
            "For sure!",
            "Ask me later.",
            "I am not sure.",
            "I can not tell you right now.",
            "I will tell you after my nap.",
            "No way!",
            "I do not think so.",
            "Without a doubt, no.",
            "The answer is clearly NO"
        ]
    if isinstance(responses, str):
        responses = [r.strip() for r in responses.split("|") if r.strip()]
    if not responses:
        raise ValueError("No responses provided.")
    return random.choice(responses)

if __name__ == "__main__":
    question = input("Ask the Magic 8-Ball a question: ")
    print(magic8ball(question))