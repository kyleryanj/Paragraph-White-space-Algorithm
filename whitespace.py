import pprint
import math

y = 'Some kinds of writing work best in long paragraphs, and others move through many short paragraphs. Newspaper reporters usually write in very short paragraphs. In addition, their examples and explanations are not always tightly tied in related clusters. This style of writing is addressed to readers who are skimming and looking for the main points in the first few inches of print, so reporters dont develop each idea fully in clear sequence. Information in newspaper articles sometimes has to be reorganized to make a standard essay. Im just adding words now so that I can get closer to 100 words. I wonder what I\'m at right now?'


def q1(inputWords, width): #inputWords is the string of space-separated words
	listOfWords = inputWords.split()
	N = len(listOfWords)
	breaks = [0 for i in range(N - 1)]
	costArray = [0 for i in range(N)]
	arrayOfCosts = [0 for i in range(N)]
	tempList = [0 for i in range(N)]
	arrayOfTemps = [0 for i in range(N)]
	traceArray = [0 for i in range(N-1)]
	for i in range(N):
		if i == 0: #this is the special case for the first psi value calculated
			for j in range(N):
				breaks[N - i - 2] = j + 1  #it's minus 2 here because there are N-1 breaks and we need the last index 
				costArray[j] = cost(listOfWords[breaks[N - i - 2]:], width) #i should be zero here
			arrayOfCosts[i] = list(costArray) #make a copy of costArray so we can still use this variable
			traceArray[i] = list(costArray)
		elif i == (N - 1): #check to see if we are at the very last psi value
			for j in range(N):
				breaks[0] = j + 1
				costArray[j] = cost(listOfWords[:breaks[0]], width) + arrayOfCosts[i-1][j]
			arrayOfCosts[i] = list(costArray)
		else:
			for j in range(N):
				breaks[N - i - 2] = j + 1 #this is the left break in the cost function
				for k in range(N):
					breaks[N - i - 1] = k + 1 #this is the right break
					if breaks[N - i - 2] <= breaks[N - i - 1]: #check to make sure the right break is equal to or greater than left break
						tempList[k] = cost(listOfWords[breaks[N - i - 2]: breaks[N - i - 1]], width) + arrayOfCosts[i-1][k]
					else:
						tempList[k] = float("inf") #if not then cost is infinity
				arrayOfTemps[j] = list(tempList)
				costArray[j] = min(tempList)
			arrayOfCosts[i] = list(costArray)
			traceArray[i] = list(arrayOfTemps)
	rowVal = N - arrayOfCosts[N-1][::-1].index(min(arrayOfCosts[N-1]))
	breaks[0] = rowVal
	for i in range(len(traceArray) - 1):
		if i == (len(traceArray) - 2):
			breakVal = N - traceArray[N-i-2][::-1].index(min(traceArray[N-i-2]))
		breakVal = N - traceArray[N-i-2][rowVal - 1][::-1].index(min(traceArray[N-i-2][rowVal - 1]))
		breaks[i + 1] = breakVal
		rowVal = breakVal

	#This code prints the text given the array of break values
	for i in range(len(breaks)):
		if breaks[N - i - 2] != N:
			listOfWords.insert(breaks[N - i - 2], "\n")
	for i in listOfWords:
		print i,




def cost(subwords, length): #subwords is a list of words that make up the subsequence
	if len(subwords) == 0:
		return 0
	phi = length
	for i in range(len(subwords)):
		phi = phi - (len(subwords[i]) + 1) #we do +1 here to account for spaces after each word
	if phi < 0:
		return float("inf")
	else:
		return phi


q1(y, 33)