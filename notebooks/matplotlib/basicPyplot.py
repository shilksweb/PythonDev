import matplotlib.pyplot as plt

x1=[1,2,8]
y1=[5,7,4]

x2=[5,7,4]
y2=[1,2,8]

plt.plot(x1, y1, label='FirstLine')
plt.plot(x2, y2, label='SecondLine')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('My Graph')

plt.legend()

plt.show()