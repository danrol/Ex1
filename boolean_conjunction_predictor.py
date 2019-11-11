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
    for index in range(len(h)):
        data_literal_index = abs(h[index])
        data_literal_value = train_data_row[data_literal_index-1]
        if h[index] < 0:
            if data_literal_value == 0:
                data_literal_value = 1
            else:
                data_literal_value = 0
        result = result and data_literal_value
    return result


def consistency_alg(train_data):
    h_previous = get_all_negative_hypothesis(len(train_data[0]))
    print("h after received: ")
    print(h_previous)
    num_of_examples = len(train_data)
    y = train_data[:, len(train_data[0])-1]

    for instance_t in range(num_of_examples):
        h = h_previous.copy()
        yt = y[instance_t]
        x_row = train_data[instance_t]
        y_predict = get_y_predict(x_row[0: -1], h)
        if (yt == 1) and (y_predict == 0):
            print("entered if")
            for index in range(instance_t+1):
                literal_serial_num = index+1
                x_iter = train_data[instance_t][index]
                if x_iter == 1:
                    h.remove(-literal_serial_num)
                    #print("iteration = "+instance_t+" removing -index = "+(-index))
                if x_iter == 0:
                    h.remove(literal_serial_num)
                    #print("iteration = "+instance_t+" removing -index = "+ index)
        if yt == 0:
            continue
        h_previous = h.copy()
    return h

if __name__ == "__main__":
    training_examples = np.loadtxt(file_path)
    print("final answer:")
    print(consistency_alg(training_examples))
