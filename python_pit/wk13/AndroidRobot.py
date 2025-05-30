class AndroidRobot:
    def __init__(self, name, model, battery_level, status):
        #When intialising the robot you need the 4 parameters above (name, model, battery_level, status)
        self.name = name
        self.model = model
        self.battery_level = battery_level  # percentage (0-100)
        self.status = status  # "idle", "working", "charging", "offline" or "destroyed"
        
    def charge(self, amount):
        """Charge the battery by a certain amount."""
        if self.status == "destroyed":
            return
        self.battery_level = min(100, self.battery_level + amount)
        self.status = "charging"
        print(f"{self.name} is charging. Battery level: {self.battery_level}%")

    def work(self, task):
        """Perform a task and reduce battery level."""
        if self.status == "destroyed" or "offline":
            return
        if self.battery_level >= 10:
            self.battery_level -= 10
            self.status = "working"
            print(f"{self.name} is performing task: {task}")
        else:
            print(f"{self.name} has low battery. Please charge.")

    def report_status(self):
        """Print the current status and battery level."""
        print(f"Name: {self.name}, Model: {self.model} Status: {self.status}, Battery: {self.battery_level}%")
        
    def self_destruct(self):
        """The Robot will self destruct"""
        if self.status == "destroyed":
            return
        print(f"{self.name}'s time has come, goodbye cruel world")
        print("Android has been destroyed.")
        self.status = "destroyed"
    
    def power_on(self):
        if self.status == "destroyed":
            return
        
        if self.status == "offline":
            self.status = "idle"
            print(f"{self.name} is now on and ready to receive instructions.")
        else:
            print(f"{self.name} is already on.")
            

    def shut_down(self):
        """Shut down the robot."""
        if self.status == "destroyed":
            return
        
        if self.status == "offline":
            print(f"{self.name} is already offline.")
        else:
            self.status = "offline"
            print(f"{self.name} is now shut down.")