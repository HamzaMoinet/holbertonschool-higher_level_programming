#!/usr/bin/env python3
import json
import pickle

class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename,'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, Exception) as e:
            print(f"Deserialization error: {e}")
            return None
