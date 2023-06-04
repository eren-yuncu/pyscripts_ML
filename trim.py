#Script for trimming individuals
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--file_list', help='List of the sequences of trimming')
args = parser.parse_args()

inds = open(args.file_list, 'r').read().splitlines()

seq_list = []
text_name = []
seq_name = []
for ind in inds:
	text_name.append(ind.rstrip('.fas'))
	seq_name.append(ind.split('_')[0])
	seq_file = open(ind,'r').readlines()
	nuc = []
	nuc_j = []
	for i in seq_file:
		if not (i.startswith('>')):
			nuc.append(i.rstrip())
	nuc_j = list(''.join(nuc))
	seq_list.append(nuc_j)

list_length = []
for i, l in enumerate(seq_list):
	list_length.append(len(seq_list[i]))

control_length = all(x == list_length[0] for x in list_length)
if control_length:
	arr = np.array(seq_list)
	arr_trim = arr[:, np.all(arr != 'N', axis = 0)]
	list_filt = arr_trim.tolist()
	list_joined = []
	for i in list_filt:
		list_joined.append(''.join(i))
	for index, sequence in enumerate(list_joined):
		with open(text_name[index] + '_trimmed.fas', 'w') as text_file:
			print(seq_file[0] + sequence, file = text_file)
else:
	print('Sequence lengths are not same!')

