'''
Possible labels
	COMMA
	PERIOD
	QUESTION_MARK
	EXCLAMATION_POINT
	COLON
	SPACE

Low-level feature functions
	1. The current word is 'and, but, yet, or, nor, for, so' and the previous tag is COMMA. 
	2. The current word is 'however, consequently, otherwise, moreover, nevertheless', the previous tag is COMMA and the current tag is COMMA.
	3. The previous tag is 'PERIOD/EXCLAMATION_POINT/QUESTION_MARK' and the current tag is STOP.
	4. The previous tag is START, the current word is 'well, now, yes, moreover, furthermore, specifically, however, likewise, therefore, consequently, meanwhile'(transitional phrase) and the current tag is COMMA. Basically transitional phrase at the beginning of a sentence.
	Using POS

'''		
from helper import *
def collins_train(data, pos, labels, num_epochs):
	iterations = 0
	W = np.zeros(J, dtype=float)
	'''for i in range(len(data)):
		if 'QUESTION_MARK' in labels[i]:
			print data[i]
			print labels[i]
	'''
	print "training started..."
	while(iterations < num_epochs):
		for i in range(5000):
			X = [data[i], pos[i]]
			Y = y2int(labels[i]) #start and stop tags also appended
			W = W + contrdiv_grad(X,Y,W)
			print i , np.count_nonzero(W)
		iterations = iterations +  1
	print "training done...."
	return W
def test(data, pos, labels, W):
	num_test = len(data)
	print "num", num_test
	true_tags = 0
	tot_tags = 0
	for i in range(num_test):
		print i
		X = [data[i], pos[i]]
		Y = y2int(labels[i])
		nz_a = non_zero_a(X)
		Y_pred = decode(X,W,nz_a)
		Y = Y[1:-1]
		Y_pred = Y_pred[1:-1]
		print data[i]
		print pos[i]	
		print Y
		print Y_pred
		for i in range(len(Y)):
			if not (Y[i]==6 or Y[i]==2):
				true_tags += int(Y[i]==Y_pred[i])
				tot_tags += 1
	print "prediction accuracy : " , (true_tags*100.0)/tot_tags , "%"

train_data = load_data('trainingSentences')
train_labels = load_data('trainingLabels')
train_POS = load_data('trainingPOS')
test_data = load_data('testSentences')
test_labels = load_data('testLabels')
test_POS = load_data('testPOS')

#W = collins_train(train_data, train_POS, train_labels, 1)
#test(test_data[1:100], test_POS[1:100], test_labels[1:100], W)

#use this once before starting the training
#def cache_POS(data, file_name ):
#	f = open('punctuationDataset/'+file_name+".txt", "w")
#	for i in range(len(data)):
#		f.write(' '.join(POS(data[i])) + '\n')
#	f.close()

#cache_POS(test_data, 'testPOS')
def custom(data, labels , pos_tags):
	f = open('punctuationDataset/custom.txt', "w")
	punc = ",.?!: "
	for i in range(len(data)):
		for j in range(len(train_data[i])):			
			f.write(train_data[i][j]+"_"+ pos_tags[i][j])
			t = t2i(train_labels[i][j])
			f.write(punc[t-1])
		f.write("\n")
	f.close()


#custom(train_data, train_labels, train_POS)