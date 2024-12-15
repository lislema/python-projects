# Data Cleansing tips 

a collection of Python one-liners for data cleaning tasks, covering missing values, duplicates, type conversion, outlier removal, and more. These are tailored for quick fixes and can be used with tools like Pandas, NumPy, and standard Python libraries.

## Handle Missing Values 

### Remove Rows with Missing Values

```python
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df.dropna())"
```

### Fill Missing Values with a Default

```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df.fillna(0))"
```

### Fill Missing Values with Mean/Median
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['column'] = df['column'].fillna(df['column'].mean()); print(df)"
```

### Drop Columns with All Missing Values 

```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df.dropna(axis=1, how='all'))"
```

## Handle Duplicates

### Remove Duplicate Rows 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df.drop_duplicates())"
```

### Keep Only the First Duplicate
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df.drop_duplicates(keep='first'))"
```
### Find Duplicate Rows
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df[df.duplicated()])"
```

## Handle Inconsistent Data

### Trim Whitespace in All Columns
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x); print(df)"
```
### Convert All Text to Lowercase
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['column'] = df['column'].str.lower(); print(df)"
```
### Standardize Date Format
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['date'] = pd.to_datetime(df['date'], errors='coerce'); print(df)"
```
### Replace Specific Values
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['column'] = df['column'].replace({'old_value': 'new_value'}); print(df)"
```
## Handle Outliers

### Remove Outliers Based on Z-Score
```
python3 -c "import pandas as pd; from scipy.stats import zscore; df = pd.read_csv('data.csv'); df = df[(zscore(df['column']) < 3)]; print(df)"
```
### Remove Outliers Based on IQR
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); Q1, Q3 = df['column'].quantile(0.25), df['column'].quantile(0.75); IQR = Q3 - Q1; df = df[(df['column'] >= Q1 - 1.5*IQR) & (df['column'] <= Q3 + 1.5*IQR)]; print(df)"
```
## Handle Data Types

### Convert Column to Integer
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['column'] = pd.to_numeric(df['column'], errors='coerce').astype('Int64'); print(df)"
```
### Convert Text to Categorical 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['column'] = df['column'].astype('category'); print(df)"
```
### Split a Column into Multiple Columns 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df'col1', 'col2' = df['column'].str.split(',', expand=True); print(df)"
```
## Normalize or Scale Data

###Normalize Column Values (Min-Max Scaling) 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['column'] = (df['column'] - df['column'].min()) / (df['column'].max() - df['column'].min()); print(df)"
```
### Standardize Column Values (Mean = 0, Std Dev = 1) 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['column'] = (df['column'] - df['column'].mean()) / df['column'].std(); print(df)"
```
## Data Reshaping

### Melt Data from Wide to Long Format 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(pd.melt(df, id_vars=['id'], var_name='metric', value_name='value'))"
```
### Pivot Data from Long to Wide Format 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df.pivot(index='id', columns='metric', values='value'))"
```
## String Cleaning

### Remove Special Characters 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['column'] = df['column'].str.replace(r'[^a-zA-Z0-9]', '', regex=True); print(df)"
```
### Extract Digits from a Column 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['column'] = df['column'].str.extract(r'(\d+)'); print(df)"
```
### Split Full Names into First and Last Name 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df'first_name', 'last_name' = df['full_name'].str.split(' ', 1, expand=True); print(df)"
```
## Detect or Remove Invalid Data

### Detect Non-Numeric Rows in a Column 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df[~df['column'].apply(lambda x: str(x).isnumeric())])"
```
### Drop Rows with Invalid Dates 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); df['date'] = pd.to_datetime(df['date'], errors='coerce'); print(df.dropna(subset=['date']))"
```
## Aggregate and Group Data

### Aggregate by Group 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df.groupby('group').agg({'column': 'mean'}))"
```
### Count Values in a Column 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df['column'].value_counts())"
```
### Calculate Percentages for Each Value 
```
python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df['column'].value_counts(normalize=True) * 100)"
```
These one-liners cover a wide range of  **data cleaning tasks**  and can handle most common cleaning scenarios.









