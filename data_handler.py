import h5py
import matplotlib.pyplot as plt
import glob
import numpy as np

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

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp3a/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps1.append(group_key)
        data_set = hf[group_key]
        data1.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp3a/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        data_set = hf[group_key]
        data2.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp3b/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps2.append(group_key)
        data_set = hf[group_key]
        data3.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp3b/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        data_set = hf[group_key]
        data4.append(data_set[()])
    hf.close()

#for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/MCP1*.hdf5'):
#
#    hf = h5py.File(filename, 'r')
#
#    for group_key in hf.keys():
#        timestamps3.append(group_key)
#        data_set = hf[group_key]
#        data5.append(data_set[()])
#    hf.close()
#
#for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/MLXObj*.hdf5'):
#
#    hf = h5py.File(filename, 'r')
#
#    for group_key in hf.keys():
#        data_set = hf[group_key]
#        data6.append(data_set[()])
#    hf.close()

data7 = np.subtract(data1,data2)
data8 = np.subtract(data3,data4)
##data9 = np.subtract(data5,data6)

for i in range(len(timestamps1)):
    timestamps4.append(i)

for i in range(len(timestamps2)):
    timestamps5.append(i)

#for i in range(len(timestamps3)):
#    timestamps6.append(i)


#for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp2b/Thermal*.hdf5'):
#
#    hf = h5py.File(filename, 'r')
#
#    for group_key in hf.keys():
#        timestamps5.append(group_key)
#        data_set = hf[group_key]
#        data5.append(data_set[()].max())
#        data6.append(data_set[()].min())
#    hf.close()


##data1.pop()
##data2.pop()
##data3.pop()
##data4.pop()
##data5.pop()
##data6.pop()

plt.figure()
##plt.plot(timestamps3, data3)

plt.plot(timestamps4, data7, label="40 cm ")
plt.plot(timestamps4, data8, label="80 cm ")
##plt.plot(timestamps4, data9, label="1  m ")
##plt.plot(timestamps4, data1, label="MCP1 40")
##plt.plot(timestamps4, data2, label="MLX 40")
##plt.plot(timestamps5, data3, label="MCP1 80")
##plt.plot(timestamps5, data4, label="MLX 80")
plt.legend(loc="upper right")

plt.title('Experiment 3\n\nDifference of Object\'s Temperature Between MCP1 and MLX On Different Cases\n(MCP1 - MLXObj)')
##plt.xlabel('Time on 2020-07-15 from 13:34:29 till 14:04:29') ##1a
##plt.xlabel('Time on 2020-07-14 from 18:37:20 till 19:07:19') ##1b
##plt.xlabel('Time on 2020-07-15 from 14:32:47 till 15:02:46') ##1c
##plt.xlabel('Time on 2020-07-15 from 15:11:37 till 15:31:37') ##2a
##plt.xlabel('Time on 2020-07-15 from 15:39:22 till 15:59:21') ##2b
##plt.xlabel('Time on 2020-07-15 from 16:23:11 till 16:43:10') ##3a
##plt.xlabel('Time on 2020-07-15 from 16:54:04 till 17:14:03') ##3b
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.ylim(top=5)
plt.ylim(bottom=-4)
##plt.xlim(left=9)

plt.show()