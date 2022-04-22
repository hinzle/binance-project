# env
local_path = '/Users/hinzlehome/codeup-data-science/binance-project/'
import sys
sys.path.insert(0,local_path+'.env')
from env import get_db_url

# local-host
import requests
import os
import datetime

# python data science library's
import math
import numpy as np
import pandas as pd
from scipy import stats

# sci-kit-learn modules
from sklearnex import patch_sklearn
patch_sklearn()
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, RFE, f_regression
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression, LinearRegression, LassoLars, TweedieRegressor
from sklearn.metrics import (
	confusion_matrix,accuracy_score,precision_score,recall_score,
	classification_report,mean_squared_error,r2_score,explained_variance_score
	)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer, PolynomialFeatures
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text


# visualizations
from pydataset import data
import matplotlib.pyplot as plt
import seaborn as sns


# state properties
np.random.seed(123)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)