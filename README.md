# Athlete Acute vs Chronic Training Load Analyzer

A Python sports analytics project designed to explore short-term and longer-term training-load patterns using rolling windows.

## Objective

The project calculates:

- Daily training load
- Seven-session acute load
- Twenty-eight-session chronic training-load reference
- Acute:chronic load ratio
- Load-status classification
- Athlete-level training-load summaries
- Training-load visualizations

## Data Flow

```text
Training Sessions
       ↓
Daily Training Load
       ↓
7-Session Acute Load
       ↓
28-Session Chronic Reference
       ↓
Acute:Chronic Ratio
       ↓
Load Classification
       ↓
Visualization
       ↓
Exported Analysis
```

## Dataset

The included dataset contains training-load observations for multiple athletes.

Each observation contains:

| Variable | Description |
|---|---|
| Athlete | Athlete identifier |
| Date | Training date |
| Training_Load | Session training load in arbitrary units |

## Acute Load

Acute load is calculated as a seven-session rolling sum.

```text
Acute Load =
Sum of the previous seven sessions
```

A minimum of seven observations is required.

## Chronic Load

The project uses a twenty-eight-session rolling average as a longer-term reference.

```text
Chronic Load =
Average of the previous twenty-eight sessions
```

A minimum of twenty-eight observations is required.

## Acute:Chronic Ratio

The ratio is calculated as:

```text
Acute Load
------------
Chronic Load × 7
```

The calculation compares the recent seven-session workload with a longer-term seven-session-equivalent reference.

## Load Classification

For this educational project:

```text
Ratio < 0.80
→ Lower Load

0.80–1.30
→ Reference Range

Ratio > 1.30
→ Higher Load
```

These thresholds are programming rules for this portfolio project and should not be interpreted as universal injury-risk thresholds.

## Important Data Requirement

A chronic reference requires sufficient historical data.

With a twenty-eight-session chronic window:

```text
28 observations per athlete
```

are required before a chronic value can be calculated.

The program therefore returns:

```text
Insufficient Baseline
```

when enough historical data are unavailable.

This prevents the system from creating artificial or unreliable baselines.

## Technologies

- Python
- Pandas
- Matplotlib
- CSV
- Datetime handling
- GroupBy
- Rolling windows
- Feature engineering
- Conditional logic
- Data visualization

## Installation

Install the required libraries:

```bash
pip install pandas matplotlib
```

## Running the Project

Place the Python file and CSV file in the same folder.

Run:

```bash
python athlete_acute_chronic_load.py
```

## Generated Files

The program generates:

```text
training_load_analysis.csv
acute_chronic_load_trend.png
load_ratio_trend.png
```

## Sports Performance Applications

The workflow can be used as an educational foundation for:

- Strength and conditioning
- Athlete monitoring
- Training-load management
- Periodization
- Sports analytics
- Performance analysis
- Longitudinal monitoring

## Limitations

This project uses synthetic data.

Training load is not a direct measurement of physiological fatigue.

The acute:chronic workload ratio has also been debated in sports-science research, and ratio thresholds should not automatically be interpreted as injury-prediction rules.

Real athlete-monitoring systems should consider:

- Individual athlete history
- Training monotony
- Training strain
- Wellness
- Recovery
- GPS metrics
- Heart-rate data
- Neuromuscular testing
- Competition schedule
- Performance outcomes

## Future Development

- Expand the dataset to 28+ sessions per athlete
- Add session RPE
- Add training duration
- Add GPS metrics
- Add wellness
- Add readiness
- Add HRV
- Add sleep
- Add sprint testing
- Add jump testing
- Add strength testing
- Add exponentially weighted moving averages
- Add athlete-specific baselines
- Build an interactive dashboard
- Add machine-learning models

## Skills Demonstrated

```text
Python
   ↓
Pandas
   ↓
Time-Series Data
   ↓
Rolling Windows
   ↓
Feature Engineering
   ↓
Conditional Logic
   ↓
Visualization
   ↓
Sports Analytics
```

## Author

**Abhishek Tomar**

Strength & Conditioning | Sports Performance | Sports Analytics | Python

## License

MIT License