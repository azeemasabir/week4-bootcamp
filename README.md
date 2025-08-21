# Week 4 Bootcamp: Expense Tracker App

Welcome to the **Week 4 Bootcamp** repository! This project focuses on building a complete **Expense Tracker Dashboard** that enables users to manage their daily expenses and gain insights through data visualization.

---

## 🎯 Project Objectives

By the end of this week, you'll be able to:

* Build a dynamic dashboard for expense management.
* Perform CRUD operations (Add and Delete expenses).
* Generate reports on daily and category-wise spending.
* Visualize financial data using charts.

---

## 📚 Learning Outcomes

| What You’ll Learn   | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| CRUD Operations     | Add and delete expenses with persistence.                      |
| Data Categorization | Track expenses by category (e.g., Food, Transport, Utilities). |
| Reporting           | Generate daily spending reports and category breakdowns.       |
| Visualization       | Use charts to make data insights clear and user-friendly.      |

---

## 📝 Assigned Tasks & Deliverables

### 1. **Expense Management Dashboard**

* Add expenses with date, category, and amount.
* Delete expenses when no longer needed.
* Persist data using a lightweight database (e.g., SQLite).

### 2. **Reporting Features**

* **Daily Spending Report**: Summarize all expenses for a given day.
* **Category-Wise Report**: Show spending distribution by category.

### 3. **Graphical Visualizations**

* Implement charts (e.g., bar charts, pie charts) to:

  * Display daily totals.
  * Visualize category-based spending patterns.

---

## ⚙️ Setup & Running the Project

### Prerequisites

* **Python 3.x**
* **Flask** (or similar web framework)
* **SQLite** (for data persistence)
* **Matplotlib / Plotly / Chart.js** (for visualization)

### Installation

```bash
git clone https://github.com/azeemasabir/week4-bootcamp.git
cd week4-bootcamp
pip install -r requirements.txt
```

### Running the App

```bash
python app.py
```

* Access the dashboard at: `http://localhost:5000/`

---

## 🔍 Example Usage

1. Navigate to the **Dashboard**.
2. Add a new expense by entering:

   * **Date** (e.g., 2025-08-21)
   * **Category** (e.g., Groceries, Transport, Utilities)
   * **Amount** (e.g., 120.50)
3. View updated reports:

   * **Daily Report**: Shows all expenses for the selected day.
   * **Category Report**: Breaks down expenses by category.
4. Explore **Charts**:

   * Bar chart for daily spending.
   * Pie chart for category-wise distribution.

---

## 🧪 Testing & Verification

* Run any included tests with:

  ```bash
  pytest
  ```
* Manually verify by adding/deleting expenses and reviewing reports and charts.

---

## 🎓 Goals Recap

* **Expense Management**: Practice CRUD functionality in a real-world context.
* **Data Reporting**: Summarize spending effectively.
* **Data Visualization**: Present insights clearly with charts.
* **Full-Stack Integration**: Connect frontend forms, backend logic, database, and visualizations.

---

## 🤝 Contributing

Contributions are welcome! Fork this repository, suggest improvements, or open a pull request.
