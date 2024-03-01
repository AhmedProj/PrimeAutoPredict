# PrimeAutoPredict

Project devoted to the developement of a deep learning model to predict the total claims payments by the insurance company. The project includes as well its deployment for production.


The goal is to compute a yearly third party premium (material + bodily injury) for the 36,311 contracts of the
pricing dataset, for 2011. The formula we'll be using for premium computation: cost multiplied by frequency (Cost * Frequency). 

To achieve this, we'll develop four models:

1- Model for material cost estimation.
2- Model for bodily injury cost estimation.
3- Model for material incident frequency prediction.
4- Model for bodily injury occurrence frequency prediction.
