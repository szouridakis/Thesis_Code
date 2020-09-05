import h5py
import matplotlib.pyplot as plt
import glob
import numpy as np
from sklearn import metrics

timestamps1 = []
timestamps2 = []
timestamps3 = []
timestamps4 = []
timestamps5 = []
timestamps6 = []
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
data10 = []
data11 = []
data12 = []
data13 = []
data14 = []
sub1 = []
sub2 = []
sub3 = []
sub4 = []
sub5 = []
sub6 = []
sub7 = []

############################ extract data from hdf5 files ###############################

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1a/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        #timestamps1.append(group_key)
        data_set = hf[group_key]
        data1.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1a/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        data_set = hf[group_key]
        data2.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1b/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps2.append(group_key)
        data_set = hf[group_key]
        data3.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1b/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        data_set = hf[group_key]
        data4.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        #timestamps3.append(group_key)
        data_set = hf[group_key]
        data5.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        data_set = hf[group_key]
        data6.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp2a/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        #timestamps3.append(group_key)
        data_set = hf[group_key]
        data7.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp2a/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        data_set = hf[group_key]
        data8.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp2b/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        #timestamps3.append(group_key)
        data_set = hf[group_key]
        data9.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp2b/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        data_set = hf[group_key]
        data10.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp3a/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        #timestamps3.append(group_key)
        data_set = hf[group_key]
        data11.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp3a/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        data_set = hf[group_key]
        data12.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp3b/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        #timestamps3.append(group_key)
        data_set = hf[group_key]
        data13.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp3b/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        data_set = hf[group_key]
        data14.append(data_set[()])
    hf.close()

# for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp2b/Thermal*.hdf5'):
#
#    hf = h5py.File(filename, 'r')
#
#    for group_key in hf.keys():
#        timestamps5.append(group_key)
#        data_set = hf[group_key]
#        data5.append(data_set[()].max())
#        data6.append(data_set[()].min())
#    hf.close()


############################ edit data before plotting ###############################
cross_cor_arr = [0,0,0,0,0,0,0]
RMSE_arr = [0,0,0,0,0,0,0]
MAE_arr = [0,0,0,0,0,0,0]
mean_arr = []
var_arr =[]


#RMSE1 = metrics.mean_squared_error(data1, data2, squared="False")
#MAE1 = metrics.mean_absolute_error(data1, data2)

#data1 = (data1 - np.mean(data1)) / (np.std(data1) *len(data1))
#data2 = (data2 - np.mean(data2)) / (np.std(data2))
#cross_cor1 = np.correlate(data1,data2)
#cross_cor_arr[0] = cross_cor1[0]
#RMSE_arr[0] = round(RMSE1,2)
#MAE_arr[0] = round(MAE1,2)
sub1 = np.subtract(data1,data2)
mean_arr.append(round(sub1.mean(),3))
var_arr.append(round(sub1.var(),3))

del data3[:100]  #the first 29 samples on MLXObj in experiment 1B are not normal because of calibration
del data4[:100]
#RMSE2 = metrics.mean_squared_error(data3, data4, squared="False")
#MAE2 = metrics.mean_absolute_error(data3, data4)

#data3 = (data3 - np.mean(data3)) / (np.std(data3) *len(data3))
#data4 = (data4 - np.mean(data4)) / (np.std(data4))
#cross_cor2 = np.correlate(data3,data4)
#cross_cor_arr[1] = cross_cor2[0]
#RMSE_arr[1] = round(RMSE2,2)
#MAE_arr[1] = round(MAE2,2)
sub2 = np.subtract(data3,data4)
mean_arr.append(round(sub2.mean(),3))
var_arr.append(round(sub2.var(),3))


#RMSE3 = metrics.mean_squared_error(data5, data6, squared="False")
#MAE3 = metrics.mean_absolute_error(data5, data6)

#data5 = (data5 - np.mean(data5)) / (np.std(data5) *len(data5))
#data6 = (data6 - np.mean(data6)) / (np.std(data6))
#cross_cor3 = np.correlate(data5,data6)
#cross_cor_arr[2] = cross_cor3[0]
#RMSE_arr[2] = round(RMSE3,2)
#MAE_arr[2] = round(MAE3,2)
sub3 = np.subtract(data5,data6)
mean_arr.append(round(sub3.mean(),3))
var_arr.append(round(sub3.var(),3))


