# CSV File Processor

A comprehensive Python script for processing CSV files with various data manipulation operations.

## Features

- **Read CSV files** with encoding support
- **Display data information** (shape, columns, data types, statistics)
- **Filter data** using various operators (==, !=, >, <, >=, <=, contains)
- **Sort data** by any column (ascending/descending)
- **Group and aggregate** data (mean, sum, count, min, max)
- **Add new columns** with custom values
- **Remove duplicates** from data
- **Save processed data** to new CSV files
- **Command-line interface** for easy usage

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy
```

## Usage

### Command Line Interface

1. **Process your own CSV file:**
```bash
python csv_processor.py --file your_data.csv
```

2. **Run demonstration with sample data:**
```bash
python csv_processor.py --demo
```

3. **Create a sample CSV file:**
```bash
python csv_processor.py --create-sample
```

### Python Script Usage

```python
from csv_processor import CSVProcessor

# Initialize processor
processor = CSVProcessor("your_file.csv")

# Read CSV file
data = processor.read_csv()

# Display information
processor.display_info()

# Filter data
filtered = processor.filter_data('Age', 30, '>')

# Sort data
sorted_data = processor.sort_data('Salary', ascending=False)

# Group and aggregate
grouped = processor.group_and_aggregate('Department', 'Salary', 'mean')

# Add new column
processor.add_column('New_Column', ['value1', 'value2', ...])

# Save processed data
processor.save_csv(processor.data, "output.csv")
```

### Simple Example

Run the example script to see basic operations:

```bash
python example_usage.py
```

## Available Operations

### Filtering
- `==` (equal)
- `!=` (not equal)
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal)
- `<=` (less than or equal)
- `contains` (string contains)

### Aggregation Operations
- `mean` - Calculate average
- `sum` - Calculate sum
- `count` - Count occurrences
- `min` - Find minimum value
- `max` - Find maximum value

## File Structure

```
.
├── csv_processor.py      # Main CSV processing class
├── example_usage.py      # Simple usage examples
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Example Data

The script can create sample data for testing:

| Name    | Age | City      | Salary | Department |
|---------|-----|-----------|--------|------------|
| Alice   | 25  | New York  | 50000  | IT         |
| Bob     | 30  | London    | 60000  | HR         |
| Charlie | 35  | Paris     | 70000  | Finance    |
| ...     | ... | ...       | ...    | ...        |

## Error Handling

The script includes comprehensive error handling for:
- File not found errors
- Invalid column names
- Data type mismatches
- Encoding issues
- Missing values

## License

This project is open source and available under the MIT License.