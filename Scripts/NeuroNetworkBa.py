import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2'
import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers
from tensorflow import keras
from tensorflow.keras.layers.experimental import preprocessing


class NeuroNetwork:

    trainData = 0;
    trainData_Label = 0;
    testData = 0;
    testData_Label = 0;

    def __init__(self, trainData,testData):
        self.trainData = trainData
        self.testData = testData

    """Function Data will be manipulatet Data get ascending numbers daly HIGH and daly LOW curse"""
    def manipulateData(self):
        print("Manipulate Data!")
        self.trainData['Date'] = self.trainData.index
        self.trainData = self.trainData.drop(['Open', 'Close','Adj Close','Volume'], axis=1)
        self.labelData()
        print(self.trainData)
 #TODO label Data muss noch implementiert werden
    """Function Data get labeld / test and train Data"""
    def labelData(self):
        print("label Data!")


#TODO create Model muss noch angepasst werden stimmt noch nicht Code noch nicht ausführbar!
    def createModel(self):
        model = keras.Sequential(
            [
                keras.Input(shape=(2)),
                layers.Dense(400, activation='relu'),  # First layer
                layers.Dense(300, activation='relu'),  # Second layer
                layers.Dense(200, activation='relu'),  # Third layer
                layers.Dense(3),  # Output Layer sind ja 2 Outputs
            ]
        )
        print(model.summary())


        model.compile(
            loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            # Loss Function das Modell wird diese Funktion minimieren
            optimizer=keras.optimizers.Adam(lr=0.001),  # Optimierer entscheidet wie gelernt wird
            metrics=["accuracy"]  #
        )
        # Konkretisiere das Training
        model.fit(self.trainData, self.labelData_Train, batch_size=26515, epochs=2000, verbose=2)
        model.save('saved_model')
        print("-----------")
        model.evaluate(self.inputData_Test, self.labelData_Test, batch_size=26515, verbose=2)  # Progress bar
        # Treffe eine Vorhersage

        prob_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
        predict = prob_model.predict(self.inputData_Test)
        self.predModel = predict

        print(predict)  # Ausgabe was Netz denkt
        #Speichere Netz ab
        #np.savetxt("foo.csv", predict, delimiter=",")

