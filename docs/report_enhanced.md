# E-Commerce Analysis for Munch’s

## Title Page
**E-Commerce Analysis for Munch’s**
*Strategies to Increase Sales and Optimize Costs*

**Prepared by:** Zain Siddiqui  
**Date:** January 2025

---

## Executive Summary

### Objective
The objective of this project is to analyze sales data from Munch’s, a fictitious online pet supply company, to identify strategies for increasing sales and reducing costs.

### Key Findings
1. **Sales Trends**: Sales consistently peaked in Q1 and Q4, driven by holiday and promotional events.
2. **Product Insights**: Dog Food is the top-selling product and often purchased with Dog Toys, suggesting strong cross-selling opportunities.
3. **Regional Performance**: The East region outperformed other regions, contributing 50% of total sales, while the West region underperformed.

### Recommendations
1. Upsell Dog Food with complementary products like Dog Toys.
2. Target underperforming regions (West and South) with localized promotions.
3. Optimize inventory based on seasonal demand, particularly in Q4.
4. Launch bundled offers to capitalize on frequently purchased combinations.

---

## 1. Introduction
This project analyzes transactional data from Munch’s to uncover sales trends, customer preferences, and regional performance. By identifying actionable insights, Munch’s can enhance its revenue, improve operational efficiency, and better serve its customers.

---

## 2. Data Preparation

### Dataset Overview
The dataset includes transaction records, product details, and customer information with the following key attributes:
- **OrderID**: Unique identifier for each transaction.
- **CustomerID**: Unique identifier for each customer.
- **ProductName**: Name of the purchased product.
- **Category**: Product category.
- **Price**: Price of the product.
- **Quantity**: Quantity purchased.
- **OrderDate**: Date of the transaction.
- **Region**: Regional data of the transaction.

### Data Cleaning Process
The dataset was cleaned using Python with the following steps:
1. Removed duplicate entries to ensure data accuracy.
2. Standardized date formats for consistency.
3. Addressed missing values by replacing them with relevant defaults.

---

## 3. Data Analysis

### 3.1 Sales Trends
- **Finding**: Sales peaked in Q1 and Q4, with December being the highest revenue month due to holiday promotions.
- **Visualization**: The Sales Analysis dashboard in Tableau revealed seasonal spikes, emphasizing the importance of targeted promotional campaigns.

### 3.2 Product Insights
- **Finding**: Dog Food accounted for 40% of total sales and is frequently purchased alongside Dog Toys. This highlights a strong opportunity for cross-selling and bundling strategies.
- **Visualization**: A Tableau highlight table ranked products by revenue, showing Dog Food as the clear leader.

### 3.3 Regional Performance
- **Finding**: The East region outperformed others, contributing 50% of sales, while the West region lagged behind. Regional performance disparities suggest the need for region-specific campaigns.
- **Visualization**: A Tableau map dashboard illustrated regional sales distribution, with the East region dominating.

---

## 4. Market Basket Analysis

### Methodology
Market basket analysis was conducted using the Apriori algorithm to identify product associations and frequently purchased combinations. The analysis utilized cleaned transactional data.

### Results
- **Top Product Associations**:
  - Dog Food and Dog Toys had a lift value of 3.5, indicating a strong relationship.
  - Cat Litter and Cat Food had a lift value of 2.8, suggesting bundling opportunities.

- **Visualization**: Results were tabulated and visualized in Tableau to highlight product combinations and their lift values.

---

## 5. Recommendations

### Upsell Opportunities
- **Action**: Promote bundled offers for Dog Food and Dog Toys, offering a 10% discount when purchased together.
- **Impact**: Increases average order value and encourages repeat purchases.

### Target Underperforming Regions
- **Action**: Run targeted promotional campaigns in the West and South regions to boost sales.
- **Impact**: Reduces regional disparities and increases overall revenue.

### Seasonal Promotions
- **Action**: Focus on Q4 sales by launching holiday-themed marketing campaigns and limited-time offers.
- **Impact**: Maximizes revenue during the peak shopping season.

### Inventory Optimization
- **Action**: Stock high-demand products, such as Dog Food, based on seasonal trends.
- **Impact**: Reduces stockouts and improves customer satisfaction.

---

## 6. Conclusion
This analysis provides actionable insights for Munch’s to increase revenue, optimize costs, and enhance customer satisfaction. By implementing the recommended strategies, Munch’s can capitalize on existing strengths while addressing weaknesses to achieve sustained growth.

---

## 7. Appendices

### Tableau Dashboards
- **Sales Analysis**: Visualizing sales trends over time.
- **Product Insights**: Highlighting top-selling products and their patterns.
- **Regional Performance**: Mapping regional sales distribution.

### Supporting Files
- Python Scripts:
  - `clean_data.py`: Script for cleaning and preprocessing the dataset.
  - `market_basket_analysis.py`: Script for conducting market basket analysis.
- Market Basket Analysis Results:
  - `market_basket_output.csv`: Contains product association insights.

---

This report was created as part of an E-Commerce Analysis project using Python and Tableau. For detailed visualizations, refer to the Tableau workbook and dashboards included in the project folder.

