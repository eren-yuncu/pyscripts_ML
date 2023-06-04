#Script for merging trimmed individuals
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--file_list', help = 'List of the sequences of merging')
args = parser.parse_args()

inds = open(args.file_list, 'r').read().splitlines()

seq_final = []
seq_name = inds[0].split('_')[0]
text_name = inds[0].split('_chr')[0]
for ind in inds:
	seq_file = open(ind,'r').readlines()
	nuc = []
	for i in seq_file:
		if not (i.startswith('>')):
			nuc.append(i.rstrip())
	seq_final.append(nuc)
seq_merged = ''.join([j for i in seq_final for j in i])

textfile = open(text_name + '_trimmed.fas', 'w')
textfile.write('>' + seq_name + '\n'+ seq_merged + '\n')
textfile.close()
