import numpy as np
import matplotlib.pyplot as plt
import dezero
from dezero import optimizers
from dezero import Model
import dezero.functions as F
import dezero.layers as L
from dezero import DataLoader


max_epoch = 100
batch_size = 30
hidden_size = 10
lr = 1.0

train_set = dezero.datasets.Spiral(train=True)
test_set = dezero.datasets.Spiral(train=False)
train_loader = DataLoader(train_set, batch_size)
test_loader = DataLoader(test_set, batch_size, shuffle=False)

class TwoLayerNet(Model):
    def __init__(self, hidden_size, out_size):
        super().__init__()
        self.l1 = L.Linear(hidden_size)
        self.l2 = L.Linear(out_size)
        self.bn1 = L.BatchNorm()

    def forward(self, x):
        y = F.sigmoid(self.bn1(self.l1(x)))
        y = self.l2(y)
        return y


model = TwoLayerNet(hidden_size, 3)
optimizer = optimizers.SGD(lr).setup(model)

for epoch in range(max_epoch):
    for x, t in train_loader:
        y = model(x)
        loss = F.softmax_cross_entropy(y, t)
        model.cleargrads()
        loss.backward()
        optimizer.update()
    if epoch % 10 == 0:
        print('loss:', loss.data)

# Plot
x = np.array([example[0] for example in train_set])
t = np.array([example[1] for example in train_set])
h = 0.001
x_min, x_max = x[:, 0].min() - .1, x[:, 0].max() + .1
y_min, y_max = x[:, 1].min() - .1, x[:, 1].max() + .1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
X = np.c_[xx.ravel(), yy.ravel()]

with dezero.test_mode():
    score = model(X)
predict_cls = np.argmax(score.data, axis=1)
Z = predict_cls.reshape(xx.shape)
plt.contourf(xx, yy, Z)

N, CLS_NUM = 100, 3
markers = ['o', 'x', '^']
colors = ['orange', 'blue', 'green']
for i in range(len(x)):
    c = t[i]
    plt.scatter(x[i][0], x[i][1],s=40,  marker=markers[c], c=colors[c])
plt.show()