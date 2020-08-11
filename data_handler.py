import h5py
import matplotlib.pyplot as plt
import glob
import os

timestamps1 = []
timestamps2 = []
data1 = []
data2 = []

for filename in glob.glob('C:/Users/stelz/Documents/Python-last/exp1/MLXObj*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps1.append(group_key)
        data_set = hf[group_key]
        data1.append(data_set[()])

for filename in glob.glob('C:/Users/stelz/Documents/Python-last/exp1/MCP1*.hdf5'):

    hf = h5py.File(filename, 'r')

    for group_key in hf.keys():
        timestamps2.append(group_key)
        data_set = hf[group_key]
        data2.append(data_set[()])

plt.figure()

plt.plot(timestamps1, data1, label="MLX")
plt.plot(timestamps1, data2, label="MCP")
plt.legend(loc="upper right")

plt.title('change over time')
plt.xlabel('time')
plt.ylabel('temperature')

plt.show()