
# list of dictionaries 
personality_tests = [
    {'name': 'MBTI', 'category': 'Jungian', 'questions': 93},
    {'name': 'Big Five', 'category': 'Trait-based', 'questions': 50},
    {'name': 'Enneagram', 'category': 'Typology', 'questions': 105},
    {'name': 'DiSC', 'category': 'Behavioral', 'questions': 28},
    {'name': 'HEXACO', 'category': 'Trait-based', 'questions': 100}
]


# using filter
# Use filter to find only the tests that are "Trait-based"
# The lambda looks at each dictionary (t) and checks its category
trait_tests = list(filter(lambda t: t['category'] == 'Trait-based', personality_tests))

print("Trait-based tests:")
for test in trait_tests:
    print(f" - {test['name']}")
    



# using map
# Use map to extract the names of all tests
test_names = list(map(lambda t: t['name'], personality_tests))

print("\nAll test names:")
for name in test_names:
    print(f" - {name}")

