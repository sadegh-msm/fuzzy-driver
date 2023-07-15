# fuzzy-driver
> self driving car with fuzzy logic

Certainly! Here's an example README.md file that provides an overview of the code and instructions on how to use it:

# Fuzzy Logic Controllers

This repository contains two fuzzy logic controllers implemented in Python: `FuzzyController` and `FuzzyGasController`. These controllers use fuzzy logic principles to make decisions based on input variables and predefined fuzzy sets.

## FuzzyController

The `FuzzyController` class implements a fuzzy logic controller for rotation control based on left and right distances. It follows the following steps:

1. **Fuzzification**: The `fuzzify` method calculates the membership values of the left and right distances in different fuzzy sets (`close_L`, `close_R`, `moderate_L`, `moderate_R`, `far_L`, and `far_R`).
2. **Inference**: The `inference` method combines the fuzzy sets obtained from fuzzification and determines the degrees of membership for different output sets (`low_right`, `high_right`, `low_left`, `high_left`, and `nothing`).
3. **Defuzzification**: The `defuzzify` method calculates the center of gravity of the fuzzy output set by evaluating the membership values of different rotation angles. It returns the defuzzified value, representing the final decision of the fuzzy controller.
4. **Decide**: The `decide` method serves as the entry point for the fuzzy controller. It takes the left and right distances as inputs, performs fuzzification, inference, and defuzzification steps, and returns the final decision (defuzzified value) of the fuzzy controller.

## FuzzyGasController

The `FuzzyGasController` class implements a fuzzy logic controller for gas control based on the center distance. It follows a similar structure to the `FuzzyController` class but with different membership functions and rules. Here are the steps:

1. **Fuzzification**: The `fuzzify` method calculates the membership values of the center distance in different fuzzy sets (`close`, `moderate`, and `far`).
2. **Inference**: The `inference` method combines the fuzzy sets obtained from fuzzification and determines the degrees of membership for different output sets (`low`, `medium`, and `high`).
3. **Defuzzification**: The `defuzzify` method calculates the center of gravity of the fuzzy output set by evaluating the membership values of different speed levels. It returns the defuzzified value, representing the final decision of the fuzzy controller.
4. **Decide**: The `decide` method serves as the entry point for the fuzzy controller. It takes the center distance as input, performs fuzzification, inference, and defuzzification steps, and returns the final decision (defuzzified value) of the fuzzy controller.

## Usage

To use the fuzzy logic controllers in your project, follow these steps:

1. Import the necessary modules:

```python
import numpy as np
```

2. Instantiate a `FuzzyController` or `FuzzyGasController` object:

```python
controller = FuzzyController()  # or FuzzyGasController()
```

3. Call the `decide` method, providing the required input values:

```python
decision = controller.decide(left_dist, right_dist)  # or center_dist
```

4. The `decision` variable will hold the final decision (defuzzified value) of the fuzzy controller.

Make sure to update the input variables (`left_dist`, `right_dist`, `center_dist`) with appropriate values based on your specific scenario.

## Example

Here's a simple example demonstrating the usage of the `FuzzyController`:

```python
controller = FuzzyController()
left_dist = 40
right_dist = 55
decision = controller.decide(left_dist, right_dist)
print(f"The rotation decision is: {decision}")
```

This will output the rotation decision based on the provided left and right distances.

