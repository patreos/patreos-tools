import operator

dropDict={}

with open('./snapshot/airdrop_results_2018-10-01.txt', 'r') as f:
	for line in f:
		tokens = line.split(',')
		user = tokens[0]
		patr = tokens[1]
		dropDict[user] = patr

# Create a list of tuples sorted by index 1 i.e. value field
listofTuples = sorted(dropDict.items(), reverse=True ,  key=lambda x: float(x[1]))


output_results_file = './snapshot/airdrop_results_2018-10-01-sorted.txt'
p = open(output_results_file, 'a')
# Iterate over the sorted sequence
for elem in listofTuples :
    p.write('%s,%s\n' % ( elem[0].replace('\n',''), elem[1].replace('\n','') ) )
    print("%s,%s" % ( elem[0].replace('\n',''), elem[1].replace('\n','') ) )

p.close()
