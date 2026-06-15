# 🧠 Perceptron Trick

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Perceptron-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" />
</p>

<p align="center">
  <b>Understanding the Building Block of Neural Networks by Implementing a Perceptron from Scratch</b>
</p>

---

## 🎯 Project Goal

The goal of this project is to understand how a **Perceptron** learns to classify data by implementing the algorithm from scratch using **NumPy**.

Instead of relying on Scikit-Learn's built-in Perceptron model, every important step is implemented manually to gain a deeper understanding of:

* Weights
* Bias
* Activation Functions
* Learning Rules
* Decision Boundaries

---

## 🔥 What This Project Covers

```text
Dataset Generation
        ↓
Data Visualization
        ↓
Step Activation Function
        ↓
Perceptron Learning Algorithm
        ↓
Weight Updates
        ↓
Decision Boundary
        ↓
Classification
```

---

## 📊 Dataset

The dataset is generated using:

```python
from sklearn.datasets import make_classification
```

### Dataset Configuration

| Parameter            | Value |
| -------------------- | ----- |
| Samples              | 100   |
| Features             | 2     |
| Classes              | 2     |
| Informative Features | 1     |
| Class Separation     | 10    |
| Random State         | 41    |

Since the data is **linearly separable**, it is perfect for understanding how a Perceptron works.

---

## 🧠 Perceptron Architecture

```text
Input Features
      │
      ▼
Weighted Sum
      │
      ▼
Step Activation Function
      │
      ▼
Prediction (0 or 1)
```

---

## ⚡ Activation Function

The Perceptron uses a **Step Function**:

```python
def step(z):
    if z > 0:
        return 1
    return 0
```

### Decision Rule

```text
z > 0   → Class 1
z ≤ 0   → Class 0
```

---

## 📈 Learning Rule

The weights are updated using the Perceptron Learning Rule:

```text
W = W + η(y - ŷ)X
```

Where:

| Symbol | Meaning          |
| ------ | ---------------- |
| W      | Weights          |
| η      | Learning Rate    |
| y      | Actual Output    |
| ŷ      | Predicted Output |
| X      | Input Features   |

---

## 📉 Decision Boundary

After training, the Perceptron learns a separating line:

```text
w₁x₁ + w₂x₂ + b = 0
```

which is transformed into:

```text
y = mx + b
```

and plotted to visualize the learned classification boundary.

---

## 🚀 Skills Practiced

* ✅ NumPy
* ✅ Data Visualization
* ✅ Classification
* ✅ Linear Algebra Basics
* ✅ Neural Network Fundamentals
* ✅ Machine Learning Concepts
* ✅ Decision Boundary Visualization

---

## 🎓 Key Learnings

This project helped me understand:

* How a Perceptron works internally
* Why weights are updated
* The role of bias
* Binary Classification
* Linear Separability
* How Neural Networks originated

---


<p align="center">
  ⭐ If you found this project useful, consider starring the repository!
</p>
