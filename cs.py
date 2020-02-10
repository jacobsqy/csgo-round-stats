import random

ties = 0;
sums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
iterations = 1000000;

for x in range(0, iterations):
    print("Percent completed: " + str(100 * x / iterations) + "%");
    teamA = 0;
    teamB = 0;
    while (teamA < 16 and teamB < 16 and teamA + teamB < 30):
        if random.random() < 0.5:
            teamA = teamA + 1;
        else:
            teamB = teamB + 1;

    if (teamA == teamB):
        ties = ties + 1;
    else:
        i = teamA + teamB - 16;
        sums[i] = sums[i] + 1;


sums.append(ties);
percents = list(map(lambda x: 100 * x / iterations, sums));
print("Iterations: " + str(iterations) + "\nSums = " + str(sums) + "\nPercents: " + str(percents));
print(len(percents));
