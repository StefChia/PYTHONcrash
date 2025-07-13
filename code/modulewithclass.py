class Car:
    """Represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Returns a neatly formatted string name syinthesis."""
        n = f'{self.make} {self.model} {self.year}'
        return n.title()

    def read_odometer(self):
        """Print a statement showing the car mileage."""
        print(f'The car mileage is: {self.odometer_reading} KM')
    
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll the odometer back!')
    def increment_odometer(self,miles):
        """Add a number of miles run to the odometer record.
        The number has to be positive."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You cannot roll odometer back!')