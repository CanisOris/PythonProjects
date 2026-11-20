
class Profile:
    # Parent 
    name = "Test Group 12"
    desc = "Personality Profile Set 12"

    # def __init__(self, name="Test Group 12"):
    #     self.name = name
    #     self.desc = self.desc

class Traits(Profile):
    # Child class that inherits from Profile
    name = "Test Group 12 - Traits"
    desc = "Personality Profile Set 12 - Traits - 74"

    # def __init__(self, name="No Name Provided"):
    #     # get the parent class's initializer
    #     super().__init__(name)

class Demographics(Profile):
    # Child class that inherits from Profile
    name = "Test Group 12 - Demographics"
    desc = "Personality Profile Set 12 - Demographics(std)"
