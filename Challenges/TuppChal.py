
# Stacks
# List = [] ordered and changeable. Duplicates OK
# Set  = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple= () ordered and unchangeable. Duplicates OK. FASTER


# Can have duplicate items
tpp = (
    "ApplePy",
    "Pandas",
    "Requests",
    "FastAPI",
    "Pandas"
)
print("====================================")
for item in tpp:
    print(item)

print("====================================")

print (tpp[0])
# range slicing
print (tpp[2:4])
# every second
print (tpp[0::2]) 
# backwards
print (tpp[:-1])

# Info
# print(dir(tpp))
# print(help(tpp))

print(type(tpp))
print("len(tpp): ", len(tpp))
print("Pandas count: ", tpp.count("Pandas"))
print("tpp.index('Pandas'): ", tpp.index("Pandas"))
print("Lotus in tpp: ", "Lotus" in tpp)
print("Pandas in tpp: ", "Pandas" in tpp)

# will not work !!! tuple is immutable
# tpp.add("8N8") this will error
# tpp.remove("ApplePy")
# tpp.pop() 
# tpp.clear() 


print("====================================")
for item in tpp:
    print(item)

print("====================================")