import foolbox
import os
from model import Model
import tensorflow as tf

from foolbox import zoo


def create():
    weights_path = zoo.fetch_weights(
        'https://www.dropbox.com/s/ywc0hg8lr5ba8zd/secret.zip?dl=1',
        unzip=True
    )
    weights_path = os.path.join(weights_path, 'models/model_0/')

    model = Model('eval')

    sess = tf.Session().__enter__()
    saver = tf.train.Saver()
    checkpoint = tf.train.latest_checkpoint(weights_path)
    saver.restore(sess, checkpoint)

    images = model.x_input
    logits = model.pre_softmax

    fmodel = foolbox.models.TensorFlowModel(images, logits, bounds=(0, 255))

    return fmodel
