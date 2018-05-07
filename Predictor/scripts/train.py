#from Predictor.models.objects.brain import Brain

def train():
    #brain = Brain()
    training_passengers = Passenger.objects.filter(passenger_type=0)
    if len(training_passengers) > 0:
        pass
    else: 
        pass
        # raise some sort of error
