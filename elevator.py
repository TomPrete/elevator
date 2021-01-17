class Elevator:
    def __init__(self, floors, current_floor, direction):
        self.direction = direction
        self.floors = floors
        self.current_floor = current_floor
        self.upper_floors = []
        self.down_floors = []

    def elevator_moving(self, *args):
        
        if len(args) == 0:
            self.direction = "waiting_time"
            return self.direction
        print("your current floor", self.current_floor)
       


        for desired_floor in args:
            if desired_floor < self.current_floor:
                self.down_floors.append(desired_floor)
            elif desired_floor > self.current_floor:
                self.upper_floors.append(desired_floor)


        self.upper_floors.sort()
        self.down_floors.sort(reverse = True)
        print(self.upper_floors)
        print(self.down_floors)

        if self.direction == "up":
            for floor in self.upper_floors[:]:

                while floor != self.current_floor:   
                    self.move_up()
            
                self.open()
                print(floor)
                print(self.upper_floors.pop(0))
                
                # self.elevator_moving(input())
                
                

        self.direction = "down"
        print("Elevator goes down") 

        if self.direction == "down":
            for floor in self.down_floors[:]:

                while floor != self.current_floor:   
                    self.move_down()
            
                self.open()
                print(floor)
                self.down_floors.remove(floor)

        self.direction = "up"
        print("Elevator goes up")  

            

    def move_up(self):
        self.current_floor += 1

    def move_down(self):
        self.current_floor -= 1

    def open(self):
        print("You are here")

    def close(self):
        pass

    def stop(self):
        pass

    def current_floor(self, given_time):
        pass

elevator = Elevator(15, 5, "up")
print(elevator.elevator_moving(1,2,4,5,6,7))  