Written by: J. Asher Glover
Problem: The Knapsack Problem

Run Script: python3 backpack.py

Structure: Each Genome takes account for its own fitness, value, and weight, as
	well as keeping track of what it looks like, in the representation of a list.
	The list is a list of 1's and 0's that pairs up with the list of boxes.  If there
	is a 1 in an index of the genome then that means the corresponding box in that index
	of the boxes is add to the "bag" there for its weight and value are added to the
	weight and value of the genome or "bag".  Fitness is determined by how optimally you
	choose boxes because it is the value of the combinations of boxes that have been selected
	by this genome, or put in this "bag", divided by the combined values of all the boxes.
	A penalization is subtracted form the genomes fitness if it is overweight which will keep
	us from selecting that one as our final candidate.

Methodology: A population of randomly generated genomes is used and from there we test 
    the fitness of each genome and then sort them with the more fit genomes ending up 
    at the top of the population.  From there we run through genAlg which culls the 
    population by 50% getting rid of the bottom half of the population which has the not 
    so good fitness.  We then randomly select 2 parents from the top half of the 
    population and use them to create 2 children by method of crossover.  We check to see 
    if either child should be mutated which is a very rare case after which we create a 
    new population from the offspring.  We run this program for 13 generations, however at 
    the end if the best genome is either overweight or has no value, meaning no boxes were 
    taken, we add one more generation to get a better genome candidate.  The end of the 
    program prints out the number of generations we ran through final generation in its 
    entirety which includes the fitness of each genome. Also the best candidate is printed 
    along with its respective value.