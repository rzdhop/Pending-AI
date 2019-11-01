#Coding: UTF-8
#Gradiant descent
import numpy as np
from math import tanh

class neurone():
    def __init__(self, inputs):
        self.input = inputs
        self.weight = 2 * np.random.random((1, 2)) - 1
        self.actualOutput = 0
        self.error = 0
        self.learningRate = 0.1

    def guess(self):
        self.actualOutput = self.activationFunction(np.dot(self.input.T, self.weight.T))
    def activationFunction(self, output):
        return tanh(output)
    def Improve(self):
        for weight in self.weight:
            for input in self.input:
                weight += self.error * input * self.learningRate
                print(weight, "-----", self.actualOutput)

if __name__ == "__main__":
    firstInput = np.array([1.35435, 1.333333])
    goal = 0.497182570654321
    myNeurone = neurone(inputs=firstInput)
    for training in range(10000):
        myNeurone.guess()
        myNeurone.error = goal - myNeurone.actualOutput
        myNeurone.Improve()
        
    print(f"\n--[{myNeurone.actualOutput}, {myNeurone.weight}, {myNeurone.error}]--\n")

    print("final output :", myNeurone.actualOutput, chr(0xa), "final weight :", myNeurone.weight)





