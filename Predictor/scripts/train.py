from Predictor.models.objects.brain import Brain
from Predictor.models.passenger import Passenger

def train():
    brain = Brain()
    brain.clear()
    brain.initialize_attrs()
    training_passengers = Passenger.objects.filter(passenger_type=0)
    if len(training_passengers) > 0:
        for passenger in training_passengers:
            brain.calculate_passenger(passenger)
            print(f"Trained {passenger.passenger_name} --- survived: {bool(passenger.survived)}")
        print("Pushing Queue ................")
        brain.push_queue()
        print("Deleting Graph Instances ..........................................")
        brain.prune()
        print("DONE")
    else: 
        print("ERROR: No Passengers initialized")
        print("run 'python manage.py import' to train")
