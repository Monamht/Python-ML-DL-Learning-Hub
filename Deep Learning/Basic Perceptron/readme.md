# 🧠 Perceptron Fundamentals | Deep Learning Learning Journey

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Deep%20Learning-Beginner-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Topic-Perceptron-orange?style=for-the-badge">
</p>

<p align="center">
  <b>My first step into Neural Networks and Deep Learning 🚀</b>
</p>

---

# 🌱 Why This Notebook?

This notebook is part of my **Deep Learning Learning Journey**.

Instead of jumping directly into Neural Networks, CNNs, and Transformers, I wanted to understand the most fundamental building block:

> 🧠 **The Perceptron**

This notebook focuses on understanding the intuition behind how a machine learns to classify data using weights, bias, and a decision boundary.

---

# 🎯 What I Explored

```text
Artificial Neuron
        ↓
Perceptron
        ↓
Weights & Bias
        ↓
Activation Function
        ↓
Decision Boundary
        ↓
Binary Classification
```

---

# 📚 Concepts Covered

## ✅ What is a Perceptron?

The Perceptron is the simplest form of an Artificial Neural Network.

It takes input features, applies weights and bias, and predicts one of two classes.

---

## ✅ Synthetic Dataset Generation

Generated a linearly separable dataset using:

```python
make_classification()
```

to understand how classification works from scratch.

---

## ✅ Data Visualization

Visualized:

* Class 0
* Class 1
* Feature Distribution

to build intuition about the dataset before training.

---

## ✅ Perceptron Training

Implemented and trained a Perceptron model using:

```python
from sklearn.linear_model import Perceptron
```

---

## ✅ Understanding Model Parameters

Explored:

```python
p.coef_
p.intercept_
```

and understood how they represent:

* Weights
* Bias

learned during training.

---

## ✅ Decision Boundary

Visualized the line learned by the Perceptron:

```text
w₁x₁ + w₂x₂ + b = 0
```

which separates the two classes.

---

# 🛠️ Libraries Used

```python
NumPy
Matplotlib
Scikit-Learn
mlxtend
```

---

# 🧠 Key Learnings

✔️ Binary Classification

✔️ Linear Separability

✔️ Artificial Neurons

✔️ Activation Functions

✔️ Decision Boundaries

✔️ Weights & Bias

✔️ Perceptron Learning

✔️ Foundations of Neural Networks

---

# 🚀 Learning Path

This notebook is part of my roadmap:

```text
Perceptron
     ↓
Neural Networks
     ↓
Backpropagation
     ↓
Gradient Descent
     ↓
Deep Neural Networks
     ↓
CNNs
     ↓
RNNs
     ↓
Transformers
```


# 💡 Takeaway

> Understanding the Perceptron is like learning the alphabet before writing sentences.

Every modern Deep Learning architecture—from CNNs to Large Language Models—is built upon the same core ideas of neurons, weights, activations, and learning.

---

<p align="center">
🚀 Learning Deep Learning One Concept at a Time
</p>

<p align="center">
⭐ If you're also learning ML/DL, feel free to follow along!
</p>
