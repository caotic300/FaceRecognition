# A Face Emotion Recognition Pipeline 

## Description
We developed a pipeline that is able to predict emotion recognition, different computer vision algori.

The purpose of this pipeline was to be able to predict face emotion recognition based on emotion recognition images. The dataset contains a number of images that can contain the following labels.

Label explanation:
1: Surprise
2: Fear
3: Disgust
4: Happiness
5: Sadness
6: Anger
7: Neutral



## Requirements 
    opencv-python==4.4.0.46
    scikit-image==0.18.3
    Keras==2.4.3
    tensorflow==2.8.0
    numpy==1.19.2
    matplotlib=3.3.2
    pandas==1.1.3
    seaborn==0.11.0
    scikit-learn==0.24.2
    torch==1.10.2
    scipy==1.4.1

    
## Installation
The requirements.txt file describes the dependencies used during the project. 

### Installing using the requirements.txt file
Run the requirements.txt file using the directory path

```
pip install -r path/to/requirements.txt
```


### Installing manually using pip
In order to run the project the following steps must be followed.
1. Install python
 
2. Install open cv library
```
    pip install opencv-python==4.4.0.46
```

2. Install scikit-image library
```
    python -m pip install -U scikit-image
```

3.Install numpy 
```
    pip install numpy
```

4. Install pandas
```
    pip install pandas
```


5. Install seaborn
```
    pip install seaborn
```

6. Install scikit-learn
```
    pip install -U scikit-learn
```

7. Install pytorch
```
    pip3 install torch torchvision
```

8. Install tensorflow
```
    pip install --upgrade tensorflow
```

9. Install matplotlib
```
   python -m pip install -U matplotlib
```

10. Install Keras
```
    pip install keras
```

11. Install scipy
```
    pip install scipy  
```

## Usage
The pipeline was created using google collab.
The different models were saved in order to predict the different images. 
We tested different architectures of the Convolutional Neural Network and Multi-layer Perceptron Neural Network and compare the different results achieved.

### Project Structure
    The project structure is contained by the following subsystems:
- CW_Dataset, contain the dataset of images and labels
- Personal Dataset, contain a personal dataset of images and labels
- Models, contain the different models used in different jupyter notebooks
- requirements.txt, contains the different dependencies used in the project 
