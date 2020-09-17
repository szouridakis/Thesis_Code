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
timestamps7 = []
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []


############################ extract data from hdf5 files ###############################

for filename in glob.glob('C:/Users/stelz/Documents/Python-last/experiments/exp13/MCP1*.hdf5'):
##for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1a/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps1.append(group_key)
        data_set = hf[group_key]
        data1.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/stelz/Documents/Python-last/experiments/exp13/MLXObj*.hdf5'):
##for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1a/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps2.append(group_key)
        data_set = hf[group_key]
        data2.append(data_set[()])
    hf.close()

#for filename in glob.glob('C:/Users/stelz/Documents/Python-last/experiments/exp12/MCP1*.hdf5'):
#for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1b/MCP1*.hdf5'):
#
#    hf = h5py.File(filename, 'r')
#
#    for group_key in hf.keys():
#        timestamps3.append(group_key)
#        data_set = hf[group_key]
#        data3.append(data_set[()])
#    hf.close()

#for filename in glob.glob('C:/Users/stelz/Documents/Python-last/experiments/exp12/MCP1*.hdf5'):
#for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1b/MLXObj*.hdf5'):
#
#    hf = h5py.File(filename, 'r')
#
#    for group_key in hf.keys():
#        timestamps4.append(group_key)
#        data_set = hf[group_key]
#        data4.append(data_set[()])
#    hf.close()

#for filename in glob.glob('C:/Users/stelz/Documents/Python-last/experiments/exp12/MCP1*.hdf5'):
#for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/MCP1*.hdf5'):
#
#    hf = h5py.File(filename, 'r')
#
#    for group_key in hf.keys():
#        timestamps5.append(group_key)
#        data_set = hf[group_key]
#        data5.append(data_set[()])
#    hf.close()

#for filename in glob.glob('C:/Users/stelz/Documents/Python-last/experiments/exp12/MCP1*.hdf5'):
#for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/MLXObj*.hdf5'):
#
#    hf = h5py.File(filename, 'r')
#
#    for group_key in hf.keys():
#        timestamps6.append(group_key)
#        data_set = hf[group_key]
#        data6.append(data_set[()])
#    hf.close()

for filename in glob.glob('C:/Users/stelz/Documents/Python-last/experiments/exp13/Thermal*.hdf5'):
#for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1b/Thermal*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps5.append(group_key)
        data_set = hf[group_key]
        data5.append(data_set[()].max())
        data6.append(data_set[()].min())
    hf.close()

#for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp2a/Thermal*.hdf5'):
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


#del data1[:100]  #the first 100 samples in experiment 1B are not normal because of calibration
#del data2[:100]
#del data3[:100]
#del data4[:100]
#del data5[:100]
#del data6[:100]
#del timestamps1[:100]

#data7 = np.subtract(data1,data2)
#data8 = np.subtract(data3,data4)
#data9 = np.subtract(data5,data6)

#for i in range(len(timestamps1)):
#   timestamps7.append(i)

#for i in range(len(data1)):
#    timestamps6.append(i)

# for i in range(len(timestamps3)):
#    timestamps6.append(i)


##case that the number of samples are not the same in the measurement we want to plot together

data1.pop()
data2.pop()
##data3.pop()
##data4.pop()
#data5.pop()
#data6.pop()


############################ plot data #################################


plt.figure()

#plt.plot(timestamps7, data7, label="40 cm")
#plt.plot(timestamps7, data8, label="80 cm")
#plt.plot(timestamps7, data9, label="1 m")
plt.plot(timestamps5, data1, label="MCP1 on Object")
plt.plot(timestamps5, data2, label="MLX Object")
plt.plot(timestamps5, data5, label="Thermal Camera MAX")
##plt.plot(timestamps5, data4, label="MLX 80")
plt.legend(loc="upper right")

##plt.xlabel('Time on 2020-07-15 from 13:34:29 till 14:04:29') ##1a
##plt.xlabel('Time on 2020-07-14 from 18:37:20 till 19:07:19') ##1b remove the first 100 samples because of MLX Calibration
##plt.xlabel('Time on 2020-07-14 from 18:39:52 till 19:07:19') ##1b remove the first 100 samples because of MLX Calibration
##plt.xlabel('Time on 2020-07-15 from 14:32:47 till 15:02:46') ##1c
#plt.xlabel('Time on 2020-07-15 from 15:11:37 till 15:31:37') ##2a
##plt.xlabel('Time on 2020-07-15 from 15:39:22 till 15:59:21') ##2b
##plt.xlabel('Time on 2020-07-15 from 16:23:11 till 16:43:10') ##3a
##plt.xlabel('Time on 2020-07-15 from 16:54:04 till 17:14:03') ##3b
#plt.title('Experiment 1\n\nDifference of Object\'s Temperature Between MCP1 and MLX on Different Cases\n(MCP1 - MLXObj)')
plt.xlabel('Time')
plt.ylabel('Temperature')


#plt.ylim(top=4)
#plt.ylim(bottom=-5)
##plt.xlim(left=9)


plt.show()
