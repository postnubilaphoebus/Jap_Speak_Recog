1. Brainstorming

Challenges:
temporal organization matters in voice recordings
time series has different lengths
examples of different classes look rather similar by visual inspection

What kind of feature extraction?
What kind of base-line model?
Filtering before feeding input data to feature extraction phase?
Remember to set up model so it overfits at first
Parameter optimization; plan to find (which) optimal parameters? 

2. Overview

Data: 
270 training recordings, 30 from each speaker
Recordings acquired over 12 channels (cepstrum coefficients)
Recording length varies between 10 and 30 timesteps
RAW DATA files: ae.train & ae.test

Task: 
Design a classification algorithm which takes as input a 12-dimensional time-series and outputs a class decision yi = { 1, …, 9}.

Code:
https://github.com/postnubilaphoebus/Jap_Speak_Recog/blob/main/README.md



3. Workflow structure

Migrate Matlab code (for importing data) to JupyterLab / Notebook


Normalize recording windows (they vary between 10 and 30 timesteps!)
- scaling?
- averaging?


How to measure precision?
- accuracy
- specificity and sensitivity for a multi-class problem!
- ROC-curve?


Dimension reduction / Feature extraction
- ANOVA
- Feature correlations
- PCA
- k-means; k++ scheme (initialization)
- Systematic Review on Github
     - Using t-SNE to view class distribution (visual representation)?
- UMAP 



What kind of model? How independent does the project have to be? (partial reliance on pre-implemented structures?)

Comparison of multiple methods -> use the best one
Baseline method: 
- DTs or random forests
- linear regression (probability output)

Summary of methods:
- linear regression (autoregression?)
- MLP
- SVM
- ANNs (e.g. CNNs)
- naive bayes
- Vector quantization
- Decision Trees?; random forests? mondrian forests?
- LSTM (suitable for time-series models)
- LSTM-CNN


Decide on a loss function:
- Baseline: quadratic?
- Otherwise: Goodfellow et al. (Deep Learning) Chapter 6.2


Decide on a regularization method
- L2-regularizer
- varying network size
- early stopping
- data augmentation (adding noise to data)





Fix a model architecture


Set up a cross-validation scheme
- semi-automated k-fold cross-validation
- leave-one-out-cross-validation


Implement training and testing subroutines
- global control parameters: 
    - learning rate
    - stopping criterion
    - initialisation scheme?

Questions:
1. What kind of built-in tools / frameworks are we allowed to use?
Example: Can we scikitlearn?
2. Is it correct that there are 12 features in this dataset corresponding to the cepstrum coefficients?
3. To what extent do we need to explain or understand the methods that we use? Are there any methods you advise against because they are too complicated?

To-Do:

1. Code migration to JupyterNotebook
- Thomas
2. Find a method to normalize recording windows
- Leanne
- Andreas (literature suggestions)
3. Look into feature extraction methods
- Laurids
4. Write abstract
- Andreas



# Jap_Speak_Recog
Project of the Machine Learning course at RUG <br />
Dataset:
https://archive.ics.uci.edu/ml/datasets/Japanese+Vowels <br />
Google Doc:
https://docs.google.com/document/d/1O5-qIBvy6kEe87fou5AGQ7VA5wKAOFOWSFszcSkFB5I/edit?usp=sharing
