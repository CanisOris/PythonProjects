
def getInfo():
    var1 = input("\nWhat is your favorite number? ")
    var2 = input("\nWhat is your second favorite number? ")
    return var1,var2



def compute():
    go = True
    while go:
        # returns and load 
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print(f"\nInput Invalid: {e}")
        except:    
            print("\nExiting ....")
            return
    print(f"\n\t{var1} + {var2} = {var3}\n")


    # finally:
    #     print("Computation finished.")
    
  




if __name__ == "__main__":
    compute()
