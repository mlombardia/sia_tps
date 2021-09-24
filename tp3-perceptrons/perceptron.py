import random
from activationFunctions import *


class SimplePerceptron:
    # hago el init con el set de training, el de valores esperados, como pondero el error y la cantidad de iteraciones,
    # y genero random los pesos
    def __init__(self, input_size, activation_function, der_activation_function, eta=0.25, delta=0.01):
        self.eta = eta
        self.activation_function = activation_function
        self.weights = np.array(np.random.rand(input_size + 1))
        self.der_activation_function = der_activation_function
        self.delta = delta

    def predict_with_biased(self, a_input):
        dot_product = self.weights.T.dot(a_input)
        return self.activation_function(dot_product)

    def predict(self, a_input):
        return self.predict_with_biased(np.insert(a_input, 0, 1))

    def calculate_mean_square_error(self, training_set, expected_set):
        sum = 0
        for i in range(len(training_set)):
            x = training_set[i]
            y = expected_set[i]

            predicted = self.predict(x)
            aux = (predicted - y) ** 2
            sum += aux
        return sum / len(training_set)

    def train(self, training_set, expected_set, error_epsilon=0, iterations_qty=1000, print_data=True):
        errors = []
        epochs = []
        training_accuracies = []
        training_set = np.array(training_set)
        expected_set = np.array(expected_set)
        ii = 0
        shuffled_list = [a for a in range(0, len(training_set))]
        random.shuffle(shuffled_list)
        p = len(training_set)
        Error = 1
        min_error = 2 * p
        while ii < iterations_qty and Error > error_epsilon:
            j = 0
            training_correct_cases = 0
            while j < len(shuffled_list):
                biased_input = np.insert(training_set[shuffled_list[j]], 0, 1)
                predicted_value = self.predict_with_biased(biased_input)
                error = expected_set[shuffled_list[j]] - predicted_value
                if error < self.delta:
                    training_correct_cases += 1
                self.weights = self.weights + (self.eta * error * self.der_activation_function(
                    self.weights.T.dot(biased_input)) * biased_input.T)
                j += 1

            Error = self.calculate_mean_square_error(training_set, expected_set)
            if Error < min_error:
                min_error = Error
            errors.append(Error)
            training_accuracies.append(training_correct_cases/len(training_set))
            if print_data:
                print("Epoch: ", ii)
                print("min error", min_error)
            print("weights: ", self.weights)
            epochs.append(ii)
            ii += 1
        return min_error, epochs, errors, training_accuracies

    def test(self, test_set, expected_test):
        return self.calculate_mean_square_error(test_set, expected_test)


class NeuronLayer:
    def __init__(self, neurons_qty, inputs_per_neuron_qty):
        self.weights = 2 * np.random.random((inputs_per_neuron_qty, neurons_qty)) - 1


class MultiLayerPerceptron:
    def __init__(self, input_size, activation_function, der_activation_function, hidden_layers, output_layer, eta=0.01):
        self.eta = eta
        self.activation_function = activation_function
        self.weights = np.array(np.array(np.random.rand(input_size + 1)))   # aca los pesos son una matriz porque hay mas de una capa
        self.der_activation_function = der_activation_function
        self.hidden_layers = hidden_layers
        self.output_layer = output_layer

    def predict_with_biased(self, a_input, a_layer):
        dot_product = np.dot(a_input, a_layer)
        return self.activation_function(dot_product)

    def predict(self, a_input, a_layer):
        return self.predict_with_biased(np.insert(a_input, 0, 1), a_layer)

    def calculate_mean_square_error(self, training_set, expected_set):
        sum = 0
        for i in range(len(training_set)):
            x = training_set[i]
            y = expected_set[i]

            predicted = self.predict(x)
            aux = (predicted-y)**2
            sum += aux
        return sum / len(training_set)

    def train(self, training_set, expected_set, error_epsilon = 0, iterations_qty=1000, print_data=True):
        errors = []
        Errors = []
        deltas = []
        epochs = []
        outputs = []
        training_set = np.array(training_set)
        expected_set = np.array(expected_set)
        ii = 0
        i = 0
        shuffled_list = [a for a in range(0, len(training_set))]
        random.shuffle(shuffled_list)
        p = len(training_set)
        Error = 1
        min_error = 2 * p
        while ii < iterations_qty and Error > error_epsilon:
            j = 0
            k = 0
            while j < len(training_set):
                # 1 aplico a la capa 0
                biased_input = np.insert(training_set[shuffled_list[j]], 0, 1)
                predicted_value = self.predict_with_biased(biased_input, self.hidden_layers[0].weights)
                error = expected_set[shuffled_list[j]] - predicted_value
                errors.append(error)
                # self.weights[i] = self.weights[i] + (self.eta * error * self.der_activation_function(self.weights[i].T.dot(biased_input)) * biased_input.T)
                outputs.append(predicted_value)

                # 2 forward propagation
                while k < len(self.hidden_layers):
                    biased_input = np.insert(training_set[shuffled_list[j]], 0, 1)
                    predicted_value = self.predict_with_biased(biased_input, self.hidden_layers[k].weights)
                    error = expected_set[shuffled_list[j]] - predicted_value
                    errors.append(error)
                    # self.weights[i] = self.weights[i] + (self.eta * error * self.der_activation_function(self.weights[i].T.dot(biased_input)) * biased_input.T)
                    outputs.append(predicted_value)
                    k += 1

                biased_input = np.insert(training_set[shuffled_list[j]], 0, 1)
                predicted_value = self.predict_with_biased(biased_input, self.output_layer.weights)

                # 3 calaculate delta for output layer

                error = expected_set[shuffled_list[j]] - predicted_value
                # self.weights[i] = self.weights[i] + (self.eta * error * self.der_activation_function(self.weights[i].T.dot(biased_input)) * biased_input.T)
                delta = (self.eta * error * self.der_activation_function(self.weights[i].T.dot(biased_input)) * biased_input.T)
                errors.append(error)
                deltas.append(delta)
                outputs.append(predicted_value)

                # 4 backpropagation between output layer and 2

                aux = 2+len(self.hidden_layers)     # output + input + hidden
                while aux >= 2:
                    delta = (self.eta * errors[k] * self.der_activation_function(self.weights[i].T.dot(biased_input)) * biased_input.T)
                    deltas.append(delta)
                    aux -= 1

                # 5 update weights
                aux = 2 + len(self.hidden_layers)  # output + input + hidden
                for h in range(aux):
                    self.weights[h] = self.weights[h] + self.eta*deltas[h]*biased_input

            # 6 calculate error, if error > epsilon goto 1
            Error = self.calculate_mean_square_error(training_set, expected_set)
            if Error < min_error:
                min_error = Error
            Errors.append(Error)

            if print_data:
                print("Epoch: ", ii)
                print("min error", min_error)
            print("weights: ", self.weights)
            epochs.append(ii)
            ii += 1
            return min_error, epochs, Errors

