# Lecture 5 - Neural Networks

## Convolution
Convolution refers to a technique that tries to enhance the most relevant
features of an image, while degrading the values of the not so important
pixels.

Convolution is a step of big importance in convolutional neural networks, since
it allows the algorithm to work with less information about the image, while
keeping the most important stuff present during the process. In CNN the
convolution process is commonly the first step, via a convolution layer. In
libraries like Tensorflow, a convolution layer is set to have n filters, and
during the training process the neural network learns which filters are the
best fit for that particular problem.

### Filters
A filter is a matrix of nxn, that is going to be applied to the whole pixels of
an image. From an analitical perspective, a filter's job is to change the value
of the pixels by applying some mathematical operations, in this operations is
where more important features receive bigger values, while the other pixels get
lower values, making them less important.

Once the filter has been applied we get a new image, hopefully with the
features we care about, highlighted. There are important values to define when
applying a convolution layer, one of them are the "strides", which is a fancy
word to define the 'steps' (in pixels) that the filter will be moved once it
has finished its application on a particular zone of the image.

### Tensorflow's Conv2D layer
Via tensorflow's documentation, the Conv2D layer is the best option to perform
convolution, specially when in the first stages of the neural network.

## Pooling
Pooling is a technique intended to reduce the size of an image. Specially used
in convolutional neural networks after a convolution process, it is of great
importance since after convolution we might end with many pixels with no
relevant value anymore, hence pooling attempts to reduce the size of the
picture by taking away those pixels and keeping the important ones.

There are 3 man types of pooling techniques:
- max pooling
- mean pooling
- sum pooling

Max pooling is the most popular one. The way it works is by getting the maximum
pixel value in a particular zone, and assign it to its correspondent pixel in
the new image.

### Tensorflow's MaxPooling2D layer
Tensorflow's documentation specifies this layer as the goto layer when polling
images.

## Resources
- https://www.tensorflow.org/tutorials/images/cnn
- https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D
- https://missinglink.ai/guides/tensorflow/tensorflow-maxpool-working-cnn-max-pooling-layers-tensorflow/
- https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D