#RMSE4 = metrics.mean_squared_error(data7, data8, squared="False")
#MAE4 = metrics.mean_absolute_error(data7, data8)

#data7 = (data7 - np.mean(data7)) / (np.std(data7) *len(data7))
#data8 = (data8 - np.mean(data8)) / (np.std(data8))
#cross_cor4 = np.correlate(data7,data8)
#cross_cor_arr[3] = cross_cor4[0]
#RMSE_arr[3] = round(RMSE4,2)
#MAE_arr[3] = round(MAE4,2)
sub4 = np.subtract(data7,data8)
mean_arr.append(round(sub4.mean(),3))
var_arr.append(round(sub4.var(),3))


#RMSE5 = metrics.mean_squared_error(data9, data10, squared="False")
#MAE5 = metrics.mean_absolute_error(data9, data10)

#data9 = (data9 - np.mean(data9)) / (np.std(data9) *len(data9))
#data10 = (data10 - np.mean(data10)) / (np.std(data10))
#cross_cor5 = np.correlate(data9,data10)
#cross_cor_arr[4] = cross_cor5[0]
#RMSE_arr[4] = round(RMSE5,2)
#MAE_arr[4] = round(MAE5,2)
sub5 = np.subtract(data9,data10)
mean_arr.append(round(sub5.mean(),3))
var_arr.append(round(sub5.var(),3))


#RMSE6 = metrics.mean_squared_error(data11, data12, squared="False")
#MAE6 = metrics.mean_absolute_error(data11, data12)

#data11 = (data11 - np.mean(data11)) / (np.std(data11) *len(data11))
#data12 = (data12 - np.mean(data12)) / (np.std(data12))
#cross_cor6 = np.correlate(data11,data12)
#cross_cor_arr[5] = cross_cor6[0]
#RMSE_arr[5] = round(RMSE6,2)
#MAE_arr[5] = round(MAE6,2)
sub6 = np.subtract(data11,data12)
mean_arr.append(round(sub6.mean(),3))
var_arr.append(round(sub6.var(),3))


#RMSE7 = metrics.mean_squared_error(data13, data14, squared="False")
#MAE7 = metrics.mean_absolute_error(data13, data14)

#data13 = (data13 - np.mean(data13)) / (np.std(data13) *len(data13))
#data14 = (data14 - np.mean(data14)) / (np.std(data14))
#cross_cor7 = np.correlate(data13,data14)
#cross_cor_arr[6] = cross_cor7[0]
#RMSE_arr[6] = round(RMSE7,2)
#MAE_arr[6] = round(MAE7,2)
sub7 = np.subtract(data13,data14)
mean_arr.append(round(sub7.mean(),3))
var_arr.append(round(sub7.var(),3))

exp_ax = ["1a", "1b", "1c", "2a", "2b", "3a", "3b"]



# data7 = np.subtract(data1,data2)
# data8 = np.subtract(data3,data4)
# data9 = np.subtract(data5,data6)

#for i in range(len(timestamps1)):
#   timestamps4.append(i)

#for i in range(len(data4)):
#    timestamps5.append(i)

# for i in range(len(timestamps3)):
#    timestamps6.append(i)


##case that the number of samples are not the same in the measurement we want to plot together

##data1.pop()
##data2.pop()
##data3.pop()
##data4.pop()
##data5.pop()
##data6.pop()


############################ plot data #################################


#plt.figure()
#plt.plot(cross_cor1)
#plt.plot(timestamps4,cross_cor2)

#print(cross_cor_arr[3])
#plt.bar(exp_ax, cross_cor_arr, width=0.2, align= 'center')
#for i, values in enumerate(cross_cor_arr):
#    plt.annotate(values, (exp_ax[i], cross_cor_arr[i]))
#plt.yscale("log")
#plt.title('Cross Correlation of MCP1 and MLXObj values')


#plt.title('Experiment 1A\n\nNormalized Cross Correlation between MCP1 and MLX Object Temperature Values')
#plt.xlabel('Samples')
#plt.ylabel('Normalized Cross-Correlation')

