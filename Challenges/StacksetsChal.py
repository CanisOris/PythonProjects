
# Stacks
# List = [] ordered and changeable. Duplicates OK
# Set  = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple= () ordered and unchangeable. Duplicates OK. FASTER

tpp = {
    "ApplePy",
    "Pandas",
    "Requests",
    "FastAPI"
}

upp = {
    "ApplePy",
    "Pandas",
    "Requests",
    "Crystal",
    "isoAi"
}
print("====================================")
for item in tpp:
    print(item)

print("====================================")
diff_set = tpp.difference(upp)
print("Difference between tpp and upp: ", diff_set)
intersect_set = tpp.intersection(upp)
print("Intersection between tpp and upp: ", intersect_set)
union_set = tpp.union(upp)
print("Union of tpp and upp: ", union_set)  
print("====================================")


# Not available for sets, as they are 
# unordered and do not support indexing or slicing.
# print (tpp[0]) 
# range slicing
# print (tpp[2:4])
# every second
# print (tpp[0::2]) 
# backwards
# print (tpp[:-1])

# Info
# print(dir(tpp))
# print(help(tpp))

print(type(tpp))
print("len(tpp): ", len(tpp))
# Not Available for sets, as they do not support counting specific elements.
# print("Pandas count: ", tpp.count("Pandas"))
# Not Available for sets, as they do not support indexing.
# print("tpp.index('Pandas'): ", tpp.index("Pandas"))
print("Lotus in tpp: ", "Lotus" in tpp)
print("Pandas in tpp: ", "Pandas" in tpp)
# tpp.pop() remove firs item will work but it is random order

# tpp[0] - no index access will error
for item in tpp:
    print(item)


