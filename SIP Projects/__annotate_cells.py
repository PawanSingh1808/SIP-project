from pathlib import Path

path = Path(r"d:\Pawan\Project\SIP Projects\CBSOT_project1.ipynb")
text = path.read_text(encoding='utf-8')
lines = text.splitlines()
out_lines = []
inside_cell = False
pending_comment = False

comment_map = [
    ('import pandas as pd', '# Import libraries for data analysis and visualization'),
    ('pd.read_excel', '# Load the Telco customer churn dataset from Excel into a DataFrame'),
    ('df.shape', '# Display the number of rows and columns in the dataset'),
    ('df.info()', '# Show dataset schema, data types, and non-null counts'),
    ("df['Churn Label'].value_counts()", '# Count how many customers have churned versus retained'),
    ('sns.histplot(df[\'Tenure Months\']', '# Plot the distribution of tenure months'),
    ("df['Tenure Months'].max()", '# Get the longest customer tenure'),
    ("df['Tenure Months'].min()", '# Get the shortest customer tenure'),
    ('sns.boxplot(y=\'Tenure Months\'', '# Create a boxplot of tenure by churn label'),
    ("df['Churn Label'].unique()", '# List the unique churn label categories'),
    ('sns.histplot(df[\'Monthly Charges\']', '# Plot the distribution of monthly charges'),
    ('sns.boxplot(y=\'Monthly Charges\'', '# Compare monthly charges by churn label'),
    ("df[df['Churn Label']=='Yes']['Monthly Charges'].quantile", '# Calculate monthly charge quantiles for churned customers'),
    ("df[df['Churn Label']=='No']['Monthly Charges'].quantile", '# Calculate monthly charge quantiles for retained customers'),
    ("df['Monthly Charges'].describe()", '# Summarize monthly charge statistics'),
    ('sns.countplot(x=\'Churn Label\'', '# Show customer counts by churn label'),
    ("df['Contract'].unique()", '# List unique contract types in the dataset'),
    ("df['Contract'].value_counts()", '# Count customers per contract type'),
    ('sns.countplot( x = \'Contract\'', '# Plot contract type counts split by churn label'),
    ("df['Internet Service'].unique()", '# List unique internet service plans'),
    ('sns.countplot( x = \'Internet Service\'', '# Plot internet service usage by churn label'),
    ("df['Payment Method'].unique()", '# List available payment methods'),
    ("df['Payment Method'].value_counts()", '# Count customers by payment method'),
    ('sns.countplot( x = \'Payment Method\'', '# Plot payment methods split by churn label'),
    ("df['Tech Support'].unique()", '# List unique tech support options'),
    ("df['Tech Support'].value_counts()", '# Count customers by tech support option'),
    ('sns.countplot( x = \'Tech Support\'', '# Plot tech support usage by churn label'),
    ('avg_tenure=df.groupby', '# Calculate average tenure by churn label'),
    ('avg_tenure', '# Display the average tenure result'),
    ('numerical_cols=[', '# Select numerical columns for correlation analysis'),
    ('.corr()', '# Compute the correlation matrix for the selected numerical columns'),
    ('correlation_matrix', '# Display the computed correlation matrix'),
    ('from matplotlib.colors import Normalize', '# Import Normalize for plot scaling or color normalization'),
    ("pd.to_numeric(df['Total Charges']", '# Convert Total Charges to numeric values, coercing invalid entries'),
    ("df['Total Charges']", '# Display the Total Charges column values'),
]

for line in lines:
    stripped = line.strip()
    if stripped.startswith('<VSCode.Cell') and 'language="python"' in stripped:
        inside_cell = True
        pending_comment = True
        out_lines.append(line)
        continue
    if inside_cell and stripped == '</VSCode.Cell>':
        out_lines.append(line)
        inside_cell = False
        pending_comment = False
        continue
    if inside_cell and pending_comment:
        if stripped and not stripped.startswith('#'):
            comment = '# Describe the purpose of this cell'
            for key, value in comment_map:
                if key in line:
                    comment = value
                    break
            out_lines.append(comment)
            out_lines.append(line)
            pending_comment = False
            continue
        elif stripped == '':
            out_lines.append('# Empty cell placeholder')
            out_lines.append(line)
            pending_comment = False
            continue
    out_lines.append(line)

path.write_text('\n'.join(out_lines) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')
print('Updated notebook with comments.')
