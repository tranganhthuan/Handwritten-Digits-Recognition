# Handwritten digits recognition trained on Semeion Dataset

Models that recognise handwritten digits, including both neuro-network and non-neuro-network models. 

*Authors: Tran Son Phat, Trang Nguyen Anh Thuan*

**How to use:**

- Main.ipynb is the main file which contains out models and data processing. 

- Paint.py is the tool we use to write digits and store it as png images.

- SampleCreation.ipynb is the file used to convert image in dataset folder to a matrix in numpy array and stored as created.data.

**Results:**

| Model | Accuracy (%) | Error rate (%) |
|-|-|-|
| KNN (base model) | 90.595 | 9.405 |
| SVM | 96.865 | 3.135 |
| LRC | 93.625 | 6.375 |
| CNN (average of 10) |  |  |
| - Without distortion | 98.181 | 1.819 |
| - With distortion | 98.213 | 1.787 |
| Hybrid CNN-SVM (average of 10) | 98.526 | 1.474 |