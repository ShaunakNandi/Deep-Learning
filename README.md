# Deep-Learning

so the notebook contains details of the various techniques I have tried to implement. Such as 
0. spatially seperated conv2D (reduce no. of params)
1. image aug (ImageDataGenerator class)
2. CLR (definitely helped in faster convergence)
3. progressively increasing size of input image to better train the model
4. no dense layer / FC. Replaced with conv2D and GAP

TODO: I did not get to try successful implementations of class weights

This was the first time I went really hands on with training a model (that too from scratch!!). So it's a start.
Really happy with this project though, even though this is far from the best models I've seen developed by peers in the competitve class I participated in.

--
0. trained on tiny-imagenet
1. total no. of params: 24M (a 2M model saturated at 50% val_acc)
2. val_acc: 53.56%
3. I experimented building a lot of models and this seemed to give the best result at the time. 
This particular one is inspired from res18 but I've modified it to a hybrid between res18 and a minimal amount of DenseNet concept. 
The intuition was to feed the input to every concat layer such that there's the global receptive of what the input image is. 

