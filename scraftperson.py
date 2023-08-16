class Spacecraft:
    def _init_(self, x, y, z, direction):
        self.position = [x, y, z]
        self.direction = direction

    def move_forward(self):
        if self.direction == "N":
            self.position[1] += 1
        elif self.direction == "S":
            self.position[1] -= 1
        elif self.direction == "E":
            self.position[0] += 1
        elif self.direction == "W":
            self.position[0] -= 1
        elif self.direction == "Up":
            self.position[2] += 1
        elif self.direction == "Down":
            self.position[2] -= 1

    def move_backward(self):
        if self.direction == "N":
            self.position[1] -= 1
        elif self.direction == "S":
            self.position[1] += 1
        elif self.direction == "E":
            self.position[0] -= 1
        elif self.direction == "W":
            self.position[0] += 1
        elif self.direction == "Up":
            self.position[2] -= 1
        elif self.direction == "Down":
            self.position[2] += 1

    # Implement other methods similarly

# Example usage
if _name_ == "_main_":
    commands = ["f", "r", "u", "b", "l"]
    starting_position = [0, 0, 0]
    initial_direction = "N"

    spacecraft = Spacecraft(starting_position[0], starting_position[1], starting_position[2], initial_direction)

    for command in commands:
        if command == "f":
            spacecraft.move_forward()
        elif command == "b":
            spacecraft.move_backward()
        elif command == "l":
            spacecraft.turn_left()
        elif command == "r":
            spacecraft.turn_right()
        elif command == "u":
            spacecraft.turn_up()
        elif command == "d":
            spacecraft.turn_down()

    final_position = tuple(spacecraft.position)
    final_direction = spacecraft.direction

    print("Final Position:", final_position)
    print("Final Direction:", final_direction)