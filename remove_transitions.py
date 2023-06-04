#Script for removing transitions from trimmed individuals
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--file_list', help = 'List of the sequences of removing transtions')
parser.add_argument('-o', '--output', help = 'Prefix of the output fas file')
args = parser.parse_args()

inds = open(args.file_list, 'r').read().splitlines()

seq_list = []
seq_name = []
for ind in inds:
    seq_file = open(ind, 'r').readlines()
    nuc = []
    nuc_j = []
    for i in seq_file:
        if (i.startswith('>')):
            seq_name.append(i.rstrip())
        else:
            nuc.append(i.rstrip())
    nuc_j = list(''.join(nuc))
    seq_list.append(nuc_j)
list_length = []
for i, l in enumerate(seq_list):
	list_length.append(len(seq_list[i]))

control_length = all(x == list_length[0] for x in list_length)
if control_length:

    arr1 = np.array(seq_list)
    tsn1 = np.array(['A', 'G'])
    tsn2 = np.array(['C', 'T'])

    for col in range(arr1.shape[1]):
        if np.array_equal((np.unique(arr1[:,col], axis = 0)), tsn1):
           arr2 = np.delete(arr1, col, 1)
    for col in range(arr2.shape[1]):
        if np.array_equal((np.unique(arr2[:,col], axis = 0)), tsn2):
            arr3 = np.delete(arr2, col, 1)

    list_filt = arr3.tolist()
    list_joined = []
    for i in list_filt:
        list_joined.append(''.join(i))

    list_f1 = list(map(list, zip(seq_name, list_joined)))
    list_f2 = [item for sublist in list_f1 for item in sublist]

    textfile = open(args.output + '.fas', 'w')
    for element in list_f2:
        textfile.write(element + '\n')
    textfile.close()

else:
	print('Sequence lengths are not same!')
