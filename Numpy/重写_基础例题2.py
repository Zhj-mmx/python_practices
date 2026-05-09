import numpy as np

train = np.array([[78, 85, 90],
                  [65, 72, 88]])

test  = np.array([[92, 88, 95],
                  [55, 60, 70]])

bonus = np.array([[5],
                  [5],
                  [10],
                  [0]]) 

all_data = np.hstack(train, test)
