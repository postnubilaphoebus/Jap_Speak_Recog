# Jap_Speak_Recog
Project of the Machine Learning course at RUG <br />
Dataset:
https://archive.ics.uci.edu/ml/datasets/Japanese+Vowels <br />
Google Doc documenting work flow (not cleaned):
https://docs.google.com/document/d/1O5-qIBvy6kEe87fou5AGQ7VA5wKAOFOWSFszcSkFB5I/edit?usp=sharing


This project used:
Python 2.7.18, Keras 2.4.3, scipy 1.3.1, scikit-learn 0.24.1

## Abstract
In this work, we present the results of our Machine Learning project for the Japanese Vowels dataset. For this project, we used a real-life dataset containing spectral recordings of vocal utterances of the Japanese vowels /ae/, recorded from nine male speakers. The task is to match each multidimensional time series with the correct speaker. We compared various preprocessing methods in conjunction with state-of-the-art classifiers and found that resampling the recordings to an equal length using cubic spline interpolation improves classification performance significantly over all classification models. The best performance was obtained by an ensemble of 11 separately trained Long Short Term Memory architectures in combination with cubic spline interpolation and subsequent resampling to an equal length of 26 time steps for each recording, yielding a training accuracy of 99.82% and a testing accuracy of 98.86%.