#ymax = cross_cor1.max()
#xpos = np.argmax(cross_cor1)
#plt.annotate(ymax, xy=(xpos, ymax))

##plt.ylim(top=5)
##plt.ylim(bottom=-4)
##plt.xlim(left=9)



#plt.figure()
#plt.plot(cross_cor2)
#plt.title('Experiment 1B\n\nNormalized Cross Correlation between MCP1 and MLX Object Temperature Values')
#plt.xlabel('Samples')
#plt.ylabel('Normalized Cross-Correlation')
#ymax = cross_cor2.max()
#xpos = np.argmax(cross_cor2)
#plt.annotate(ymax, xy=(xpos, ymax))

#plt.bar(exp_ax, RMSE_arr, width=0.2, align= 'center')
#for i, values in enumerate(RMSE_arr):
#   plt.annotate(values, (exp_ax[i], RMSE_arr[i]))

##plt.yscale("log")
#plt.title('Root Mean Square Error of MLXObj values over MCP1 values')
#plt.xlabel('Experiments')
#plt.ylabel('Values')

#plt.figure()
#plt.plot(cross_cor3)
#plt.title('Experiment 1C\n\nNormalized Cross Correlation between MCP2 and MLX Ambient Temperature Values')
#plt.xlabel('Samples')
#plt.ylabel('Normalized Cross-Correlation')
#ymax = cross_cor3.max()
#xpos = np.argmax(cross_cor3)
#plt.annotate(ymax, xy=(xpos, ymax))

#plt.bar(exp_ax, MAE_arr, width=0.2, align= 'center')
#for i, values in enumerate(MAE_arr):
#    plt.annotate(values, (exp_ax[i], MAE_arr[i]))

##plt.yscale("log")
#plt.title('Mean Absolute Error of MLXObj values over MCP1 values')
#plt.xlabel('Experiments')
#plt.ylabel('Values')

plt.figure()
#plt.plot(cross_cor4)
#plt.title('Experiment 2A\n\nNormalized Cross Correlation between MCP2 and MLX Ambient Temperature Values')
#plt.xlabel('Samples')
#plt.ylabel('Normalized Cross-Correlation')
#ymax = cross_cor4.max()
#xpos = np.argmax(cross_cor4)
#plt.annotate(ymax, xy=(xpos, ymax))

plt.bar(exp_ax, mean_arr, width=0.2, align= 'center')
for i, values in enumerate(mean_arr):
    plt.annotate(values, (exp_ax[i], mean_arr[i]))

plt.title('Mean of the difference of MCP1 - MLXObj values')
plt.xlabel('Experiments')
plt.ylabel('Values')




plt.figure()
#plt.plot(cross_cor5)
#plt.title('Experiment 2B\n\nNormalized Cross Correlation between MCP2 and MLX Ambient Temperature Values')
#plt.xlabel('Samples')
#plt.ylabel('Normalized Cross-Correlation')
#ymax = cross_cor5.max()
#xpos = np.argmax(cross_cor5)
#plt.annotate(ymax, xy=(xpos, ymax))

plt.bar(exp_ax, var_arr, width=0.2, align= 'center')
for i, values in enumerate(var_arr):
    plt.annotate(values, (exp_ax[i], var_arr[i]))

plt.title('Variance of the difference of MCP1 - MLXObj values')
plt.xlabel('Experiments')
plt.ylabel('Values')

#plt.figure()
#plt.plot(cross_cor6)
#plt.title('Experiment 3A\n\nNormalized Cross Correlation between MCP2 and MLX Ambient Temperature Values')
#plt.xlabel('Samples')
#plt.ylabel('Normalized Cross-Correlation')
#ymax = cross_cor6.max()
#xpos = np.argmax(cross_cor6)
#plt.annotate(ymax, xy=(xpos, ymax))

#plt.figure()
#plt.plot(cross_cor7)
#plt.title('Experiment 3B\n\nNormalized Cross Correlation between MCP2 and MLX Ambient Temperature Values')
#plt.xlabel('Samples')
#plt.ylabel('Normalized Cross-Correlation')
#ymax = cross_cor7.max()
#xpos = np.argmax(cross_cor7)
#plt.annotate(ymax, xy=(xpos, ymax))



plt.show()
