import random
import matplotlib.pyplot as plt

def CreateRandomArray():
    arr = []
    for i in range(1, 200):
        arr.append(random.randint(1, 1000))
    return arr

def SmoothArray(arr, runTimes):
    for i in range(0, runTimes):
        for j in range(1, len(arr) - 1):
            arr[j] = (arr[j - 1] + arr[j] + arr[j + 1]) / 3
    return arr

def PlotArray(arr, subplot):
    plt.subplot(subplot)
    plt.plot(arr)

snapArr = CreateRandomArray()

plt.figure(figsize=(24, 4))

plt.subplot(161)
PlotArray(snapArr, 161)

plt.subplot(162)
PlotArray(SmoothArray(snapArr.copy(), 1), 162)

plt.subplot(163)
PlotArray(SmoothArray(snapArr.copy(), 2), 163)

plt.subplot(164)
PlotArray(SmoothArray(snapArr.copy(), 5), 164)

plt.subplot(165)
PlotArray(SmoothArray(snapArr.copy(), 10), 165)

plt.subplot(166)
PlotArray(SmoothArray(snapArr.copy(), 20), 166)

plt.tight_layout()
plt.show()
  