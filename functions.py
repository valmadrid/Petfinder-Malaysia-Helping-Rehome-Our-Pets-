
import pandas as pd

import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import itertools

from statistics import mode

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.feature_selection import SelectFromModel

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score, roc_curve, auc, classification_report, confusion_matrix
from sklearn.metrics import f1_score, precision_recall_fscore_support, precision_recall_curve
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus


from itertools import cycle

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.preprocessing import MinMaxScaler
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from scipy import interp
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelBinarizer
from  sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import multilabel_confusion_matrix


def minmax_scaler(X_train, X_test, cols_to_scale):
    """
    Takes in X train and test and scale then columns specified in cols_to_scale (list)
    
    """

    X_train_cat = X_train.drop(cols_to_scale, axis=1)
    X_test_cat = X_test.drop(cols_to_scale, axis=1)

    X_train_cont = X_train[cols_to_scale]
    X_test_cont = X_test[cols_to_scale]

    scaler = MinMaxScaler()
    scaler.fit(X_train_cont)
    X_train_cont_scaled = scaler.transform(X_train_cont)
    X_test_cont_scaled = scaler.transform(X_test_cont)

    X_train_scaled = pd.DataFrame(X_train_cont_scaled,
                                  columns=X_train_cont.columns,
                                  index=X_train_cont.index)
    X_train_scaled = pd.concat([X_train_scaled, X_train_cat], axis=1)

    X_test_scaled = pd.DataFrame(X_test_cont_scaled,
                                 columns=X_test_cont.columns,
                                 index=X_test_cont.index)
    X_test_scaled = pd.concat([X_test_scaled, X_test_cat], axis=1)

    return X_train_scaled, X_test_scaled