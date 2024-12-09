from pomegranate import *
#transition model
Rain0 = DiscreteDistribution({'y':0.5, 'n':0.5}) #probabilità che piova o non piova

Rain1 = ConditionallyProbabilityTable(    #probabilità condizionate
    [['y', 'y', 0.7],
     ['y', 'n', 0.3],
     ['y', 'y', 0.3],
     ['y', 'y', 0.7]], [Rain0])

Rain2 = ConditionallyProbabilityTable(
    [['y', 'y', 0.7],
     ['y', 'n', 0.3],
     ['y', 'y', 0.3],
     ['y', 'y', 0.7]], [Rain1])

#Sensor Model
Umbrella1 = ConditionallyProbabilityTable(    #probabilità condizionate
    [['y', 'y', 0.9],
     ['y', 'n', 0.1],
     ['y', 'y', 0.2],
     ['y', 'y', 0.8]], [Rain1])

Umbrella2 = ConditionallyProbabilityTable(
    [['y', 'y', 0.9],
     ['y', 'n', 0.1],
     ['y', 'y', 0.2],
     ['y', 'y', 0.8]], [Rain2])
