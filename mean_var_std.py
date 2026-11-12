import numpy as np

def calculate(list_inp):
    if len(list_inp) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list_inp).reshape(3,3)
    calculations = { 
        "mean" : [ matrix.mean(axis=0).tolist(),
                   matrix.mean(axis=1).tolist(),
                   float(matrix.mean()) 
        ],
        "variance" : [ matrix.var(axis=0).tolist(),
                       matrix.var(axis=1).tolist(),
                       float(matrix.var()) 
        ],
        "standard deviation" : [ matrix.std(axis=0).tolist(),
                                 matrix.std(axis=1).tolist(),
                                 float(matrix.std())   
        ],
        "max" : [ matrix.max(axis=0).tolist(),
                  matrix.max(axis=1).tolist(),
                  int(matrix.max())

        ],
        "min" : [ matrix.min(axis=0).tolist(),
                  matrix.min(axis=1).tolist(),
                  int(matrix.min())

        ],
        "sum" : [ matrix.sum(axis=0).tolist(),
                  matrix.sum(axis=1).tolist(),
                  int(matrix.sum())

        ]
    }
    print(calculations)
    return calculations