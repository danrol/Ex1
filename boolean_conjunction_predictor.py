import numpy as np
input_file_path = "data.txt"
#input_file_path = "alternative_data.txt"
output_file_path = "output.txt"


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
    num_of_examples = len(train_data)
    y = train_data[:, len(train_data[0])-1]

    for instance_t in range(num_of_examples):
        h = h_previous.copy()
        yt = y[instance_t]
        x_row = train_data[instance_t][:-1]
        y_predict = get_y_predict(x_row, h)
        if (yt == 1) and (y_predict == 0):

            for index, x_iter in enumerate(x_row):
                literal_serial_num_to_del = index + 1
                if x_iter == 1:
                    literal_serial_num_to_del = -literal_serial_num_to_del
                if literal_serial_num_to_del in h:
                    h.remove(literal_serial_num_to_del)

        if yt == 0:
            continue
        h_previous = h.copy()
    return h


def get_string_result(h):
    result = ""
    for x in h:
        if x < 0:
            result = result + "not(x" + str(abs(x))+") "
        else:
            result = result + "x"+str(abs(x))+" "
    return result


def write_output_to_file(h, result):
    file = open(output_file_path, 'w')
    file.write(result)
    file.close()


if __name__ == "__main__":
    training_examples = np.loadtxt(input_file_path)
    h = consistency_alg(training_examples)
    string_result = get_string_result(h)
    write_output_to_file(h, string_result)
    print(string_result)