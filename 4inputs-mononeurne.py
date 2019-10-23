#Coding: UTF-8
import numpy as np

class neurone():
    def __init__(self, input):
        self.input = input
        self.weight = 2 * np.random.random((3, 1)) -1

def SigmoidFunction(value):
    return 1 / (1 + np.exp(-value))
def SigmoidDerivate(value):
    return value * (1 - value)

if __name__ == "__main__":
    firstInput = np.array([[1, 0, -1], [0, -7, 1], [-1, 0, 1], [2, 0, -4]])
    goal = np.array([0, -6, 0, -2]).T
    myNeurone = neurone(input=firstInput)
    print(firstInput,chr(0x0a) , myNeurone.weight)
    for training in range(50000):
        actualOutput = SigmoidFunction(np.dot(myNeurone.input, myNeurone.weight))
        errorRange = goal - actualOutput
        print(SigmoidDerivate(actualOutput))
        deltaW =  np.dot(myNeurone.input, errorRange * SigmoidDerivate(actualOutput))
        myNeurone.weight += deltaW

    print("final output :",chr(0x0a) , actualOutput, chr(0xa), "final weight :", chr(0x0a), myNeurone.weight)
