import matplotlib.pyplot
import matplotlib.gridspec
import matplotlib.animation

finished = False

def min_and_mean_fitness(queue):
    global finished

    finished = False
    generations = []
    min_fitness = []
    mean_fitness = []
    max_fitness = []

    fig = matplotlib.pyplot.figure()
    aux = fig.add_subplot(1, 1, 1)

    def animate(i):
        global finished

        if finished:
            return

        gen = queue.get()
        print(gen[1], gen[2], gen[3], gen[4])

        if len(gen) == 0:
            finished = True
            return

        generations.append(gen[1])  #el numero de generacion
        min_fitness.append(gen[2])
        max_fitness.append(gen[3])
        mean_fitness.append(gen[4])

        aux.clear()

        matplotlib.pyplot.xlabel("Generation")
        matplotlib.pyplot.ylabel("Fitness")
        matplotlib.pyplot.title("Fitness real-time")

        l1, = aux.plot(generations, min_fitness, 'r-')
        l2, = aux.plot(generations, mean_fitness, 'g-')
        l3, = aux.plot(generations, max_fitness, 'b-')

        matplotlib.pyplot.legend([l3, l2, l1], ["Maximum Fitness", "Mean Fitness", "Minimum Fitness"])

    ani = matplotlib.animation.FuncAnimation(fig, animate, interval=100)
    matplotlib.pyplot.show()
    return

