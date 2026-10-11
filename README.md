# Customer Retention & Churn Analysis

## Project Overview

Customer Retention & Churn Analysis explores customer churn patterns in the IBM Telco Customer Churn dataset. The project uses Python for data analysis and Power BI to present customer retention metrics and churn-related insights.

The goal is to understand how churn varies across contract types, tenure, payment methods, internet services, and monthly charges, then identify areas the business could investigate to improve retention.

## Objectives

- Measure customer count, churn, and retention.
- Compare churn across contract types and payment methods.
- Explore the relationship between customer tenure and churn.
- Compare churn patterns across internet service types and customer segments.
- Examine monthly charges for churned and retained customers.
- Present key findings through Power BI dashboards.

## Tools and Technologies

- **Python** — data analysis
- **Pandas** — data cleaning and manipulation
- **Matplotlib** — charts and visualizations
- **Power BI** — interactive dashboards
- **DAX** — KPI measures
- **Git and GitHub** — version control and project sharing

## Dataset

The project uses the **IBM Telco Customer Churn** dataset.

- **Customers:** 7,043
- **Columns:** 21
- **Target field:** `Churn` (`Yes` or `No`)

The dataset includes customer tenure, contract type, payment method, internet service, monthly charges, total charges, and churn status.

## Project Structure

```text
Customer-Retention-Churn-Analysis/
├── Dataset/
│   └── customer_churn..csv
├── Python/
│   └── churn_analysis.py
├── powerbi/
│   └── Customer_Retention_Churn_Dashboard.pbix
├── screenshots/
│   ├── executive_overview.png
│   ├── churn_analysis.png
│   └── retention_analysis.png
└── README.md
```

*The CSV filename has two dots before `csv` in the working project. Update the names above if your actual files or folders differ.*

## Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Customers | 7,043 |
| Churned Customers | 1,869 |
| Retained Customers | 5,174 |
| Churn Rate | 26.54% |
| Retention Rate | 73.46% |

## Dashboard Pages

### 1. Customer Retention Overview
Summarizes customer counts, churned and retained customers, churn rate, retention rate, average tenure, average monthly charges, and total customer revenue.

### 2. Churn Analysis
Explores churn by contract type, payment method, and customer tenure.

### 3. Customer Insights
Examines churn across internet service, monthly charges, tenure, payment method, and gender, along with churn rates by selected customer groups.

## Key Insights

- **Overall churn:** 1,869 of 7,043 customers churned, giving a churn rate of approximately **26.54%**.
- **Retention:** 5,174 customers were retained, equivalent to approximately **73.46%**.
- **Contract type:** Churn patterns differ by contract type. Contract-level comparisons can help identify customer groups that may need closer retention analysis.
- **Tenure:** Churn varies with customer tenure, so it is useful to compare newer customers with longer-standing customers.
- **Monthly charges:** In this dataset, churned customers generally have higher monthly charges than retained customers. This is an observed association, not proof that higher charges cause churn.
- **Payment and internet services:** Comparing churn rates across payment methods and internet service types can help identify groups for further investigation.

## Recommendations

- Investigate churn rates across contract types, especially shorter-term contracts.
- Review the early customer experience and onboarding for newer customers.
- Compare service usage, support experience, and monthly charges for churned and retained customers.
- Examine payment-method and internet-service groups with higher churn rates.
- Test retention offers or service improvements and measure their outcomes before scaling them.

## How to Run the Python Analysis

1. Install Python.
2. Open a terminal in the project root folder.
3. Install the required packages:

   ```bash
   pip install pandas matplotlib
   ```

4. Run the analysis script:

   ```bash
   python Python/churn_analysis.py
   ```

Make sure the CSV path inside the script matches the actual file location. The current dataset filename is `customer_churn..csv`.

## Open the Power BI Dashboard

Open `powerbi/Customer_Retention_Churn_Dashboard.pbix` in Power BI Desktop. If Power BI cannot locate the CSV, update the data source path to the dataset in your project folder.

## Dashboard Screenshots

Save screenshots in the `screenshots/` folder and update the filenames below to match your actual files.

![Customer Retention Overview](screenshots/executive_overview.png)

![Churn Analysis](screenshots/churn_analysis.png)

![Retention Analysis](screenshots/retention_analysis.png)

## Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory data analysis
- Customer churn and retention metrics
- KPI calculation with DAX
- Data visualization
- Power BI dashboard development
- Business insight generation
- Analytical reporting

## Limitations

The dataset does not include a customer signup date or a complete time-stamped event history. Therefore, a true calendar-based cohort retention analysis cannot be calculated from this dataset alone. Tenure-based comparisons can be used as a proxy, but should not be described as calendar cohorts.

## Conclusion

This project demonstrates how Python and Power BI can be used to measure customer churn, explore retention patterns, compare customer groups, and communicate findings through dashboards. The results can guide further investigation into customer experience and retention strategies.

**Project type:** Data Analytics / Customer Retention  
**Tools:** Python, Pandas, Matplotlib, Power BI, DAX
