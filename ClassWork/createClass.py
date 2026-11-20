class PersonalityProfile:
    def __init__(self, name="No Name Provided", personality_type="Unspecified",
                 strengths="", challenges=""):
        # Define the attributes of the class.
        self.name = name
        self.personality_type = personality_type
        self.strengths = strengths
        self.challenges = challenges

    # Define the methods of the class.
    def analyze(self):
        return (
            f"Personality analysis for {self.name}\n"
            f"Personality type: {self.personality_type}\n"
            f"Strengths: {self.strengths}\n"
            f"Challenges: {self.challenges}"
        )

    # Adding r before ''' tells Python not to interpret backslashes as escape sequences.
    notes = r'''
    !s — Calls str(value) to produce a human-readable string representation.
    !r — Calls repr(value) to produce an unambiguous/developer-friendly representation
            (quoting strings and escaping special characters).
    !a — Calls ascii(value) to return a pure-ASCII string
            using repr() escapes (\x, \u, \U) for non-ASCII characters.
    '''

    def __str__(self):
        return f"{self.name}: {self.personality_type}"

    def __repr__(self):
        return (
            f"PersonalityProfile(name={self.name!r}, "
            f"personality_type={self.personality_type!r}, "
            f"strengths={self.strengths!r}, challenges={self.challenges!r})"
        )


# Outside the class, create an instance with illustrative personality traits.
new_profile = PersonalityProfile(
    "John Doe",
    "Introvert",
    "Thoughtful reflection, focused independent work, and attentive listening",
    "Speaking up in large groups and managing social fatigue",
)
print(new_profile.analyze())
