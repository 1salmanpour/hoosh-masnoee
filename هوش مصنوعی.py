class Elevator:
    def __init__(self, floors):
        self.current_floor = 0
        self.requests = []  # List of requested floors
        self.floors = floors
        self.direction = "idle"  # Can be 'up', 'down', or 'idle'

    def request_floor(self, floor):
        if 0 <= floor < self.floors and floor not in self.requests:
            self.requests.append(floor)
            self.requests.sort()  # Keep requests sorted for simplicity

    def move(self):
        if not self.requests:
            self.direction = "idle"
            return "Elevator is idle."

        # Determine direction
        if self.current_floor < self.requests[0]:
            self.direction = "up"
        elif self.current_floor > self.requests[0]:
            self.direction = "down"

        # Move elevator
        if self.direction == "up":
            self.current_floor += 1
        elif self.direction == "down":
            self.current_floor -= 1

        # Check if we've reached the target floor
        if self.current_floor == self.requests[0]:
            self.requests.pop(0)

        return f"Elevator is on floor {self.current_floor}, moving {self.direction}."

# Example usage
elevator = Elevator(floors=10)

# Request some floors
elevator.request_floor(3)
elevator.request_floor(7)
elevator.request_floor(1)

# Simulate elevator movement
for _ in range(15):  # Run a number of steps
    print(elevator.move())
