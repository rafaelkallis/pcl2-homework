#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Vorlage
# Uebung 5, Aufgabe 2
"""This module uses a naive bayes classifier to identify the gender of names"""

import random
import collections
from nltk.metrics import precision, recall, f_measure
from nltk.classify import NaiveBayesClassifier, accuracy
from functools import reduce


class NaiveBayesClassifierNameGenderPrediction:
    """This class implements the naive bayes classification on gender 
    recognition of names"""

    def __init__(self, female_file, male_file):
        self.male_file = male_file
        self.female_file = female_file

        self.main()

    @staticmethod
    def extract_data(data_file):
        """extract the given data file"""
        extracted_file = open(data_file, 'r', encoding='utf-8')
        extracted_file = extracted_file.read()
        splitted_file = extracted_file.split('\n')
        splitted_file.pop()
        return splitted_file

    @staticmethod
    def evaluation(test_set, classifier):
        """Evaluate the classifier with the test set. Print the accuracy,
        precision, recall and f-measure."""
        refsets = collections.defaultdict(set)
        testsets = collections.defaultdict(set)

        for i, (feats, label) in enumerate(test_set):
            refsets[label].add(i)
            observed = classifier.classify(feats)
            testsets[observed].add(i)

        print('Accuracy:', accuracy(classifier, test_set))
        print('Precision:', precision(refsets['MALE'], testsets['MALE']))
        print('Recall:', recall(refsets['MALE'], testsets['MALE']))
        print('F Measure:', f_measure(refsets['MALE'], testsets['MALE']))

    @staticmethod
    def gender_features(name):
        """Return a dictionary with all features to identify the gender of
        a name"""
        order_a = 0
        for ind, x in enumerate(name):
            if x == 'a':
                order_a += ind + 1

        return {
            'order_a': order_a,
            'second_last_char': name[-2],
            'last_char': name[-1]
        }

    def get_training_and_test_labeled_features(self, female_training_data,
                                               male_training_data,
                                               female_test_data,
                                               male_test_data):
        """return a labeled dictionary of all features for the training
        and test data"""
        training_list = []
        testing_list = []
        for male_name in male_training_data:
            training_list.append(
                (NaiveBayesClassifierNameGenderPrediction.gender_features(male_name), 'MALE'))
        for female_name in female_training_data:
            training_list.append(
                (NaiveBayesClassifierNameGenderPrediction.gender_features(female_name), 'FEMALE'))

        for male_name in male_test_data:
            testing_list.append(
                (NaiveBayesClassifierNameGenderPrediction.gender_features(male_name), 'MALE'))
        for female_name in female_test_data:
            testing_list.append(
                (NaiveBayesClassifierNameGenderPrediction.gender_features(female_name), 'FEMALE'))

        return (training_list, testing_list)

    @staticmethod
    def get_train_and_test_data(male_data, female_data):
        """Split the male and female data into training and test data."""
        male_test_data = []
        female_test_data = []
        for _ in range(100):
            male_test_data.append(male_data.pop(
                random.randint(0, len(male_data) - 1)))
            female_test_data.append(female_data.pop(
                random.randint(0, len(female_data) - 1)))

        return (male_data, male_test_data, female_data, female_test_data)

    def main(self):
        male_data = self.extract_data(self.male_file)
        female_data = self.extract_data(self.female_file)

        male_train_data, male_test_data, female_train_data, female_test_data = \
            self.get_train_and_test_data(male_data, female_data)

        # get the training and test set for the classifier and the evaluation
        train_set, test_set = self.get_training_and_test_labeled_features(
            female_train_data, male_train_data, female_test_data,
            male_test_data)

        # create classifier with the training set
        classifier = NaiveBayesClassifier.train(train_set)

        # print the evaluation with the precision, recall and f-measure
        self.evaluation(test_set, classifier)

        # print the 10 most informative features
        # classifier.show_most_informative_features(10)


if __name__ == '__main__':
    NaiveBayesClassifierNameGenderPrediction('aufgabe2/female.txt',
                                             'aufgabe2/male.txt')
