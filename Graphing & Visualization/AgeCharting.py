import random
import matplotlib.pyplot as plt
from faker import Faker

fake = Faker()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def ReturnInfo(self):
        return self.name, self.age

def CreateRandomPeople(times):
    people = []
    for i in range(times):
        person = Person(fake.name(), random.randint(1, 99))
        people.append(person)

    namesArr = []
    ageArr = []

    for person in people:
        namesArr.append(person.name)
        ageArr.append(person.age)

    return namesArr, ageArr

def SortPeople(namesArr, ageArr):
    for i in range(len(ageArr)):
        for j in range(len(ageArr)):
            if ageArr[i] < ageArr[j]:
                temp = ageArr[i]
                ageArr[i] = ageArr[j]
                ageArr[j] = temp

                temp = namesArr[i]
                namesArr[i] = namesArr[j]
                namesArr[j] = temp

    return namesArr, ageArr

def PlotArrays(names, ages):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Sort names and ages together
    sorted_data = sorted(zip(names, ages), key=lambda x: x[1])
    sortedNamesArr, sortedAgeArr = zip(*sorted_data)

    ax1.bar(names, ages)
    ax1.set_xlabel('Names')
    ax1.set_ylabel('Ages')
    ax1.set_xticklabels(names, fontsize=6)
    ax1.set_yticks([0, 20, 40, 60, 80])  # Set custom y-axis tick values
    ax1.set_yticklabels([0, 20, 40, 60, 80], fontsize=6)  # Set custom y-axis tick labels
    ax1.set_title('Names and Ages')

    ax2.bar(sortedNamesArr, sortedAgeArr)
    ax2.set_xlabel('Names')
    ax2.set_ylabel('Ages')
    ax2.set_xticklabels(sortedNamesArr, fontsize=6)
    ax2.set_yticks([0, 20, 40, 60, 80])  # Set custom y-axis tick values
    ax2.set_yticklabels([0, 20, 40, 60, 80], fontsize=6)  # Set custom y-axis tick labels
    ax2.set_title('Sorted Names and Ages')

    plt.tight_layout()
    plt.show()

namesArr, ageArr = CreateRandomPeople(10)
PlotArrays(namesArr, ageArr)
