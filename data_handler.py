import h5py
import matplotlib.pyplot as plt
import glob

timestamps1 = []
timestamps2 = []
timestamps3 = []
timestamps4 = []
data1 = []
data2 = []
data3 = []
data4 = []

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/DHThi*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps1.append(group_key)
        data_set = hf[group_key]
        data1.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/DHTtemp*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps2.append(group_key)
        data_set = hf[group_key]
        data2.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/MCP2*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps3.append(group_key)
        data_set = hf[group_key]
        data3.append(data_set[()])
    hf.close()

for filename in glob.glob('C:/Users/Stelios/Desktop/Thesis/experiments/exp1c/MLXAmb*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps4.append(group_key)
        data_set = hf[group_key]
        data4.append(data_set[()])
    hf.close()

plt.figure()

plt.plot(timestamps1, data1, label="DHT Heat Index")
plt.plot(timestamps1, data2, label="DHT Temperature")
plt.plot(timestamps1, data3, label="MCP Ambient ")
plt.plot(timestamps1, data4, label="MLX Ambient ")
plt.legend(loc="upper right")

plt.title('Experiment 1C\n\nChange of Ambient Temperature in Each Sensor')
##plt.xlabel('Time on 2020-07-15 from 13:34:29 till 14:04:29') ##1a
##plt.xlabel('Time on 2020-07-14 from 18:37:20 till 19:07:19') ##1b
plt.xlabel('Time on 2020-07-15 from 14:32:47 till 15:02:46') ##1c
##plt.xlabel('Time on 2020-07-15 from 15:11:37 till 15:31:37') ##2a
##plt.xlabel('Time on 2020-07-15 from 15:39:22 till 15:59:21') ##2b
##plt.xlabel('Time on 2020-07-15 from 16:23:11 till 16:43:10') ##3a
##plt.xlabel('Time on 2020-07-15 from 16:54:04 till 17:14:03') ##3b
plt.ylabel('Temperature')

plt.show()