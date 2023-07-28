# 08 March 2022
# Mad Lib
import random 

n= input("Hello, please state 4 nouns, seperated by space: ")
noun_list = n.split()

v = input("Please state 4 verbs, seperated by space: ")
verb_list = v.split()

adj = input("Please state 5 adjectives, seperated by space: ")
adj_list = adj.split()


story = "I will remember that day... it was my dad's last day. He was diagnosed with an incurable disease. So he'll try enjoying his life for the last time.\
 My dad went to the mall with {} and a {} {}. There, he bought a {}. After that he went to a {} gym to {} and {}.\
 After going to the gym, he decided to go to a bar and get {}. He went home quite {} and head straight to {} {}. He said it was the {}\
 day of his life because it was the first time he felt life in many years. He then slept {} for the last time."

print(story.format(noun_list[random.randint(0,3)],
                   adj_list[random.randint(0,4)],
                   noun_list[random.randint(0,3)],
                   noun_list[random.randint(0,3)],
                   adj_list[random.randint(0,4)],
                   verb_list[random.randint(0,3)],
                   verb_list[random.randint(0,3)],
                   verb_list[random.randint(0,3)],
                   adj_list[random.randint(0,4)],
                   verb_list[random.randint(0,3)],
                   noun_list[random.randint(0,3)],
                   adj_list[random.randint(0,4)],
                   adj_list[random.randint(0,4)]))
