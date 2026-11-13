subdivisions_dict = {
    "Introversion": {"code": "I", "preference": "Internal"},
    "Extraversion": {"code": "E", "preference": "External"},
    "Sensing": {"code": "S", "preference": "Concrete"},
    "Intuition": {"code": "N", "preference": "Abstract"},
    "Thinking": {"code": "T", "preference": "Logic"},
    "Feeling": {"code": "F", "preference": "Values"},
    "Judging": {"code": "J", "preference": "Structure"},
    "Perceiving": {"code": "P", "preference": "Flexible"}
}

test_info = {
    "name": "Myers-Briggs Type Indicator",
    "abbreviation": "MBTI",
    "category": "Typology",
    "popular": True,
    "typeclassifica"
    "subdivisions": subdivisions_dict,
    "myrating": 7
}




print(test_info)
# NOTE: .get() fails gracefully like c# get param 
category = test_info.get("category")
print("Category: ", category)
# will fail
inventor = test_info.get("inventor")
print("Inventor: ", inventor)
# fail default 
cost = test_info.get("cost", "Free / Varies")
print("Cost: ", cost)

# ARE YOU THE KEY MASTER?
# Test if key exists in the dictionary
if "category" in test_info:
    print("Category exists:", test_info["category"])
else:
    print("Category key does not exist.")
# using try
try:
    print(test_info["kategory"])
except KeyError:
    print("The kategory key does not exist!")    
# Test if key is missing from the dictionary
if "inventor" not in test_info:
    print("Inventor is missing from the dictionary.")

# Update it
if "myrating" in test_info:
    test_info["myrating"] = 9

print(test_info)


# Create a blank scoring sheet
trait_keys = subdivisions_dict.keys()
scoring_sheet = dict.fromkeys(trait_keys, 0)

print("\nBlank Scoring Sheet created with fromkeys():")
print(scoring_sheet)