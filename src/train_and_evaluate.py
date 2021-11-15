# load the train and test
# train algo
# save the metrices and parameters

import os
import warnings
import sys
import pandas as ps
import numpy a np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet