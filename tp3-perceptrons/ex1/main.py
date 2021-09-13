from perceptron import SimplePerceptron
import numpy

train_data = numpy.array([
        [-1, -1, -1],
        [-1, 1, -1],
        [1, -1, 1],
        [1, 1, 1]
    ])

and_expected_data = numpy.array([-1, -1, -1, 1])

perceptron = SimplePerceptron(train_data, and_expected_data)
perceptron.train()

i = 0
while(i < len(and_expected_data)):
    print("input: ", train_data[i])
    print("expected: ", and_expected_data[i])
    print("guessed: ", perceptron.guess(train_data[i]))
    i += 1

print(perceptron.guess([-1,-1,1]))

#or_train_data = numpy.array([
#       [-1, 1],
#       [1, -1],
#        [-1, -1],
#        [1, 1]
#    ])
or_expected_data = numpy.array([-1, 1, 1, 1])

second_perceptron = SimplePerceptron(train_data, or_expected_data)
second_perceptron.train()
print(second_perceptron.guess([-1, -1, 1]))

i = 0
while(i < len(or_expected_data)):
    print("input: ", train_data[i])
    print("expected: ", or_expected_data[i])
    print("guessed: ", second_perceptron.guess(train_data[i]))
    i += 1
