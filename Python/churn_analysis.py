import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/customer_churn..csv")

# Clean data
df.columns = df.columns.str.strip()
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)

# ==============================
# DATASET INFORMATION
# ==============================
print("===== DATASET SHAPE =====")
print(df.shape)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# ==============================
# KEY PERFORMANCE INDICATORS
# ==============================
total_customers = df["customerID"].nunique()
churned_customers = (df["Churn"] == "Yes").sum()
retained_customers = (df["Churn"] == "No").sum()

churn_rate = churned_customers / total_customers * 100
retention_rate = retained_customers / total_customers * 100

print("\n===== KEY PERFORMANCE INDICATORS =====")
print(f"Total Customers: {total_customers:,}")
print(f"Churned Customers: {churned_customers:,}")
print(f"Retained Customers: {retained_customers:,}")
print(f"Churn Rate: {churn_rate:.2f}%")
print(f"Retention Rate: {retention_rate:.2f}%")
print(f"Average Tenure: {df['tenure'].mean():.2f} months")
print(f"Average Monthly Charges: ${df['MonthlyCharges'].mean():,.2f}")
print(f"Total Customer Revenue: ${df['TotalCharges'].sum():,.2f}")

# ==============================
# CHURN BY CONTRACT
# ==============================
contract_churn = pd.crosstab(
    df["Contract"], df["Churn"], normalize="index"
) * 100

print("\n===== CHURN BY CONTRACT (%) =====")
print(contract_churn.round(2))

# ==============================
# CHURN BY PAYMENT METHOD
# ==============================
payment_churn = pd.crosstab(
    df["PaymentMethod"], df["Churn"], normalize="index"
) * 100

print("\n===== CHURN BY PAYMENT METHOD (%) =====")
print(payment_churn.round(2))

# ==============================
# CHURN BY INTERNET SERVICE
# ==============================
internet_churn = pd.crosstab(
    df["InternetService"], df["Churn"], normalize="index"
) * 100

print("\n===== CHURN BY INTERNET SERVICE (%) =====")
print(internet_churn.round(2))

# ==============================
# CHURN BY TENURE GROUP
# ==============================
def tenure_group(months):
    if months <= 12:
        return "0-12 Months"
    elif months <= 24:
        return "13-24 Months"
    elif months <= 48:
        return "25-48 Months"
    return "49+ Months"

df["Tenure Group"] = df["tenure"].apply(tenure_group)

tenure_order = [
    "0-12 Months",
    "13-24 Months",
    "25-48 Months",
    "49+ Months"
]

tenure_churn = pd.crosstab(
    df["Tenure Group"], df["Churn"], normalize="index"
) * 100

tenure_churn = tenure_churn.reindex(tenure_order)

print("\n===== CHURN BY TENURE GROUP (%) =====")
print(tenure_churn.round(2))

# ==============================
# CHART 1: CHURN DISTRIBUTION
# ==============================
df["Churn"].value_counts().plot(kind="bar", figsize=(7, 5))
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==============================
# CHART 2: CHURN BY CONTRACT
# ==============================
pd.crosstab(df["Contract"], df["Churn"]).plot(
    kind="bar", figsize=(8, 5)
)
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==============================
# CHART 3: CHURN RATE BY TENURE
# ==============================
tenure_churn["Yes"].plot(kind="bar", figsize=(8, 5))
plt.title("Churn Rate by Customer Tenure")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==============================
# CHART 4: MONTHLY CHARGES VS CHURN
# ==============================
df.boxplot(column="MonthlyCharges", by="Churn", figsize=(8, 5))
plt.title("Monthly Charges by Churn Status")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.show()

print("\n===== ANALYSIS COMPLETED =====")
