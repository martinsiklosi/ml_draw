import tensorflow as tf
from tensorflow import keras
from settings import *

# get data
# kika på https://www.tensorflow.org/tutorials/load_data/images
(train_images, train_labels), (test_images, test_labels) = \
    keras.datasets.mnist.load_data()

# setup model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(GRID_SIZE, GRID_SIZE)),
    keras.layers.Dense(392, activation=tf.nn.relu),
    keras.layers.Dense(392, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax),
])

model.compile(
    optimizer=tf.optimizers.Adam(),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# train model
model.fit(train_images, train_labels, epochs=5)

# save model
model.save('model')
