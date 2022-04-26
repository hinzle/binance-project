# model.py
'''
this module is used to forecast binance bitcoin timedata.
includes viz.
'''
import sys
local_path = '/Users/hinzlehome/codeup-data-science/binance-project/'
sys.path.insert(0, local_path)
from utils.imports import *
# used for trouble shooting filepath issues
# import os
# print(os.getcwd())


# evaluation function to compute rmse
def evaluate(target_var):
    rmse = round(math.sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 0)
    return rmse

# plot and evaluate 
def plot_and_eval(target_var):
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var], label = 'Train', linewidth = 1)
    plt.plot(validate[target_var], label = 'Validate', linewidth = 1)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = evaluate(target_var)
    print(target_var, '-- RMSE: {:.0f}'.format(rmse))
    plt.show()


def append_eval_df(model_type, target_var):
	'''
	function to store rmse for comparison purposes
	'''
	rmse = evaluate(target_var)
	d = {'model_type': [model_type], 'target_var': [target_var], 'rmse': [rmse]}
	d = pd.DataFrame(d)
	return eval_df.append(d, ignore_index = True)
