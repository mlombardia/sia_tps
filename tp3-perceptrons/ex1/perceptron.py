import numpy as np


class SimplePerceptron():
    # hago el init con el set de training, el de valores esperados, como pondero el error y la cantidad de iteraciones,
    # y genero random los pesos
    def __init__(self, training_set, expected_set, error_ponderation=0.25, iterations_qty=1000):
        self.training_set = np.array(training_set)
        self.expected_set = expected_set
        self.error_ponderation = error_ponderation
        self.iterations_qty = iterations_qty
        self.weights = np.array(np.random.rand(len(training_set[0]) + 1))

    def activation_function(self, x):
        if x >= 0:
            return 1
        return -1

    def predict(self, a_input):
        dot_product = self.weights.T.dot(a_input)
        return self.activation_function(dot_product)

    def train(self):
        for _ in range(self.iterations_qty):
            for training_row, expected_row in zip(self.training_set, self.expected_set):
                biased_input = np.insert(training_row, 0, 1)
                predicted_value = self.predict(biased_input)
                error = expected_row - predicted_value
                self.weights = self.weights + self.error_ponderation * error * biased_input

        print("weights: ", self.weights)

    def guess(self, a_input):
        return self.predict(np.insert(a_input, 0, 1))
