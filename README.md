<p align="center">
  <img src="https://github.com/mahimai-raja/NUS_007/blob/main/logo/image.JPG" width="12000" height="300" />
</p>


<h2 align="center" ><b>
  Parkinson's disease prediction with Hand-drawn spiral images.<b\>
</h2>

## Project done by :

-> Akshita Verma <br>
-> Arpan Malik <br>
-> Hirshikesh Akilan <br>
-> Hriddhima Singh <br>
-> Ishita Gupta <br>
-> Mahimai Raja

## About

This is the official project repository of the team 7 for National University of Singapore, GAIP.

## Technologies

* [Python 3](https://www.python.org)
* [Tensorflow 2.1.8 / Keras](https://www.tensorflow.org)
* [scikit-learn](https://scikit-learn.org/stable/)
* [OpenCV](https://opencv.org)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Matplotlib](https://matplotlib.org)

## Parkinson's Disease : 
<p> Parkinson's disease is a brain disorder that causes unintended or uncontrollable movements, such as shaking, stiffness, and difficulty with balance and coordination. Symptoms usually begin gradually and worsen over time. As the disease progresses, people may have difficulty walking and talking.</p>



##Deep Learning Approach

Several models were trained for this task (as a learning experience). Ultimately, the Convolution Neural Network (CNN) approach was chosen as the best of all when compared to other model's performance.

* The image dataset was augumented using keras libraries and they we preprocessed using OpenCV libraries.
* Using the preprocessed data an convolutional neural network was developed with a single layer of 512 neurons and several dropout layers.

## Acknowledgements

The image data folder was downloaded from an article on [pyimagesearch](https://www.pyimagesearch.com/2019/04/29/detecting-parkinsons-disease-with-opencv-computer-vision-and-the-spiral-wave-test/) which provides the author's own approach using machine learning algorithms on this data set. Few of the computer vision techniques were revised from his post. Originally the dataset is curated by Adriano de Oliveira Andrade and Joao Paulo Folado from the NIATS of Federal University of Uberlândia. 
