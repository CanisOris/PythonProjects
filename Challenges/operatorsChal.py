# Challenge 1

var0 = ("hello").upper()
var1 = "x"
var2 = "a"
var3 = "welcome to the jungle"
var4 = var3[0:8] 
var5 = var3[8:] 
var6 = len(var3)

print("\n1-4")
print("{} {} {}, \n\t {}{}".format(var0, var1, var2, var4, var5))
print("len = {}".format(var6))

if ("welcome" in var3):
    print("\ncase matters in compare!")
else:
    print("\ncase does not matter in compare!")


# Operators Challenge
# print("{}".format(var1))
m1 = 9
m2 = 1
m3 = m1 + m2
print("1- {}".format(m3))
m3 += 24
print("2- {}".format(m3))
if ((m1 * 3) >= (m3 - 8) ): print("max reached") 

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a
print("\n5.")
print("list_a == list_b",format((list_a == list_b))) 
print("list_a is list_b",format((list_a is list_b)))
print("list_a is list_b",format((list_a is list_c)))
print("\n6.")
print("\"jungle\" in var3",format(("jungle" in var3)))

print("\n7.")
# abin = 42
# bina = bin(abin)
# # binaStr = f"{bina:08b}"
# print (format(bina,"08b"))
# result = bina << 2
# print (format(bina,"08b"))

abin = 42
print(format(abin, "08b"))    

result = abin << 2
# 3.6 f-string
# This one took a while to get :)
print(f"{result:08b} = {result}")