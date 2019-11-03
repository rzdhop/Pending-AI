#Coding: UTF-8
#Gradiant descent
import numpy as np

class neurone():
    def __init__(self, inputs):
        self.actualOutput = 0
        self.error = 0
        self.learningRate = 0.1
        self.weightBies = 2 * np.random.random((1, 1)) - 1
        self.biesValue = np.array([1])
        self.input = np.append(inputs, self.biesValue)
        self.weight = np.append(2 * np.random.random((1, 2)) - 1, self.weightBies, axis=1)
        print(self.input, chr(0xa),self.weight)
    def guess(self):
        self.actualOutput = self.activationFunction(np.dot(self.input.T, self.weight.T))
    def activationFunction(self, output):
        return output # (1-np.exp(-2*output)) // (1 + np.exp(-2*output) ## tangeate hyperbolique function 
    def Improve(self):
        for weight in self.weight:
            for input in self.input:
                weight += self.error * input * self.learningRate
                print(self.weight, "-----", self.actualOutput)

if __name__ == "__main__":
    firstInput = np.array([0, 0])
    goal = 999
    myNeurone = neurone(inputs=firstInput)
    for training in range(100):
        myNeurone.guess()
        myNeurone.error = goal - myNeurone.actualOutput
        myNeurone.Improve()
        
    print(chr(0xa), "final output :", myNeurone.actualOutput, chr(0xa), "final weight :", myNeurone.weight, chr(0xa), "final error :", myNeurone.error, chr(0xa))
