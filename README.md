# Understanding Bias in Yelp Reviews


Following is a brief overview of the project, for more details the
[report](report.pdf) can be consulted.

Yelp reviews can be manually labelled by users as useful as a way to
filter what is informative and what is not for others. However, is there
bias in this labelling process? Research indicates that humans can be
easily swayed by other indicators outside of the utility of a piece of
information in other scenarios. A Naive Bayes classifier, a Linear SVM
classifier, and a random forest classifier were used to construct four
separate models that attempt to predict whether a review was useful. It
was found that the model that used review text, previous useful vote
count, and cool vote count provided the most accurate results,
highlighting that users are biased by things outside of review text when
labelling a review as useful. Additionally, while literature uses random
forest classifiers to achieve an accuracy of 95%, an accuracy of 99% was
achieved here with a Linear SVM classifier.

# Team Members
  - Adele Chui\
  University of Waterloo\
  Department of Systems Design Engineering\
  aschui@edu.uwaterloo.ca
  - Arumoy Shome\
  University of Waterloo\
  Department of Systems Design Engineering\
  ashome@edu.uwaterloo.ca
