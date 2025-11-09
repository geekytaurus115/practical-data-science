
# 🧠 Customer Segmentation using K-Means Clustering

## 📋 Project Overview

This project demonstrates **unsupervised learning** by performing **customer segmentation** using the **K-Means clustering algorithm**.
The goal is to identify distinct customer groups based on features such as **Age**, **Annual Income**, and **Spending Score** from the *Mall Customers Dataset*.

---

## 🎯 Objective

Segment customers into meaningful groups so that businesses can:

* Understand customer behavior.
* Design personalized marketing campaigns.
* Optimize resource allocation and product targeting.

---

## ⚙️ What is K-Means Clustering?

**K-Means** is an **unsupervised machine learning algorithm** used to group similar data points into **K distinct clusters**.
It minimizes the **intra-cluster variance** — ensuring that points in the same cluster are close together, while clusters themselves are well-separated.

---

## 🧩 How K-Means Works (Step-by-Step)

1. **Select number of clusters (K)** — decide how many groups you want.
2. **Initialize centroids** — randomly select K points as starting centers.
3. **Assign points to nearest centroid** — based on Euclidean distance.
4. **Update centroids** — compute the mean of points in each cluster.
5. **Repeat** steps 3–4 until centroids stop moving (convergence).

🧮 **Objective Function:**

$$
J = \sum_{i=1}^{k} \sum_{x_j \in C_i} \|x_j - \mu_i\|^2
$$


The algorithm tries to minimize this sum of squared distances.

---

## ✅ Why K-Means?

| Strength                     | Description                                         |
| ---------------------------- | --------------------------------------------------- |
| **Simple & Efficient**       | Easy to implement, fast on large datasets           |
| **Interpretable Results**    | Cluster centers provide clear insights              |
| **Scalable**                 | Works well with numerical and high-dimensional data |
| **Well-known & widely used** | Common baseline for segmentation problems           |

---

## ⚠️ Limitations of K-Means

| Limitation                            | Impact                                                             |
| ------------------------------------- | ------------------------------------------------------------------ |
| Must predefine **K**                  | Need to determine optimal K using methods like Elbow or Silhouette |
| Sensitive to **outliers**             | Outliers can distort cluster centroids                             |
| Works best for **spherical clusters** | Struggles with complex or varying-density data                     |
| **Hard assignments only**             | Each point belongs to exactly one cluster (no probabilities)       |

---

## 💡 Alternative Clustering Algorithms

| Algorithm                        | Key Idea                               | Strength                                | Best Use Case                                   |
| -------------------------------- | -------------------------------------- | --------------------------------------- | ----------------------------------------------- |
| **Hierarchical Clustering**      | Builds a tree (dendrogram) of clusters | No need to predefine K; interpretable   | Small datasets; when you want cluster hierarchy |
| **DBSCAN**                       | Groups dense points, marks outliers    | Handles arbitrary shapes; detects noise | Spatial / noisy data                            |
| **Gaussian Mixture Model (GMM)** | Uses probabilistic clustering          | Models overlapping/elliptical clusters  | When clusters overlap                           |
| **Mean Shift**                   | Finds dense regions automatically      | Detects any shape; no K needed          | When K is unknown; small data                   |
| **Spectral Clustering**          | Uses graph theory & eigenvalues        | Works with complex structures           | Non-linear or graph-like data                   |

---

## 🧭 Why Choose K-Means for This Project

* Dataset is small (≈200 rows) and **numeric** — ideal for K-Means.
* The goal is **simple, interpretable customer groups**.
* **Fast convergence** and **easy visualization** (2D/3D plots).
* Great starting point to understand **unsupervised learning** concepts.

---

## 📈 Evaluation Methods

* **Elbow Method:** To determine optimal `k` by observing the point where inertia starts to flatten.
* **Silhouette Score:** To evaluate how well clusters are separated.

---

## 🧮 Tools & Libraries Used

* **Python**
* **Pandas** — Data handling
* **Matplotlib** — Visualization
* **Scikit-learn** — KMeans, scaling, metrics, PCA

---


