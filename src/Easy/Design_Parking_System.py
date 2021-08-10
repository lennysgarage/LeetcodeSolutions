class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space = [0] * 3
        self.space[0] = big
        self.space[1] = medium
        self.space[2] = small

    def addCar(self, carType: int) -> bool:
        roomLeft = self.space[carType-1]
        if roomLeft > 0:
            self.space[carType-1] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)