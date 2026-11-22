
# Parent class subject: game theory strategy
class Strategy:
    def __init__(self, name):
        # shared by all strategies
        self.name = name

    # child classes override (polymorphism)
    def choose_move(self, opponent_last_move):
        return "cooperate"


# First child class inheriting from Strategy: Always Cooperate
class AlwaysCooperate(Strategy):
    def __init__(self, name, trust_score, rounds_played):
        # Initialize parent attribute 'name'
        super().__init__(name)
        # 
        self.trust_score = trust_score
        self.rounds_played = rounds_played

    # Polymorphism: overrides choose_move() 
    def choose_move(self, opponent_last_move):
        return "cooperate"


# Second child class inheriting from Strategy: Tit for Tat
class TitForTat(Strategy):
    def __init__(self, name, retaliate_immediately, forgiveness_rate):
        # Initialize parent attribute 'name'
        super().__init__(name)
        # Two attributes unique to TitForTat
        self.retaliate_immediately = retaliate_immediately
        self.forgiveness_rate = forgiveness_rate

    # Polymorphism: overrides choose_move() 
    def choose_move(self, opponent_last_move):
        # Cooperate on the first round if there is no previous move
        if opponent_last_move is None:
            return "cooperate"
        return opponent_last_move




if  __name__ == "__main__":
    # run child strategies
    cooperator = AlwaysCooperate("Saint", 1.0, 10)
    mirror = TitForTat("Reciprocator", True, 0.1)
