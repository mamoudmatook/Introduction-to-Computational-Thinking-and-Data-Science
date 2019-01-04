def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    result=[]
    for i in range (numTrials):
        buckets=['r','r','r','g','g','g']
        draws=[]
        for j in range(3):
            choice=random.choice(buckets)
            draws.append(choice)
            buckets.remove(choice)
        result.append(draws)
    c=0
    for l in result:
        if l[0]==l[1]==l[2]:
            c+=1
    return c/numTrials
            

