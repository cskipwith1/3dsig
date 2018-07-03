import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.metrics import auc, roc_curve, precision_recall_curve, average_precision_score, confusion_matrix

def draw_roc_curve(y_true, y_score, ax=None, annot=True, **kwargs):
    
    fpr, tpr, _ = roc_curve(y_true, y_score)
    
    if ax is None:
        ax = plt.gca()
        
    # If one isn't passed, create a label for the plot containing the AUC and, if passed, the name of the curve
    if annot:
        roc_auc = auc(fpr, tpr)
        if 'label' in kwargs:
            label = kwargs['label']
        elif 'name' in kwargs:
            name = kwargs['name']
            label = f'{name} AUC = {roc_auc:.3f}'
        else:
            label = f'AUC = {roc_auc:.3f}'
    else:
        label=None
    
    ax.plot(fpr, tpr, label=label)
    ax.set_xlabel('False positive rate')
    ax.set_ylabel('True positive rate')
    ax.legend(loc='best', fancybox=True)
    
    return ax

def draw_pr_curve(y_true, y_score, ax=None, annot=True, **kwargs):
    
    if ax is None:
        ax = plt.gca()
        
    precision, recall, _ = precision_recall_curve(y_true, y_score)
    
    # If one isn't passed, create a label for the plot containing the average precision and, if passed, the name of the curve
    # TODO add other metrics like F1 score - FB
    if annot:
        pr_score = average_precision_score(y_true, y_score)
        if 'label' in kwargs:
            label = kwargs['label']
        elif 'name' in kwargs:
            name = kwargs['name']
            label = f'{name} average precision score = {pr_score:.3f}'
        else:
            label = f'Average precision score = = {pr_score:.3f}'
    else:
        label=None
        
    ax.step(recall, precision, label=label)
    
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    
    ax.legend(loc='best')
    
    return ax

def draw_confusion_matrix(y_true, y_predicted, class_labels=None, ax=None):
    
    if ax is None:
        ax = plt.gca()
    
    cm = pd.DataFrame(confusion_matrix(y_true, y_predicted)).T
    
    if class_labels is not None:
        relabel_dict = {i: label for i, label in enumerate(class_labels)}
        cm.rename(relabel_dict, axis='index', inplace=True)
        cm.rename(relabel_dict, axis='columns', inplace=True)

    sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', square=True, linewidths=0.1, linecolor='k', cbar_kws={'shrink': 0.75}, ax=ax)
    ax.set_ylabel('Predicted class label')
    ax.set_xlabel('True class label')

    return ax
