import matplotlib.pyplot as plt
import matplotlib.gridspec
import matplotlib.animation

finished_min = False

def min_and_mean_fitness(queue):

    global finished_min

    finished_min = False
    generations = []
    min_fitness = []
    mean_fitness = []
    max_fitness = []

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    def animate(i):

        gen = queue.get()
        #gen = [1,2,3,4,5]

        print("desde graph")
        print(gen[1])
        print(len(gen[0]))

        if len(gen[0]) == 0:
            return

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


def diversity(queue):
    generations = []
    diversity_weapon = []
    diversity_boots = []
    diversity_helmet = []
    diversity_gloves = []
    diversity_chestplate = []
    diversity_height = []

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    def animate(i):
        gen = queue.get()

        if len(gen[0]) == 0:
            return

        generations.append(gen[1])  # el numero de generacion
        diversity_weapon.append(gen[2])
        diversity_boots.append(gen[3])
        diversity_helmet.append(gen[4])
        diversity_gloves.append(gen[5])
        diversity_chestplate.append(gen[6])
        diversity_height.append(gen[7])

        ax.clear()

        plt.xlabel("Generation")
        plt.ylabel("Diversity")
        plt.title("Diversity real-time")


        l1, = ax.plot(generations, diversity_weapon, color='#2eb6ff', linestyle='solid')
        l2, = ax.plot(generations, diversity_boots, color='#602ae8', linestyle='solid')
        l3, = ax.plot(generations, diversity_helmet, color='#ffec1f', linestyle='solid')
        l4, = ax.plot(generations, diversity_gloves, color='#e61ea7', linestyle='solid') #ver mas colores
        l5, = ax.plot(generations, diversity_chestplate, color='#18f57b', linestyle='solid') #ver mas colores
        l6, = ax.plot(generations, diversity_height, color='#ff5436', linestyle='solid') #ver mas colores



    ani = matplotlib.animation.FuncAnimation(fig, animate, interval=100)
    plt.show()
    return

