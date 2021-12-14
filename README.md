Dimensionality reduction using CHi square and classification on reduced data set using SVM
1. Developed sets of methods for learning and classifying on simulated dataset of single nucleotide polymorphism (SNP) genotype data 
containing 29623 SNPs (total features).Amongst all SNPs are 15 causal 
ones which means they and neighboring ones discriminate between case and 
controls while remainder are noise.
2. Use of univariate method "Chi-square " for selecting 15 important features
3. In the training are 4000 cases and 4000 controls.
4. Trained model using SVM to perform classification.
5. Prediction of test labels

Memory issues:

One challenge with this project is the size of the data and loading it into 
RAM. Floats and numbers take up more than 4 bytes in Python because 
everything is really an object (a struct in C) that contain other 
information besides the value of the number. To reduce the space we can use 
the array class of Python.
