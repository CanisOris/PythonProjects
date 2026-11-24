from abc import ABC, abstractmethod
#

# Abstract base class 
class WarehouseStation(ABC):
    # note: '->' None = action that does not return a value
    def __init__(self, station_id: str) -> None:
        # Store the unique identifier for this station
        self.station_id = station_id

    # Regular method: shared behavior inherited by child classes
    def log_status(self, message: str) -> None:
        print(f"[{self.station_id}] {message}")

    # Abstract method: every child station must define how it processes an item
    @abstractmethod
    def process_item(self, item_sku: str) -> None:
        pass

    @abstractmethod
    def process_store(self, item_sku: str) -> None:
        pass


# Child class for a packing station
class PackingStation(WarehouseStation):
    # implementation of abstract method 
    
    def process_store(self, item_sku: str) -> None:
        print(f"Storing item '{item_sku}' in the warehouse.")

    def process_item(self, item_sku: str) -> None:
        print(f"Packing item '{item_sku}' into a shipping box.")


if __name__ == "__main__":
    # Create an object of the child class
    packing_station_1 = PackingStation("PACK-01")

    # Use the regular method inherited from the parent class
    packing_station_1.log_status("Station online and ready.")

    # abstract methods
    packing_station_1.process_store("SKU-4098")
    packing_station_1.process_item("SKU-4098")

    # Use the parent's regular method again after processing
    packing_station_1.log_status("Completed item SKU-4098.")