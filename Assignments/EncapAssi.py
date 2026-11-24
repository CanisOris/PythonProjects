class GumballMachine:
    # gumball machine whos stock an cash are encapsulated
    def __init__(self, gumballs: int = 0, price: float = 0.25):
        self.price = price
        # __private var for gumballs and cash box
        self.__gumballs = max(0, gumballs)
        self.__cash_box = 0.0
        self._jammed = False

    #Protected helper method
    # clear jam action return none
    def _clear_jam(self) -> None:
        # Reset internal jam flag so the dispensing mechanism can operate again
        self._jammed = False    

    # buy a gumball
    def insert_coin_and_turn(self, payment: float) -> str:
        if self._jammed:
            return "Machine is jammed!"
        if self.__gumballs <= 0:
            return "Out of gumballs!"
        if payment < self.price:
            return f"Need at least ${self.price:.2f} (got ${payment:.2f})."

        self.__gumballs -= 1
        self.__cash_box += self.price
        change = round(payment - self.price, 2)
        # return any change to the customer
        if change > 0:
            # return the change amount to the customer
            return f"Dispensed 1 gumball! Change: ${change:.2f}"
        return "Dispensed 1 gumball!"

    # add gumballs to the machine
    def refill(self, count: int) -> None:
        if count <= 0:
            raise ValueError("Refill count must be positive.")
        self.__gumballs += count

    # collect cash from the machine
    def collect_cash(self) -> float:
        collected = self.__cash_box
        self.__cash_box = 0.0
        return collected

    def service_machine(self) -> None:
        self._clear_jam()
        print("Machine serviced.")

    # show the number of gumballs remaining (read-only)
    @property
    def gumballs_remaining(self) -> int:
        """Read-only view of current gumball count."""
        return self.__gumballs


machine = GumballMachine(gumballs=3, price=0.50)
print(machine.insert_coin_and_turn(0.50))
# Simulate a jam
machine._jammed = True
print(machine.insert_coin_and_turn(1.00))  
print(machine.gumballs_remaining)           

# Clear the jam and refill the machine
machine.service_machine()
machine.refill(5)
print(machine.gumballs_remaining)           
print(f"Collected: ${machine.collect_cash():.2f}")  

# Bypassing __gumballs directly does not alter the internal mangled attribute
machine.__gumballs = 500
print(machine.gumballs_remaining)           