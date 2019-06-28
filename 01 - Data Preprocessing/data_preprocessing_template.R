# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

# Taking care of missing values
dataset$Age[is.na(dataset$Age)] <- mean(dataset$Age, na.rm=TRUE)
dataset$Salary[is.na(dataset$Salary)] <- mean(dataset$Salary, na.rm=TRUE)

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)