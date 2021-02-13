from sklearn import svm

#function mostFrequent taken from https://www.geeksforgeeks.org/frequent-element-array/
def mostFrequent(arr, n):

    # Sort the array
    arr.sort()

    # find the max frequency using
    # linear traversal
    max_count = 1; res = arr[0]; curr_count = 1

    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count += 1

        else :
            if (curr_count > max_count):  
                max_count = curr_count
                res = arr[i - 1]

            curr_count = 1

    # If last element is most frequent
    if (curr_count > max_count):

        max_count = curr_count
        res = arr[n - 1]

    return res

def ensembleMixedPredict(inputs_train, outputs_train, inputs_test, outputs_test, inputs_train2D, inputs_test2D):
    yhats = []
    yhats2 = []


    #SVM
    classifier1 = svm.SVC(kernel='linear')
    classifier1.fit(inputs_train2D, outputs_train)
    yhats2.append(classifier1.predict(inputs_test2D))
    classifier2 = svm.SVC(kernel='rbf')
    classifier2.fit(inputs_train2D, outputs_train)
    yhats2.append(classifier2.predict(inputs_test2D))
    classifier3 = svm.SVC(kernel='poly')
    classifier3.fit(inputs_train2D, outputs_train)
    yhats2.append(classifier3.predict(inputs_test2D))

    #LSTM
    c1 = makeLSTM_Model(inputs_train, outputs_train, 'adamax', 15, 0.2)
    yhats.append(c1.predict(inputs_test))
    c2 = makeLSTM_Model(inputs_train, outputs_train, 'adamax', 20, 0.3)
    yhats.append(c2.predict(inputs_test))
    #c4 = makeLSTM_Model(inputs_train, outputs_train, 'adamax', 10, 0.1)
    #yhats.append(c4.predict(inputs_test))
    c3 = makeLSTM_Model(inputs_train, outputs_train, 'adagrad', 20, 0.2)
    yhats.append(c3.predict(inputs_test))
    yhats = np.array(yhats)
    yhats = np.argmax(yhats, axis = 2)
    yhats2 = np.array(yhats2)
    #print('yhats', yhats.shape)
    #print('yhats2', yhats2.shape)
    yhats = np.append(yhats, yhats2, axis = 0)
    #print('combined', yhats.shape)
    #print(yhats)
    #yhats = np.argmax(yhats, axis = 0)     This argmax doesnt work
    #print('argmax', yhats.shape)
    #print(yhats)
    outcomes = np.zeros(len(yhats[0]))
    for i in range (len(yhats[0])):
        temp = np.zeros(len(yhats))
        for j in range (len(yhats)):
            temp[j] = yhats[j][i]
        outcomes[i] = mostFrequent(temp, len(temp))
        #print(temp, outcomes[i])

    #print(outcomes)


    return accuracy_score(outputs_test, outcomes)



def predictLabelsMixed(trainInputs, trainOutputs):
    inputs_train, inputs_test, outputs_train, outputs_test = splitData(trainInputs, trainOutputs)
    inputs_train = np.asarray(inputs_train).astype('float32')
    inputs_test = np.asarray(inputs_test).astype('float32')
    outputs_train = np.asarray(outputs_train).astype('float32')
    outputs_test = np.asarray(outputs_test).astype('float32')


    inputs_train2D = inputs_train.reshape(216, 338)
    inputs_test2D = inputs_test.reshape(54, 338)

    # Predict the test labels
    prediction = ensembleMixedPredict(inputs_train, outputs_train, inputs_test, outputs_test, inputs_train2D, inputs_test2D )


    return prediction
