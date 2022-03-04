from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Acc = TP + TN / TP + TN + FP + FN
# Precission = TP / TP + FP
# Recall = TP / TP + FN

# For this example
# TP (negative class) = 2
# TP (zero class) = 1
# TP (positive class) = 4

# FP (negative class) = 1
# FP (zero class) = 2
# FP (positive class) = 3

# FN (negative class) = 3
# FN (zero class) = 3
# FN (positive class) = 0

# Precision = number of correctly computed numbers / number of all predicted numbers of respective class
# Recall = number of correctly computed numbers / numbers of all actual numbers of respective class

real_labels =     [0, 1, 2, 1, 0, 0, 1, 0, 2, 2, 1, 0, 2]
computed_labels = [0, 2, 2, 1, 0, 2, 2, 1, 2, 2, 0, 1, 2]
label_names = ['negative (class 0)', 'zero (class 1)', 'positive (class 2)']

# Confusion matrix
print(confusion_matrix(real_labels, computed_labels))

# Precision and recall
print(classification_report(real_labels, computed_labels, target_names=label_names))