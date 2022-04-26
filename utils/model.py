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

def split_plot(train,validate,test,col='close'):
    plt.figure(figsize=(16,9))
    plt.plot(train[col])
    plt.plot(validate[col])
    plt.plot(test[col])
    plt.ylabel(col+' price')
    plt.xlabel(col+' time')
    plt.title('btcusd 1m kline, close price')
    plt.show()

def yhat_model(train):
	# last observed value
	lov = train['close'][-1:][0]
	# add lov to yhat
	yhat_df = pd.DataFrame({'close': validate.close,'lov': [lov]},index = validate.index)
	# calc avg
	avg =round(train.close.mean(),3)
	avg = pd.DataFrame({'avg': [avg]},index = validate.index)
	# add avg to yhat
	yhat_df=pd.concat([yhat_df,avg],axis=1)
	# calc simple moving average using TAlib
	sma=talib.SMA(train.close,10)
	sma=round(sma[-1],3)
	sma = pd.DataFrame({'sma': [sma]},index = validate.index)
	# add sma to yhat
	yhat_df=pd.concat([yhat_df,sma],axis=1)
	# calc holt's linear trend prediction
	model = Holt(train.close, exponential = True)
	model = model.fit(smoothing_level = .1, 
						smoothing_slope = .1, 
						optimized = False)
	# add holts to yhat
	yhat_items = model.predict(start = validate.index[0], 
								end = validate.index[-1])
	yhat_df['holt'] = round(yhat_items, 2)

	#plot yhat
	g = sns.JointGrid()
	g.fig.set_figwidth(16)
	g.fig.set_figheight(9)
	sns.lineplot(data=yhat_df,ax=g.ax_joint)
	sns.lineplot(data=train.close,ax=g.ax_joint)
	#sns.kdeplot(yhat_df.close, linewidth=2, ax=g.ax_joint)
	return yhat_df


def rmse_model(yhat_df):
	# start eval_df for rmse storage
	eval_df=pd.DataFrame()
	# comb through yhat and calc rmse, not close
	for col in yhat_df.columns:
		if col == 'close':
			print('skipping close')
			continue
		else:
			print(col)
			# calc rmse 
			x=mean_squared_error(yhat_df.close,yhat_df[col],squared=False)
			# add to eval_df
			eval_df=pd.concat([eval_df,pd.DataFrame({col:[x]})],axis=1)
	# plot eval_df
	p=sns.barplot(data=eval_df)
	p.set_xlabel('Model')
	p.set_ylabel('RMSE')
	return eval_df