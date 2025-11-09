# 🧩 Customer Segmentation using K-Means Clustering

## 📄 Project Overview
This project demonstrates how to use **unsupervised learning** for customer segmentation.  
Using the **Mall Customers dataset**, the model identifies distinct customer groups based on:
- Age  
- Annual Income  
- Spending Score  

The goal is to uncover **hidden patterns in customer behavior** and help businesses make data-driven marketing decisions.

---

## ⚙️ Technologies Used
- **Python**
- **Pandas**
- **Matplotlib**
- **Scikit-learn (KMeans, StandardScaler)**
- **Joblib**

---

## 🧮 Steps Involved
1. Load and explore the dataset  
2. Select relevant features (`Age`, `Annual Income`, `Spending Score`)  
3. Scale data using `StandardScaler`  
4. Use the **Elbow Method** to find the optimal number of clusters  
5. Train the **KMeans model**  
6. Visualize the clusters using **Matplotlib**  
7. Assign human-readable labels to clusters  
8. Save model for future predictions  

---

## 📊 Example Cluster Interpretation
| Cluster | Label | Description |
|----------|--------|-------------|
| 0 | Average Spenders | Older, moderate income and spending |
| 1 | Young Affluent Spenders | Young, high income and high spending |
| 2 | Young Impulsive Shoppers | Young, low income but high spending |
| 3 | Careful Young Buyers | Young, mid income and cautious spending |
| 4 | Wealthy Low Spenders | Older, high income but low spending |

---
