import random
from random import randint
from random import shuffle

# The boxes from the pdf for reference
boxes = [[20,6],[30,5],[60,8],[90,7],[50,6],[70,9],[30,4]]

# Max weight the bag can hold
max_weight = 120

# The total sum of the values of all the boxes for fitness
# purposes
tot_val = 45

# The size of each genome's set
set_size = 7
 
# The amount of genomes in a population
pop_size = 8

# The set we want to avoid at all costs
worst_set = [0, 0, 0, 0, 0, 0, 0]	

# Done
class MyGenome:
	# Initializes with a set holder and a holder for
	# fitness, weight, and value
    def __init__(self):
        self.gSet = []
        self.fitness = 0
        self.weight = 0
        self.value = 0

        # Creates a set full of zeros for the genome
        for i in range(7):
            self.gSet.append(0)

    # Used to randomly create a sequence for the genome
    # that is used to decided which boxes we will consider
    # taking
    def randomize(self, currgenome):
    	# Used to decide how many 1's will be in this genome's
    	# set
        num = randint(0, 7)
        temparr = [ i for i in range(7)]

        # Used to shuffle the numbers around the array after
        # appending them
        shuffle(temparr)

        i = 0

        # pulls out a random index and then puts a 1 there and will
        # continue until we have placed the amount of 1's that we want
        while i < num:
            index = temparr[i]
            currgenome[index] = 1
            i += 1

        return currgenome

def sort(population):
    more_fit = []
    less_fit = []
    as_fit = []
  
    i = 0

    # The fitness that we used to sort the population
    if  len(population) > 1:
        cutoff = population[0].fitness

        while i < len(population):
            testSub = population[i].fitness

            if testSub < cutoff:
                less_fit.append(population[i])

            if testSub == cutoff:
                as_fit.append(population[i])

            if testSub > cutoff:
                more_fit.append(population[i])

            i += 1

        return sort(more_fit)+as_fit+sort(less_fit)

    else:
        return population

# returns a random genome for the parents for reproduction
def randSelect(population):
    index = randint(0, pop_size/2)
    return population[index]

# Done but want to add random cull seletion
def genAlg(population):
    new_population = []
    generate(new_population)
    # using the cull to get rid of 50% of the population
    cull = (pop_size/2)
    i = 0

    while i < cull:

    	# selection of parents
        parent_x = randSelect(population)
        parent_y = randSelect(population)

        # creation of children
        child_x, child_y = crossover(parent_x, parent_y)

        # deciding whether or not to mutate the children
        if (random.uniform(0,1) < 0.050):
            child_x = mutate(child_x)
            
        if (random.uniform(0,1) < 0.050):
            child_y = mutate(child_y)
            
        # creating a new population from the generated children
        new_population.append(child_x)
        new_population.append(child_y)

        i += 1

    return new_population

#Done
def fitFunc(population):
    weight = 0
    value = 0
    value_arr = []
    value_arr = zeroOut(value_arr)
    i = 0
    j = 0

    while i < pop_size:
        testSub = population[i]

        while j < set_size:
            if (testSub.gSet[j] == 1):
                weight += boxes[j][0]
                value += boxes[j][1]
            j += 1

        j = 0
        testSub.weight = weight
        testSub.value = value

        if (weight > max_weight):
       	    # penalization for being overweight
       	    value -= 120

        value_arr[i] = value

        # reset the values for the next test subject
        value = 0
        weight = 0
        i += 1

    while j < pop_size:
    	# generate the fitness value for each genome
        # I generate fitness by seeing out of the total
        # values from all the boxes how well it did to pick
        # the best ones, meaning how optimal it was in picking
        # the better valued boxes
        fit_val = 100 * (value_arr[j]/tot_val)
        population[j].fitness = fit_val
        j += 1
    
    population = sort(population)
    return population

# Done
def mutate(child):
	# decided where we want the mutation to occer
    pivot = randint(0,set_size-1)

    # mutate
    if (child.gSet[pivot] == 0):
        child.gSet[pivot] = 1
    else:
        child.gSet[pivot] = 0

    return child



# Done
def crossover(parent_x, parent_y):
	#where we want the crossover to take place
    cross = randint(0,set_size)
    # creation of new genomes for the children
    child_x = MyGenome()
    child_y = MyGenome()

    child_x.gSet = parent_x.gSet[:cross] + parent_y.gSet[cross:]
    child_y.gSet = parent_y.gSet[:cross] + parent_x.gSet[cross:]

    return child_x, child_y

def generate(population):

	#used to generate the initial population 
    i = 0

    while i < pop_size:
        newgenome = MyGenome()
        newgenome.gSet = newgenome.randomize(newgenome.gSet)
        population.append(newgenome)

        i += 1

    return population

# Done
def zeroOut(genome_set):
    i = 0

    while i < pop_size:
        genome_set.append(0)
        i += 1

    return genome_set

# Done
def main():
    population = []
    i = 0
    generations = 13

    population = generate(population)

    while i < generations:
        population = fitFunc(population)
        population = genAlg(population)
        
        # genome that has no value will be accepted and will result 
        #in the creation of 1 more generation
        if (population[0].gSet == worst_set):
        	generations += 1
   
        i += 1

    population = fitFunc(population)
    population = sort(population)
    print("Number of Generations: ")
    print(generations)
    print(" ")
    print("Final Generation: ")
    for i in population:
    	print("Genome: ")
    	print(i.gSet)
    	print("Fitness: ")
    	print(i.fitness)
    print("Best Candidate: ")
    print(population[0].gSet)
    print(population[0].value)

if __name__ == '__main__':
    main()