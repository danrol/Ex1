import numpy as np
file_path = "data.txt"


# class Hypothesis:
#     def __init__(self, size):
#         all_ones_hyp = list(range(size))
#         all_zeros_hyp = list(range(size))


def get_all_negative_hypothesis(train_data_size):
    h = []
    for index in range(1, train_data_size):
        h.extend([index, -index])
    return h


def get_y_predict(train_data_row, h):
    result = 1
    sign = 1
    for index in range(1, len(h)):
        if h[index]> 0:
            sign = 1
        elif h[index] < 0:
            sign = -1
        result = result and (sign*train_data_row[abs(h[index])])
    return result


def consistency_alg(train_data):
    # xt is training data
    h_previous = get_all_negative_hypothesis(len(train_data[0]))
    print("h after received: ")
    print(h_previous)
    num_of_examples = len(train_data)
    num_of_literals = len(train_data[0])-1
    y = train_data[:, len(train_data[0])-1]

    for instance_t in range(num_of_examples):
        h = h_previous
        yt = y[instance_t]
        y_predict = get_y_predict(train_data[instance_t], h)
        if (yt == 1) and (y_predict == 0):
            print("entered if")
            for index in range(1, instance_t+1):
                x_iter = train_data[instance_t][index]
                if x_iter == 1:
                    h.remove(-index)
                    #print("iteration = "+instance_t+" removing -index = "+(-index))
                if x_iter == 0:
                    h.remove(index)
                    #print("iteration = "+instance_t+" removing -index = "+ index)
        if yt == 0:
            continue
        h_previous = h
    return h

if __name__ == "__main__":
    training_examples = np.loadtxt(file_path)
    print(consistency_alg(training_examples))
