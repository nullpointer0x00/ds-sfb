import sys
sys.path.append("../")
from backpain_helper import BackpainHelper
from sklearn import neighbors
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.io import sql
import sqlite3

bh = BackpainHelper()
df = bh.get_spine_data()

columns = ['pelvic_incidence', 'pelvic_tilt','lumbar_lordosis_angle','sacral_slope','pelvic_radius','degree_spondylolisthesis','pelvic_slope','direct_tilt','thoracic_slope','cervical_tilt','sacrum_angle','scoliosis_slope']
df = bh.get_spine_data()
X_data = df[columns]
y_data = df.classification


def nested_cross_val(X, y, n_trials) :
    X_data = X
    y_data = y

    NUM_TRIALS = n_trials
    # Arrays to store scores
    non_nested_scores = np.zeros(NUM_TRIALS)
    nested_scores = np.zeros(NUM_TRIALS)

    # Loop for each trial
    for i in range(NUM_TRIALS):
        inner_cv = KFold(n_splits = 4, shuffle=True, random_state=i)
        outer_cv = KFold(n_splits = 4, shuffle=True, random_state=i)

        # Non_nested parameter search and scoring
        clf = GridSearchCV(estimator=neighbors.KNeighborsClassifier(),
                       param_grid={'n_neighbors':[5],'weights':['uniform']},
                       cv=inner_cv)
        clf.fit(X_data, y_data)
        non_nested_scores[i] = clf.best_score_
        nested_score = cross_val_score(clf, X=X_data, y=y_data, cv=outer_cv)
        nested_scores[i] = nested_score.mean()

    score_difference = non_nested_scores - nested_scores
    return score_difference

print nested_cross_val(X_data, y_data, 50)