#!/usr/bin/env python3
"""
CSV File Processor Script
A comprehensive Python script for processing CSV files with various operations.
"""

import csv
import pandas as pd
import sys
import os
from pathlib import Path
import argparse
from typing import List, Dict, Any, Optional


class CSVProcessor:
    """A class to handle various CSV file operations."""
    
    def __init__(self, file_path: str):
        """
        Initialize the CSV processor with a file path.
        
        Args:
            file_path (str): Path to the CSV file
        """
        self.file_path = file_path
        self.data = None
        
    def read_csv(self, encoding: str = 'utf-8') -> pd.DataFrame:
        """
        Read CSV file into a pandas DataFrame.
        
        Args:
            encoding (str): File encoding (default: utf-8)
            
        Returns:
            pd.DataFrame: The loaded data
        """
        try:
            self.data = pd.read_csv(self.file_path, encoding=encoding)
            print(f"Successfully loaded {len(self.data)} rows from {self.file_path}")
            return self.data
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
            return None
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None
    
    def display_info(self) -> None:
        """Display basic information about the CSV data."""
        if self.data is None:
            print("No data loaded. Please read a CSV file first.")
            return
            
        print("\n" + "="*50)
        print("CSV FILE INFORMATION")
        print("="*50)
        print(f"File: {self.file_path}")
        print(f"Shape: {self.data.shape}")
        print(f"Columns: {list(self.data.columns)}")
        print(f"Data types:\n{self.data.dtypes}")
        
        print("\nFirst 5 rows:")
        print(self.data.head())
        
        print("\nBasic statistics:")
        print(self.data.describe())
        
        print("\nMissing values:")
        missing = self.data.isnull().sum()
        if missing.sum() > 0:
            print(missing[missing > 0])
        else:
            print("No missing values found.")
    
    def filter_data(self, column: str, value: Any, operator: str = '==') -> pd.DataFrame:
        """
        Filter data based on column value.
        
        Args:
            column (str): Column name to filter on
            value (Any): Value to filter by
            operator (str): Comparison operator ('==', '!=', '>', '<', '>=', '<=', 'contains')
            
        Returns:
            pd.DataFrame: Filtered data
        """
        if self.data is None:
            print("No data loaded.")
            return None
            
        if column not in self.data.columns:
            print(f"Column '{column}' not found in data.")
            return None
        
        try:
            if operator == '==':
                filtered_data = self.data[self.data[column] == value]
            elif operator == '!=':
                filtered_data = self.data[self.data[column] != value]
            elif operator == '>':
                filtered_data = self.data[self.data[column] > value]
            elif operator == '<':
                filtered_data = self.data[self.data[column] < value]
            elif operator == '>=':
                filtered_data = self.data[self.data[column] >= value]
            elif operator == '<=':
                filtered_data = self.data[self.data[column] <= value]
            elif operator == 'contains':
                filtered_data = self.data[self.data[column].str.contains(str(value), na=False)]
            else:
                print(f"Unsupported operator: {operator}")
                return None
                
            print(f"Filtered data: {len(filtered_data)} rows found")
            return filtered_data
            
        except Exception as e:
            print(f"Error filtering data: {e}")
            return None
    
    def sort_data(self, column: str, ascending: bool = True) -> pd.DataFrame:
        """
        Sort data by specified column.
        
        Args:
            column (str): Column name to sort by
            ascending (bool): Sort in ascending order (default: True)
            
        Returns:
            pd.DataFrame: Sorted data
        """
        if self.data is None:
            print("No data loaded.")
            return None
            
        if column not in self.data.columns:
            print(f"Column '{column}' not found in data.")
            return None
        
        try:
            sorted_data = self.data.sort_values(by=column, ascending=ascending)
            print(f"Data sorted by '{column}' ({'ascending' if ascending else 'descending'})")
            return sorted_data
        except Exception as e:
            print(f"Error sorting data: {e}")
            return None
    
    def group_and_aggregate(self, group_column: str, agg_column: str, operation: str = 'mean') -> pd.DataFrame:
        """
        Group data and perform aggregation.
        
        Args:
            group_column (str): Column to group by
            agg_column (str): Column to aggregate
            operation (str): Aggregation operation ('mean', 'sum', 'count', 'min', 'max')
            
        Returns:
            pd.DataFrame: Aggregated data
        """
        if self.data is None:
            print("No data loaded.")
            return None
            
        if group_column not in self.data.columns or agg_column not in self.data.columns:
            print("One or both columns not found in data.")
            return None
        
        try:
            if operation == 'mean':
                result = self.data.groupby(group_column)[agg_column].mean()
            elif operation == 'sum':
                result = self.data.groupby(group_column)[agg_column].sum()
            elif operation == 'count':
                result = self.data.groupby(group_column)[agg_column].count()
            elif operation == 'min':
                result = self.data.groupby(group_column)[agg_column].min()
            elif operation == 'max':
                result = self.data.groupby(group_column)[agg_column].max()
            else:
                print(f"Unsupported operation: {operation}")
                return None
                
            print(f"Grouped by '{group_column}' with {operation} of '{agg_column}':")
            return result.reset_index()
            
        except Exception as e:
            print(f"Error in grouping and aggregation: {e}")
            return None
    
    def save_csv(self, data: pd.DataFrame, output_path: str, index: bool = False) -> bool:
        """
        Save DataFrame to CSV file.
        
        Args:
            data (pd.DataFrame): Data to save
            output_path (str): Output file path
            index (bool): Whether to save index (default: False)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            data.to_csv(output_path, index=index)
            print(f"Data saved to {output_path}")
            return True
        except Exception as e:
            print(f"Error saving CSV file: {e}")
            return False
    
    def add_column(self, column_name: str, values: List[Any] = None, default_value: Any = None) -> bool:
        """
        Add a new column to the data.
        
        Args:
            column_name (str): Name of the new column
            values (List[Any]): List of values for the new column
            default_value (Any): Default value if values not provided
            
        Returns:
            bool: True if successful, False otherwise
        """
        if self.data is None:
            print("No data loaded.")
            return False
        
        try:
            if values is not None:
                if len(values) != len(self.data):
                    print("Length of values doesn't match number of rows.")
                    return False
                self.data[column_name] = values
            else:
                self.data[column_name] = default_value
                
            print(f"Column '{column_name}' added successfully.")
            return True
            
        except Exception as e:
            print(f"Error adding column: {e}")
            return False
    
    def remove_duplicates(self, subset: List[str] = None) -> pd.DataFrame:
        """
        Remove duplicate rows.
        
        Args:
            subset (List[str]): Columns to consider for duplicates
            
        Returns:
            pd.DataFrame: Data without duplicates
        """
        if self.data is None:
            print("No data loaded.")
            return None
        
        try:
            original_count = len(self.data)
            self.data = self.data.drop_duplicates(subset=subset)
            new_count = len(self.data)
            print(f"Removed {original_count - new_count} duplicate rows.")
            return self.data
            
        except Exception as e:
            print(f"Error removing duplicates: {e}")
            return None


def create_sample_csv(filename: str = "sample_data.csv") -> None:
    """Create a sample CSV file for testing."""
    sample_data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 28, 22, 45, 31],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Berlin', 'Toronto'],
        'Salary': [50000, 60000, 70000, 55000, 48000, 80000, 65000],
        'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing', 'Finance', 'HR']
    }
    
    df = pd.DataFrame(sample_data)
    df.to_csv(filename, index=False)
    print(f"Sample CSV file '{filename}' created with {len(df)} rows.")


def main():
    """Main function to demonstrate CSV processing capabilities."""
    parser = argparse.ArgumentParser(description='CSV File Processor')
    parser.add_argument('--file', '-f', type=str, help='Path to CSV file')
    parser.add_argument('--create-sample', action='store_true', help='Create a sample CSV file')
    parser.add_argument('--demo', action='store_true', help='Run demo with sample data')
    
    args = parser.parse_args()
    
    if args.create_sample:
        create_sample_csv()
        return
    
    if args.demo:
        # Create sample data for demo
        create_sample_csv()
        file_path = "sample_data.csv"
    elif args.file:
        file_path = args.file
    else:
        print("Please provide a CSV file path using --file or use --demo for demonstration.")
        return
    
    # Initialize processor
    processor = CSVProcessor(file_path)
    
    # Read the CSV file
    data = processor.read_csv()
    if data is None:
        return
    
    # Display basic information
    processor.display_info()
    
    if args.demo:
        print("\n" + "="*50)
        print("DEMONSTRATION OF CSV OPERATIONS")
        print("="*50)
        
        # Filter data
        print("\n1. Filtering data (Age > 30):")
        filtered = processor.filter_data('Age', 30, '>')
        if filtered is not None:
            print(filtered[['Name', 'Age', 'City']])
        
        # Sort data
        print("\n2. Sorting data by Salary (descending):")
        sorted_data = processor.sort_data('Salary', ascending=False)
        if sorted_data is not None:
            print(sorted_data[['Name', 'Salary']].head())
        
        # Group and aggregate
        print("\n3. Average salary by department:")
        grouped = processor.group_and_aggregate('Department', 'Salary', 'mean')
        if grouped is not None:
            print(grouped)
        
        # Add a new column
        print("\n4. Adding a new column 'Salary_Category':")
        categories = ['Low' if x < 55000 else 'High' for x in processor.data['Salary']]
        processor.add_column('Salary_Category', categories)
        print(processor.data[['Name', 'Salary', 'Salary_Category']].head())
        
        # Save processed data
        output_file = "processed_data.csv"
        processor.save_csv(processor.data, output_file)
        print(f"\nProcessed data saved to {output_file}")


if __name__ == "__main__":
    main()