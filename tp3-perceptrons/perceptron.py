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
            training_accuracies.append(training_correct_cases / len(training_set))
            if print_data:
                print("Epoch: ", ii)
                print("min error", min_error)
            print("weights: ", self.weights)
            epochs.append(ii)
            ii += 1
        return min_error, epochs, errors, training_accuracies

    def test(self, test_set, expected_test):
        return self.calculate_mean_square_error(test_set, expected_test)


class NeuronLayer:  # es una matriz
    def __init__(self, neurons_qty, inputs=None, activation="tanh"):
        self.neurons_qty = neurons_qty
        self.inputs = inputs
        (f, df) = self.get_functions(activation)
        self.f = f
        self.df = df
        self.weights = None

    def init_weights(self, inputs=None):
        self.inputs = inputs if inputs is not None else self.inputs
        self.weights = 2 * np.random.random((self.neurons_qty, self.inputs+1)) - 1  # esto ES una matriz

    def get_functions(self, activation_function):
        if activation_function == "tanh":
            f = tanh_act
            df = der_tanh_act
        elif activation_function == "sigmoid":
            f = sigmoid_act
            df = der_sigmoid_act
        else:
            raise LookupError("falta funcion")
        return f, df

    def forward(self, a_input):
        # [w1 w2 B] . [i0, i1, i2] = k

        # [w1, w2, B] x [i0     = [k]
        #                i1
        #                i2]

        #         [w11, w12, B1] x [i0     = [o1    # salida de la primera neurona
        #         [w21, w22, B2]    i1        o2]   # salida de la segunda neurona
        #                           i2]
        a_input_biased = np.insert(a_input, 0, 1)
        output = np.matmul(self.weights, np.transpose(a_input_biased))
        output = np.transpose(output)
        return output


class MultiLayerPerceptron:
    def __init__(self, neuron_layers, eta=0.01):
        self.eta = eta
        self.neuron_layers = neuron_layers
        self._init_layers()

    def _init_layers(self):
        for i in range(len(self.neuron_layers)):
            if i != 0:  # la capa 0 no depende de nadie, depende de los inputs
                self.neuron_layers[i].init_weights(inputs=self.neuron_layers[
                    i - 1].neurons_qty)  # se fija cuantas salidas tiene la capa anterior y se lo pone a esta nueva capa
            else:
                self.neuron_layers[i].init_weights()  # no le paso nada porque ya lo tenia

    def predict(self, a_input):
        res = a_input
        for i in range(len(self.neuron_layers)):
            res = self.neuron_layers[i].forward(res)
        return res

    def calculate_mean_square_error(self, training_set, expected_set):
        sum = 0
        for i in range(len(training_set)):
            x = training_set[i]
            y = expected_set[i]

            predicted = self.predict(x)
            aux = np.linalg.norm(predicted - y, ord=2) ** 2
            sum += aux
        return sum / len(training_set)

    def train(self, training_set, expected_set, error_epsilon=0, iterations_qty=1000, print_data=True):
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
            while j < len(training_set):
                x = training_set[shuffled_list[j]]
                y = expected_set[shuffled_list[j]]

                predicted_value = self.predict(x)  # forward propagation

                print(predicted_value)

                # self.back_propagate(predicted_value, x, y)
                j += 1

            Error = self.calculate_mean_square_error(training_set, expected_set)
            if Error < min_error:
                min_error = Error
            ii += 1


