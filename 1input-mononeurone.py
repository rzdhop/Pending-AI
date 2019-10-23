#Coding: UTF-8
import numpy as np

class neurone():
    def __init__(self, input, weight):
        self.input = input
        self.weight = weight
def SigmoidFunction(value):
    return 1 / (1 + np.exp(-value))
def SigmoidDerivate(value):
    return value * (1 - value)

#try with more inputs
if __name__ == "__main__":
    firstInput = int(input("Enter first input: "))
    goal = int(input("Enter goal number: "))
    firstWeight = 2 * np.random.random((1, 1)) -1
    myNeurone = neurone(input=firstInput, weight=firstWeight)

    for training in range(500000):
        actualOutput = SigmoidFunction(myNeurone.input * myNeurone.weight)
        errorRange = goal - actualOutput
        deltaW =  myNeurone.input * errorRange * SigmoidDerivate(actualOutput)
        myNeurone.weight += deltaW

    print("final output :", actualOutput, chr(0xa), "final weight :", myNeurone.weight)





