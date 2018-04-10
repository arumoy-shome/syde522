'''
creates datasets/Y.csv consisting of labels for reviews dataset
'''

import math

THRESHOLD = math.floor(1.385085) 
NOT_USEFUL = 0
USEFUL = 1

def labeler(vote):
    if math.floor(vote) < THRESHOLD:
        return NOT_USEFUL
    else:
        return USEFUL

Y = [labeler(row['useful']) for index, row in reviews.iterrows()]

df = pd.DataFrame(Y)
df.to_csv('../dataset/Y.csv', header=['label'], index=False)