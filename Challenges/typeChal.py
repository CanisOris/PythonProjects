

class PersonalityType:
    #  PersonalityType.describe = describe the personality type
    #  Returns a string with the class name, title, and functions
    def describe(self):
        # convert the list into comma-separated strings
        functions = ", ".join(self.functions)
        # return the class name as string and the title along with functions
        return f"{type(self).__name__} ({self.title}) - {functions}"


class INTJ(PersonalityType):
    title = 'Architect'
    functions = ('Ni', 'Te', 'Fi', 'Se')


class INTP(PersonalityType):
    title = 'Logician'
    functions = ('Ti', 'Ne', 'Si', 'Fe')


class ENTJ(PersonalityType):
    title = 'Commander'
    functions = ('Te', 'Ni', 'Se', 'Fi')


class ENTP(PersonalityType):
    title = 'Debater'
    functions = ('Ne', 'Ti', 'Fe', 'Si')


class INFJ(PersonalityType):
    title = 'Advocate'
    functions = ('Ni', 'Fe', 'Ti', 'Se')


class INFP(PersonalityType):
    title = 'Mediator'
    functions = ('Fi', 'Ne', 'Si', 'Te')


class ENFJ(PersonalityType):
    title = 'Protagonist'
    functions = ('Fe', 'Ni', 'Se', 'Ti')


class ENFP(PersonalityType):
    title = 'Campaigner'
    functions = ('Ne', 'Fi', 'Te', 'Si')


class ISTJ(PersonalityType):
    title = 'Logistician'
    functions = ('Si', 'Te', 'Fi', 'Ne')


class ISFJ(PersonalityType):
    title = 'Defender'
    functions = ('Si', 'Fe', 'Ti', 'Ne')


class ESTJ(PersonalityType):
    title = 'Executive'
    functions = ('Te', 'Si', 'Ne', 'Fi')


class ESFJ(PersonalityType):
    title = 'Consul'
    functions = ('Fe', 'Si', 'Ne', 'Ti')


class ISTP(PersonalityType):
    title = 'Virtuoso'
    functions = ('Ti', 'Se', 'Ni', 'Fe')


class ISFP(PersonalityType):
    title = 'Adventurer'
    functions = ('Fi', 'Se', 'Ni', 'Te')


class ESTP(PersonalityType):
    title = 'Entrepreneur'
    functions = ('Se', 'Ti', 'Fe', 'Ni')


class ESFP(PersonalityType):
    title = 'Entertainer'
    functions = ('Se', 'Fi', 'Te', 'Ni')

# Group by type
def describe_personality(item):
    match item:
        case INTJ() | INTP() | ENTJ() | ENTP():
            return f"Analyst: {item.describe()}"
        case INFJ() | INFP() | ENFJ() | ENFP():
            return f"Diplomat: {item.describe()}"
        case ISTJ() | ISFJ() | ESTJ() | ESFJ():
            return f"Sentinel: {item.describe()}"
        case ISTP() | ISFP() | ESTP() | ESFP():
            return f"Explorer: {item.describe()}"
        case _:
            return f"Unknown personality type: {type(item).__name__}"


# Test is running from this file, if so run this stock data
if __name__ == "__main__":
    # Pass in the objects
    incoming_stream = [
        INTJ(), INTP(), ENTJ(), ENTP(),
        INFJ(), INFP(), ENFJ(), ENFP(),
        ISTJ(), ISFJ(), ESTJ(), ESFJ(),
        ISTP(), ISFP(), ESTP(), ESFP(),
    ]
    # incoming_stream = [
    #         INTJ(), INTP(), ENTJ(), ENTP(),
    #         INFJ(), INFP(), ENFJ(), ENFP()
    #     ]
    # incoming_stream = [
    #             INFJ()
    #         ]

    
    for item in incoming_stream:
        print(describe_personality(item))
