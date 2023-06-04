#Script for filtering coding genes from annotation file
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--annotation', help='Name of annotation file')
parser.add_argument('-g', '--gene', help='Name of the gene')
args = parser.parse_args()

ref = open(args.annotation, 'r').readlines()

a = []
for line in ref:
	if not (line.startswith('#')):
		a.append(line)

df = pd.DataFrame(a)
df = df[0].str.split('\t', expand=True,)
df = df.loc[df[2] == args.gene]
df = df[[0, 3, 4]]

df.rename(columns = {0 :'chr', 3 :'begin', 4 :'end'}, inplace=True )
df[['chr', 'begin', 'end']] = df[['chr', 'begin', 'end']].astype(int)

df_filt = df.sort_values(by = 'end')
df_filt.drop_duplicates(subset=['chr', 'begin'], keep='last', inplace =True)
df_filt = df_filt.sort_values(by=['chr', 'begin'])

df_filt[['begin', 'end']] = df_filt[['begin', 'end']].astype(str)
df_filt = df_filt.assign(position = df_filt['begin'] + '-' + df_filt['end'])

df_final = df_filt[['chr', 'position']]
df_final.to_csv(args.gene +'_list.txt', sep =':', index = False, header = False)
