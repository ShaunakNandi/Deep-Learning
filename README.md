# Training the tiny-ImageNet Dataset

### Please open [this link](https://colab.research.google.com/drive/1_0B06FOWZJ1oPuqUPF5FDtTGDskU7dfM) if the notebook does not load.

This project documents my learnings while designing and training this CNN model from scratch.

Training is done on the [Tiny ImageNet dataset](https://tiny-imagenet.herokuapp.com/)
  
So the notebook contains details of the various techniques I have tried to implement. Such as 
1. spatially seperated conv2D (reduce no. of params)
2. image aug (ImageDataGenerator class)
3. CLR (definitely helped in faster convergence)
4. progressively increasing size of input image to better train the model
5. no dense layer / FC. Replaced with conv2D and GAP

# The Utility python file

val_id.py is a python program I wrote to segregate the validation dataset (10,000 images) into their respective folders. 
Accprding to the structure of the dataset, the folder names is the class names itself. Hence, given the path to val images, 
this program reads the annotation.txt, creates the folders (200) and moves images into respective folders (50 images per folder).

- - - -

1. Trained on tiny-imagenet, Keras framework (tf backend)
2. Total no. of params: 24M (another 2M model I made, saturated at 50% val_acc)
3. val_acc: 53.56%
4. I experimented building a lot of models and this seemed to give the best result at the time. 
This particular one is inspired from res18 but I've modified it to a hybrid between res18 and a minimal amount of DenseNet concept. 
The intuition was to feed the input to every concat layer such that there's the global receptive of what the input image is. 

- - - -

TODO: 
1. I did not get to try successful implementations of class weights/ hard-mining/ soft-labelling
2. Increase the val_acc off course
