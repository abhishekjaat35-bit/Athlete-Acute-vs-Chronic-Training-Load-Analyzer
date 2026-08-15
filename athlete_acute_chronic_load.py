import pandas as pd
import matplotlib.pyplot as plt


print("=" * 80)
print("          ATHLETE ACUTE VS CHRONIC TRAINING LOAD ANALYZER")
print("=" * 80)


# ------------------------------------------
# Load Data
# ------------------------------------------

data = pd.read_csv("training_load_data.csv")

data["Date"] = pd.to_datetime(data["Date"])

data = data.sort_values(
    ["Athlete", "Date"]
).reset_index(drop=True)


# ------------------------------------------
# Calculate Acute Load
# ------------------------------------------
# Acute load = 7-session rolling total

data["Acute_Load_7"] = (
    data.groupby("Athlete")["Training_Load"]
    .transform(
        lambda x: x.rolling(
            window=7,
            min_periods=7
        ).sum()
    )
)


# ------------------------------------------
# Calculate Chronic Load
# ------------------------------------------
# Chronic load = 28-session rolling average
#
# It represents the athlete's longer-term
# training-load reference.

data["Chronic_Load_28"] = (
    data.groupby("Athlete")["Training_Load"]
    .transform(
        lambda x: x.rolling(
            window=28,
            min_periods=28
        ).mean()
    )
)


# ------------------------------------------
# Calculate Acute:Chronic Ratio
# ------------------------------------------

data["Acute_Chronic_Ratio"] = (
    data["Acute_Load_7"]
    /
    (data["Chronic_Load_28"] * 7)
)


# ------------------------------------------
# Classify Load Ratio
# ------------------------------------------

def classify_ratio(ratio):

    if pd.isna(ratio):
        return "Insufficient Baseline"

    elif ratio < 0.80:
        return "Lower Load"

    elif ratio <= 1.30:
        return "Reference Range"

    else:
        return "Higher Load"


data["Load_Status"] = (
    data["Acute_Chronic_Ratio"]
    .apply(classify_ratio)
)


# ------------------------------------------
# Display Raw Data
# ------------------------------------------

print("\n" + "=" * 80)
print("TRAINING LOAD DATA")
print("=" * 80)

print(data.to_string(index=False))


# ------------------------------------------
# Display Calculated Analysis
# ------------------------------------------

print("\n" + "=" * 80)
print("ACUTE VS CHRONIC LOAD ANALYSIS")
print("=" * 80)

display_columns = [
    "Athlete",
    "Date",
    "Training_Load",
    "Acute_Load_7",
    "Chronic_Load_28",
    "Acute_Chronic_Ratio",
    "Load_Status"
]

print(
    data[display_columns].to_string(
        index=False,
        formatters={
            "Acute_Load_7":
                lambda x:
                "N/A" if pd.isna(x)
                else f"{x:.1f}",

            "Chronic_Load_28":
                lambda x:
                "N/A" if pd.isna(x)
                else f"{x:.1f}",

            "Acute_Chronic_Ratio":
                lambda x:
                "N/A" if pd.isna(x)
                else f"{x:.2f}"
        }
    )
)


# ------------------------------------------
# Athlete Summary
# ------------------------------------------

athlete_summary = (
    data.groupby("Athlete")
    .agg(
        Sessions=("Training_Load", "count"),
        Total_Load=("Training_Load", "sum"),
        Average_Load=("Training_Load", "mean"),
        Maximum_Load=("Training_Load", "max"),
        Minimum_Load=("Training_Load", "min")
    )
    .reset_index()
)


print("\n" + "=" * 80)
print("ATHLETE TRAINING LOAD SUMMARY")
print("=" * 80)

print(
    athlete_summary.to_string(
        index=False,
        formatters={
            "Average_Load":
                "{:.1f}".format
        }
    )
)


# ------------------------------------------
# Valid Ratio Summary
# ------------------------------------------

valid_ratios = data.dropna(
    subset=["Acute_Chronic_Ratio"]
)


print("\n" + "=" * 80)
print("LOAD RATIO SUMMARY")
print("=" * 80)

if len(valid_ratios) > 0:

    print(
        f"Average Ratio : "
        f"{valid_ratios['Acute_Chronic_Ratio'].mean():.2f}"
    )

    print(
        f"Minimum Ratio : "
        f"{valid_ratios['Acute_Chronic_Ratio'].min():.2f}"
    )

    print(
        f"Maximum Ratio : "
        f"{valid_ratios['Acute_Chronic_Ratio'].max():.2f}"
    )

else:

    print("Insufficient data for ratio calculation.")


# ------------------------------------------
# Status Summary
# ------------------------------------------

status_summary = (
    data["Load_Status"]
    .value_counts()
    .reset_index()
)

status_summary.columns = [
    "Load_Status",
    "Observations"
]


print("\n" + "=" * 80)
print("LOAD STATUS SUMMARY")
print("=" * 80)

print(
    status_summary.to_string(index=False)
)


# ------------------------------------------
# Highest Training Load
# ------------------------------------------

highest_load = data.loc[
    data["Training_Load"].idxmax()
]


print("\n" + "=" * 80)
print("HIGHEST TRAINING LOAD")
print("=" * 80)

print(
    f"Athlete : {highest_load['Athlete']}"
)

print(
    f"Date    : {highest_load['Date'].date()}"
)

print(
    f"Load    : {highest_load['Training_Load']} AU"
)


# ------------------------------------------
# Visualization 1
# Acute and Chronic Load
# ------------------------------------------

plt.figure(figsize=(11, 6))

for athlete in data["Athlete"].unique():

    athlete_data = data[
        data["Athlete"] == athlete
    ]

    plt.plot(
        athlete_data["Date"],
        athlete_data["Training_Load"],
        marker="o",
        label=f"{athlete} Daily Load"
    )

plt.title("Athlete Training Load Trend")
plt.xlabel("Date")
plt.ylabel("Training Load (AU)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig(
    "acute_chronic_load_trend.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Visualization 2
# Acute:Chronic Ratio
# ------------------------------------------

plt.figure(figsize=(11, 6))

for athlete in data["Athlete"].unique():

    athlete_data = data[
        data["Athlete"] == athlete
    ]

    plt.plot(
        athlete_data["Date"],
        athlete_data["Acute_Chronic_Ratio"],
        marker="o",
        label=athlete
    )

plt.axhline(
    1.00,
    linestyle="--",
    label="Reference = 1.00"
)

plt.title("Acute:Chronic Training Load Ratio")
plt.xlabel("Date")
plt.ylabel("Acute:Chronic Ratio")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig(
    "load_ratio_trend.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Export Complete Analysis
# ------------------------------------------

data.to_csv(
    "training_load_analysis.csv",
    index=False
)


# ------------------------------------------
# Final Output
# ------------------------------------------

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)

print("Files created:")
print("1. training_load_analysis.csv")
print("2. acute_chronic_load_trend.png")
print("3. load_ratio_trend.png")

print("\n" + "=" * 80)
print("MONITOR LOAD • ANALYZE TRENDS • INFORM TRAINING")
print("=" * 80)