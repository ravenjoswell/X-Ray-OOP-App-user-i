class User():
        def __init__(self, name, email = None, drivers_licence = None, number = None):
            self.name = name
            self.email = email
            self.drivers_license = drivers_licence
            self.number = number 
        

        def __str__(self):
             return f"{self.name} | {self.email} | {self.drivers_license} | {self.number} "



 