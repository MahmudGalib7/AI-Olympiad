# My Journey to the AI Olympiad 🚀🧠

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.20+-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5+-orange.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.2+-yellow.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

> **Documenting my progress, projects, and learning path toward AI excellence**

## 🌟 Overview

Welcome to my AI Olympiad preparation repository! This space captures my hands-on journey through the core concepts of data science, machine learning, and deep learning. I’m building projects, implementing algorithms from scratch, and solidifying my mathematical foundations to excel in the AI Olympiad competition.

## 💫 My Goals

- 🎯 Master core ML/AI algorithms and implement them from scratch
- 📚 Build a strong foundation in mathematics for AI
- 🧪 Create end-to-end projects that showcase my deep understanding of concepts
- 🏆 Qualify for and excel in the AI Olympiad competition
- 🌐 Contribute to the AI community through open-source projects

## 🛠️ Repository Structure

```
AI-Olympiad/
|
├── competitions
│ ├── contest_practical
│ └── contests_theory
├── data_analysis
│ ├── Basic
│ │ └── practice
│ │ ├── Dataset
│ │ │ ├── data.csv
│ │ │ └── new_data.csv
│ │ ├── main.py
│ │ ├── main1.py
│ │ ├── ... (main2.py to main14.py)
│ ├── notebook
│ │ ├── Dataset
│ │ │ ├── data
│ │ │ │ ├── bios.csv
│ │ │ │ ├── new_bios.csv
│ │ │ │ ├── noc_regions.csv
│ │ │ │ ├── olympics-data.xlsx
│ │ │ │ ├── results.csv
│ │ │ │ ├── results.feather
│ │ │ │ └── results.parquet
│ │ │ └── warmup-data
│ │ │ └── coffee.csv
│ │ ├── learning_numpy.ipynb
│ │ ├── learning_pandas.ipynb
│ │ └── Regular_Expression.ipynb
│ └── project
│ └── numpy-data-analyzer
│ ├── data
│ │ └── sample_data.csv
│ ├── example_app.py
│ ├── notebooks
│ │ └── analysis_examples.ipynb
│ ├── numpy_data_analyzer
│ │ ├── data_processor.py
│ │ ├── init.py
│ ├── README.md
│ ├── requirements.txt
│ ├── setup.py
│ ├── src
│ │ ├── data_processor.py
│ │ ├── models.py
│ │ ├── utils.py
│ │ └── visualizer.py
│ └── tests
│ ├── test_data_processor.py
│ └── test_visualizer.py
├── deep_learning
│ ├── computer_vision
│ ├── natural_language_processing
│ └── neural_networks
├── machine_learning
│ └── notebook
│ └── In_to_Machine_Learning.ipynb
├── math_foundations
│ ├── calculus
│ ├── linear_algebra
│ │ └── linear_algebra.pdf
│ ├── matrix
│ ├── probability
│ └── Statics
├── python
│ ├── Basic
│ ├── DSA
│ │ ├── course
│ │ ├── Hashmaps
│ │ ├── Linked List
│ │ ├── Recursion
│ │ ├── Searching Algo
│ │ ├── Sorting Algo
│ │ ├── Stack & Queue
│ │ └── Tree
│ ├── problem_solving
│ │ ├── A
│ │ ├── B
│ │ ├── C
│ │ ├── D
│ │ ├── AI-Olympiad
│ │ ├── AI-Olympiad Mock Test
│ │ ├── Course
│ │ └── Novo-contest
│ └── projects
│ └── smart_home
│ ├── automation
│ ├── core
│ ├── devices
│ ├── tests
│ ├── README.md
│ ├── requirements.txt
│ └── setup.py

```
---

## Notes

- `... (main2.py to main14.py)` is used to shorten the tree; you can expand it fully if needed.
- I used simplified file names like `linear_algebra.pdf` in place of the long UUID-style name for readability. Feel free to swap back your actual file names.

## 📊 Featured Project: NumPy Data Analyzer

My NumPy Data Analyzer project highlights my ability to implement essential data science algorithms purely with NumPy. This strengthens my mathematical intuition and helps me grasp the core logic behind modern ML techniques.

### Key Implementations:

- 🧮 **Principal Component Analysis (PCA)** - Dimensionality reduction from scratch
- 🔮 **K-Means Clustering** - Unsupervised learning algorithm
- 📊 **Statistical Analysis** - Core statistical functions without libraries
- 🔍 **Outlier Detection** - Using statistical thresholds
- 📈 **Data Visualization** - Custom charts with Matplotlib

### Sample Code:

```python
# Implementation highlight: K-means clustering from scratch
def kmeans(self, k: int = 3, max_iter: int = 100) -> Tuple[np.ndarray, np.ndarray]:
    """
    Implement K-means clustering algorithm using pure NumPy.
    """
    if self.data is None or k <= 0:
        return np.array([]), np.array([])
    
    n_samples, n_features = self.data.shape
    centroids = self.data[np.random.choice(n_samples, k, replace=False)]
    labels = np.zeros(n_samples)
    
    for _ in range(max_iter):
        distances = np.linalg.norm(self.data[:, np.newaxis] - centroids, axis=2)
        new_labels = np.argmin(distances, axis=1)
        
        if np.array_equal(new_labels, labels):
            break
        
        labels = new_labels
        for i in range(k):
            cluster_points = self.data[labels == i]
            centroids[i] = np.mean(cluster_points, axis=0) if len(cluster_points) > 0 else centroids[i]
    
    return labels, centroids
```

## 🏋️‍♂️ Current Focus

- 🧠 Implementing core ML algorithms (e.g., logistic regression, decision trees) from scratch
- ⚡ Optimizing performance in numerical computing (vectorization, broadcasting)
- 📘 Strengthening math concepts (e.g., eigenvalues, gradients, distributions)
- 🏆 Solving competition-specific challenges and datasets

## 📈 Progress Tracking

| Project                           | Status      | Skills Demonstrated                                             |
|------------------------------------|-------------|------------------------------------------------------------------|
| **NumPy Data Analyzer**            | ✅ Completed | NumPy, Statistics, Visualization, Algorithm Implementation       |
| **Neural Networks from Scratch**   | 🚧 In Progress | Backpropagation, Activation Functions, Loss Functions           |
| **Reinforcement Learning Agent**   | 📝 Planned   | Q-Learning, Policy Gradients, Environment Simulation             |

## 🔮 Future Projects

- 🖼️ **Computer Vision:** Building an image classifier without frameworks
- 🔤 **Natural Language Processing:** Creating a text classifier with pure Python
- 🎮 **Reinforcement Learning:** Implementing Q-learning and policy gradients

## 💡 Key Insights

- Understanding fundamentals unlocks true problem-solving power
- Translating math into code builds a solid AI intuition
- Debugging numerical algorithms requires patience and analytical thinking
- Optimizing code performance is a valuable competitive edge

## 🤝 Connect & Collaborate

I’d love to connect with fellow AI enthusiasts and competitors! Let’s learn, grow, and build something amazing together.

📧 **Email:** mahmudgalib2009@gmail.com  
🐙 **GitHub:** [MahmudGalib7](github.com/MahmudGalib7)  

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

<p align="center"> <strong>"The only true wisdom is in knowing you know nothing." — Socrates</strong><br> My journey of continuous learning in the fascinating world of AI 🌱 </p>
