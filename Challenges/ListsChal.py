
# Stacks
# List = [] ordered and changeable. Duplicates OK
# Set  = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple= () ordered and unchangeable. Duplicates OK. FASTER


personality_tests = [
    "Myers-Briggs Type Indicator (MBTI)",
    "Big Five Personality Traits (OCEAN)",
    "Enneagram",
    "Minnesota Multiphasic Personality Inventory (MMPI)",
    "DiSC Assessment",
    "16 Personality Factor Questionnaire (16PF)",
    "CliftonStrengths (StrengthsFinder)",
    "Keirsey Temperament Sorter"
]

# INDEX OPERATORS #############################################################
# Works with collects like it does strings

# [0]INFJ :)
print (personality_tests[0])
# 4th-5th
print (personality_tests[4:5])
# every second
print (personality_tests[0::2]) 
# backwards
print (personality_tests[:-1])


# length of list divided and round to int
mid = len(personality_tests) //2

# get part of the list
# start to mid
first_half = personality_tests[:mid]
first_half.append("Hogan Personality Inventory (HPI)")
first_half.append("Strengths Profile")

for item in first_half:
    first_half.append(item)

# end to mid
second_half = personality_tests[mid:]
second_half_rev = list(reversed(second_half)) 

print("Second half:", second_half)
print("Second half Rev:", second_half_rev)

# concatenates lists
first_half.extend(second_half)
print(first_half)


p_ack = ["MBTI", "Enneagram", "DiSC"]

# copy - note: shallow copy (.copy(), [:], list(varList))
# copy.deepcopy() for deep
p_ack_cp = p_ack.copy()
p_ack.extend(p_ack_cp)


# Remove
# p_ack.remove("Enneagram")
# did it remove 2?  no it did not
# you have to loop each item but the suggested way it to do it on one line
p_ack = [item for item in p_ack if item != "Enneagram"]

print(p_ack)

print(dir(p_ack))





