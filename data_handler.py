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
        #timestamps2.append(group_key)
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


cross_cor1 = np.correlate(data1, data2)
RMSE1 = metrics.mean_squared_error(data1, data2, squared="False")
MAE1 = metrics.mean_absolute_error(data1, data2)
cross_cor_arr[0] = cross_cor1[0]
RMSE_arr[0] = round(RMSE1,2)
MAE_arr[0] = round(MAE1,2)

cross_cor2 = np.correlate(data3, data4)
RMSE2 = metrics.mean_squared_error(data3, data4, squared="False")
MAE2 = metrics.mean_absolute_error(data3, data4)
cross_cor_arr[1] = cross_cor2[0]
RMSE_arr[1] = round(RMSE2,2)
MAE_arr[1] = round(MAE2,2)

cross_cor3 = np.correlate(data5, data6)
RMSE3 = metrics.mean_squared_error(data5, data6, squared="False")
MAE3 = metrics.mean_absolute_error(data5, data6)
cross_cor_arr[2] = cross_cor3[0]
RMSE_arr[2] = round(RMSE3,2)
MAE_arr[2] = round(MAE3,2)

cross_cor4 = np.correlate(data7, data8)
RMSE4 = metrics.mean_squared_error(data7, data8, squared="False")
MAE4 = metrics.mean_absolute_error(data7, data8)
cross_cor_arr[3] = cross_cor4[0]
RMSE_arr[3] = round(RMSE4,2)
MAE_arr[3] = round(MAE4,2)

cross_cor5 = np.correlate(data9, data10)
RMSE5 = metrics.mean_squared_error(data9, data10, squared="False")
MAE5 = metrics.mean_absolute_error(data9, data10)
cross_cor_arr[4] = cross_cor5[0]
RMSE_arr[4] = round(RMSE5,2)
MAE_arr[4] = round(MAE5,2)

cross_cor6 = np.correlate(data11, data12)
RMSE6 = metrics.mean_squared_error(data11, data12, squared="False")
MAE6 = metrics.mean_absolute_error(data11, data12)
cross_cor_arr[5] = cross_cor6[0]
RMSE_arr[5] = round(RMSE6,2)
MAE_arr[5] = round(MAE6,2)

cross_cor7 = np.correlate(data13, data14)
RMSE7 = metrics.mean_squared_error(data13, data14, squared="False")
MAE7 = metrics.mean_absolute_error(data13, data14)
cross_cor_arr[6] = cross_cor7[0]
RMSE_arr[6] = round(RMSE7,2)
MAE_arr[6] = round(MAE7,2)

exp_ax = ["1a", "1b", "1c", "2a", "2b", "3a", "3b"]



# data7 = np.subtract(data1,data2)
# data8 = np.subtract(data3,data4)
# data9 = np.subtract(data5,data6)

#for i in range(len(timestamps1)):
#   timestamps4.append(i)

# for i in range(len(timestamps2)):
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


plt.figure(1)
#plt.plot(timestamps4,cross_cor2)

#print(cross_cor)
#print(RMSE)
#print(MAE)

plt.bar(exp_ax, cross_cor_arr, width=0.2, align= 'center')

for i, values in enumerate(cross_cor_arr):
    plt.annotate(values, (exp_ax[i], cross_cor_arr[i]))

plt.yscale("log")
plt.title('Cross Correlation of MCP1 and MLXObj values')

##plt.plot(timestamps4, data7, label="40 cm ")
##plt.plot(timestamps4, data8, label="80 cm ")
##plt.plot(timestamps4, data9, label="1  m ")
##plt.plot(timestamps4, data1, label="MCP1 40")
##plt.plot(timestamps4, data2, label="MLX 40")
##plt.plot(timestamps5, data3, label="MCP1 80")
##plt.plot(timestamps5, data4, label="MLX 80")
##plt.legend(loc="upper right")

#plt.title('Experiment 3A\n\n')
##plt.xlabel('Time on 2020-07-15 from 13:34:29 till 14:04:29') ##1a
##plt.xlabel('Time on 2020-07-14 from 18:37:20 till 19:07:19') ##1b
##plt.xlabel('Time on 2020-07-15 from 14:32:47 till 15:02:46') ##1c
##plt.xlabel('Time on 2020-07-15 from 15:11:37 till 15:31:37') ##2a
##plt.xlabel('Time on 2020-07-15 from 15:39:22 till 15:59:21') ##2b
##plt.xlabel('Time on 2020-07-15 from 16:23:11 till 16:43:10') ##3a
##plt.xlabel('Time on 2020-07-15 from 16:54:04 till 17:14:03') ##3b
plt.xlabel('Experiments')
plt.ylabel('Values')
##plt.ylim(top=5)
##plt.ylim(bottom=-4)
##plt.xlim(left=9)



plt.figure(2)

plt.bar(exp_ax, RMSE_arr, width=0.2, align= 'center')
for i, values in enumerate(RMSE_arr):
    plt.annotate(values, (exp_ax[i], RMSE_arr[i]))

##plt.yscale("log")
plt.title('Root Mean Square Error of MLXObj values over MCP1 values')
plt.xlabel('Experiments')
plt.ylabel('Values')

plt.figure(3)

plt.bar(exp_ax, MAE_arr, width=0.2, align= 'center')
for i, values in enumerate(MAE_arr):
    plt.annotate(values, (exp_ax[i], MAE_arr[i]))

##plt.yscale("log")
plt.title('Mean Absolute Error of MLXObj values over MCP1 values')
plt.xlabel('Experiments')
plt.ylabel('Values')
plt.show()
