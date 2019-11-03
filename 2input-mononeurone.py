#Coding: UTF-8
#Gradiant descent
import numpy as np
from math import tanh

class neurone():
    def __init__(self, inputs):
        self.actualOutput = 0
        self.error = 0
        self.learningRate = 0.1
        self.biesValue = np.array([1])
        self.input = np.append(inputs, self.biesValue)
        self.weight = 2 * np.random.random((1, 3)) - 1
    def guess(self):
        self.actualOutput = self.activationFunction(np.dot(self.input.T, self.weight.T))
    def activationFunction(self, output):
        return output #tanh() for tangeante hyperbolique
    def Improve(self):
        for weight in self.weight:
            for input in self.input:
                weight += self.error * input * self.learningRate
                print(self.weight, "-----", self.actualOutput)

if __name__ == "__main__":
    firstInput = np.array([0, 0])
    goal = 999
    myNeurone = neurone(inputs=firstInput)
    for training in range(1000):
        myNeurone.guess()
        myNeurone.error = goal - myNeurone.actualOutput
        myNeurone.Improve()
        
    print(chr(0xa), "final output :", myNeurone.actualOutput, chr(0xa), "final weight :", myNeurone.weight, chr(0xa), "final error :", myNeurone.error, chr(0xa))
