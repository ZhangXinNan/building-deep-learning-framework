<p>
<a href="https://www.amazon.co.jp/dp/4873119065/ref=cm_sw_r_tw_dp_U_x_KiA1Eb39SW14Q"><img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/deep-learning-from-scratch-3.png" height="250"></a>
</p>

## 本书简介

本书创建了一个深度学习框架——DeZero。DeZero是本书原创的框架，它用最少的代码实现了现代深度学习框架的功能。DeZero是一个小而强大的框架，我们将通过60个步骤来完成它。在这一过程中，读者会加深对PyTorch、Chainer和TensorFlow等现代深度学习框架的理解。

<p>
<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/dezero_logo.png" width="400px" </p>


<p>
  <a href="https://pypi.python.org/pypi/dezero"><img
		alt="pypi"
		src="https://img.shields.io/pypi/v/dezero.svg"></a>
  <a href="https://github.com/oreilly-japan/deep-learning-from-scratch-3/blob/master/LICENSE.md"><img
		alt="MIT License"
		src="http://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://travis-ci.org/oreilly-japan/deep-learning-from-scratch-3"><img
		alt="Build Status"
		src="https://travis-ci.org/oreilly-japan/deep-learning-from-scratch-3.svg?branch=master"></a>
</p>

## 新消息
<a href="https://www.ituring.com.cn/book/2863"><img src="https://raw.githubusercontent.com/koki0702/koki0702.github.io/master/dezero-book/images/summary_ja.png" height="150px"></a>

【试读】本书的部分内容可在线阅读。
https://www.ituring.com.cn/book/2863

## 文件夹的内容

|文件夹名 |说明         |
|:--        |:--                  |
|[dezero](/dezero)       |DeZero的源代码|
|[examples](/examples)     |使用DeZero开发的示例|
|[steps](/steps)|各步骤的代码文件（step01.py ~ step60.py）|
|[tests](/tests)|DeZero的单元测试|


## 所需的外部库

本书使用的Python版本和外部库如下所示。

- [Python 3](https://docs.python.org/3/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

另外DeZero还提供了可在NVIDIA的GPU上运行的可选功能。此时需要安装下面的库。

- [CuPy](https://cupy.chainer.org/) （可选）


## 运行方法

本书所讲解的Python文件主要在[steps](/steps)文件夹中。
可以通过以下Python命令运行这些文件（可以在任何目录下运行Python命令）。

```
$ python steps/step01.py
$ python steps/step02.py

$ cd steps
$ python step31.py
```

## 代码示例

DeZero的其他实现示例在[examples](/examples)。

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_tanh.png" height="175"/>](/examples/tanh.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_spiral.png" height="175"/>](/examples/spiral.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_gpu.png" height="175"/>](/examples/mnist_colab_gpu.ipynb)

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/gan.gif" height="175"/>](/examples/gan.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/vae.png" height="175"/>](/examples/vae.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/grad_cam.png" height="175"/>](/examples/grad_cam.py)

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/style_transfer.png" height="175"/>](/examples/style_transfer.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/pythonista.png" height="175"/>](https://github.com/oreilly-japan/deep-learning-from-scratch-3/wiki/DeZero%E3%82%92iPhone%E3%81%A7%E5%8B%95%E3%81%8B%E3%81%99)

## 勘误信息

本书的勘误信息汇总在[勘误页面](https://www.ituring.com.cn/book/2863)。

如果您发现任何未列在勘误页面上的错字或其他错误，请在勘误页面[提交勘误](https://www.ituring.com.cn/book/2863)。
