from operator import add 
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    viruses=[]
    virus_list=[0]*300
    for i in range(numViruses):
        viruses.append(SimpleVirus(maxBirthProb,clearProb))
    for l in range(numTrials):
        copy=viruses[:]
        means=[]
        patient=Patient(copy,maxPop)
        for m in range(300):
            patient.update()
            means.append(patient.getTotalPop())
        virus_list=list(map(add,virus_list,means))
    virus_avg=[x/numTrials for x in virus_list]
    pylab.plot(virus_avg, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()


    # TODO


