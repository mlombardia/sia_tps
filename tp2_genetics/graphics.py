import matplotlib.pyplot as plt
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

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    def animate(i):



        gen = queue.get()
        #gen = [1,2,3,4,5]
        print(gen[1], gen[2], gen[3], gen[4])
        print(len(gen))
        if len(gen) == 0:
            finished = True
            #return

        generations.append(gen[1])  #el numero de generacion
        min_fitness.append(gen[2])
        max_fitness.append(gen[3])
        mean_fitness.append(gen[4])

        ax.clear()

        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.title("Fitness real-time")

        l1, = ax.plot(generations, min_fitness, 'r-')
        l2, = ax.plot(generations, mean_fitness, 'g-')
        l3, = ax.plot(generations, max_fitness, 'b-')

        plt.legend([l3, l2, l1], ["Maximum Fitness", "Mean Fitness", "Minimum Fitness"])

    ani = matplotlib.animation.FuncAnimation(fig, animate, interval=100)
    plt.show()
    return

