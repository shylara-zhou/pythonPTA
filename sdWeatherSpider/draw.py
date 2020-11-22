
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
with open("weather.txt", "r", encoding='utf8',newline='') as filereader:
    filereader = filereader.readlines()
    city=[]
    tem=[]
    for i in range(len(filereader)):
        print(filereader[i])
        a=filereader[i]
        str= a.split(' ')
        a = str[1].split('℃')
        city.append(str[0])
        tem.append(a[0])
    plt.figure(figsize=(6, 4))
    plt.title('福建各城市当日温度情况')

    plt.xlabel('城市')
    plt.ylabel('温度℃')
    plt.plot(city, tem, color='red', linewidth=2.0, linestyle='--')
    for a, b in zip(city, tem  ):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    plt.legend()
    plt.show()


