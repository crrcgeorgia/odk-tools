#%%
from itertools import permutations
from random import choice
import pandas as pd

#%%

# Load source csv
df = pd.read_csv('q2_sourcelab.csv')

# Set the number of permutations
num_perms = 30

# Check groups of labels are evenly sized, important for multilanguage
lab_groups = df['col'].unique()
if len(lab_groups) > 1:
    num_qs = []
    for group in lab_groups:
        num_qs.append(len(df[df['col'] == group]))
    if len(set(num_qs)) != 1:
        print('Warning: Groups of labels must be evenly sized. You will probably get odd results')

# Get permutations, this may take a while
perms = list(permutations(range(num_qs[0])))

# Get indices for new table
indices = [choice(perms) for i in range(num_perms)]

# %%
out = {}
for group in lab_groups:
    out[group] = []
    labs = df[df['col'] == group]['lab'].values
    measure = df[df['col'] == group]['measurement'].values
    for idx in indices:
        out[group].append((labs[list(idx)], measure[list(idx)]))

table = {}
for group, vals in out.items():
    table[group] = []

    table['condition'] = []
    table['measurement'] = []
    for n, i in enumerate(vals):
        for m, x in enumerate(zip(i[0], i[1])):
            table[group].append(x[0])
            table['measurement'].append(x[1])
            table['condition'].append(f"{n+1}-V{m+1}")

final = pd.DataFrame(table)[['condition', 'measurement'] + list(lab_groups)]
final.to_csv('q2.csv')
# %%


