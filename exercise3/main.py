#Shiven, Jay Lebo, Alec, Andrew, Jay Patel

import numpy

def main():
    random= numpy.random.rand(10) #I took this code from internet
                                  #this creates an array of number between (0,1) interval  
                                  #here there are 10 floats in the array. If i want to change the interval i do that by giving arguements in front of 10                                 

    mean = numpy.mean(random)
    median = numpy.median(random)
    standard_dev = numpy.std(random)

    print(random)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation", standard_dev)

main()

