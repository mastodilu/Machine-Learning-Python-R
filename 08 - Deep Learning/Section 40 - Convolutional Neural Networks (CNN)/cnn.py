# Convolutional Neural Network

# Importing the Keras libraries and packages
from keras.models import Sequential # inizializza CNN (come >sequenza di layer< o come grafo)
from keras.layers import Convolution2D # step 1: convoluzione (2D per le immagini)
from keras.layers import MaxPooling2D # step 2: max pooling (per riconoscere una feature in maniera più flessibile)
from keras.layers import Flatten # step 3: flattening (si crea il vettore di feature per l'input della rete)
from keras.layers import Dense # step 4: usato per aggiungere il layer fully connected alla rete

"""
per il training set e il test set non possiamo più usare una tabella con i dati
scritti per riga, ma usiamo cartelle diverse che contengono le immagini di cani 
e gatti. Inoltre ogni immagine ha nel nome la classe giusta, tipo gatto_n.jpeg
deve essere classificata come gatto.
"""

# Initialising the CNN
# sequential inizializza la CNN come stack di layer
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
"""
Convolution2D:
    filters: Integer, the dimensionality of the output space
        (i.e. the number of output filters in the convolution).    
    kernel_size: An integer or tuple/list of 2 integers, specifying the
        height and width of the 2D convolution window. Can be a single integer to specify the same value for all spatial dimensions
Input shape:
    4D tensor with shape: (batch, channels, rows, cols) if data_format is "channels_first" or 4D tensor with shape:
        (batch, rows, cols, channels) if data_format is "channels_last".
activation:
    Activation function to use (relu è quella non lineare ____/¯¯¯)
    
32, (3, 3), indica 32 filter matrix grandi 3x3 --> la rete sarà composta da 32 feature maps
(64, 64, 3) indica la forma dell'immagine di input. Perchè tutto funzioni dobbiamo prima convertire le immagini a questa esatta dimensione.
        (l'ordine dei parametri è invertito perchè stiamo usando tensorflow)
"""

# Step 2 - Pooling
# effettua max pooling con una matrice 2x2
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer and max pooling it
classifier.add(Convolution2D(32, (3, 3), activation = 'relu')) # input_shape non è necesario qua
classifier.add(MaxPooling2D(pool_size = (2, 2)))

"""
# prova e vedi le performance
classifier.add(Convolution2D(64, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
"""

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))    # hidden layer fully connected (nota che usa Dense)
                                                                # 128 è scelto abbastanza a naso, ed è una potenza di 2 del numero di nodi di input (64)
classifier.add(Dense(units = 1, activation = 'sigmoid')) # output node

# Compiling the CNN
"""
compile serve a configurare il modello per fare il training
    binary_crossentropy va bene perchè abbiamo un output binario cane/gatto,
    se così non fosse dovremmo usate categorical_crossentropy
"""
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# Part 2 - Fitting the CNN to the images

"""
con ImageDataGenerator possiamo applicare il rescale alle immagini per cambiarne
la dimensione, ma possiamo anche applicare delle trasformazioni in modo da poter
usare una stessa immagine lievemente modificata (ruotata, stirata,..) per 
eseguire un training più completo del modello
"""
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255, # assegna ad ogni pixel un valore compreso tra 0 e 1
                                   shear_range = 0.2,
                                   zoom_range = 0.2, # applica uno zoom casuale
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

# crea il training set
training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64), # dimensione dell'immagine passata
                                                 batch_size = 1, # quante immagini contemporaneamente vengono passate alla CPU (o GPU)
                                                 class_mode = 'binary') # binary perchè cane/gatto

# crea il test set
test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 1,
                                            class_mode = 'binary')

classifier.fit_generator( training_set,
                         steps_per_epoch = training_set.samples, # 8000
                         epochs = 25,
                         validation_data = test_set,
                         validation_steps = test_set.samples) # 2000

# acc: precisione del training_set
# val_acc: precision del test_set