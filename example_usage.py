#!/usr/bin/env python3
"""
Example usage of the CSV Processor
This script demonstrates basic CSV operations.
"""

from csv_processor import CSVProcessor, create_sample_csv

def simple_csv_operations():
    """Demonstrate simple CSV operations."""
    
    # Create a sample CSV file for demonstration
    print("Creating sample CSV file...")
    create_sample_csv("example_data.csv")
    
    # Initialize the CSV processor
    processor = CSVProcessor("example_data.csv")
    
    # Read the CSV file
    print("\nReading CSV file...")
    data = processor.read_csv()
    
    if data is not None:
        # Display basic information about the data
        processor.display_info()
        
        # Example 1: Filter data
        print("\n--- Example 1: Filtering ---")
        filtered_data = processor.filter_data('Age', 30, '>')
        print("People older than 30:")
        print(filtered_data[['Name', 'Age']])
        
        # Example 2: Sort data
        print("\n--- Example 2: Sorting ---")
        sorted_data = processor.sort_data('Salary', ascending=False)
        print("Top 3 highest earners:")
        print(sorted_data[['Name', 'Salary']].head(3))
        
        # Example 3: Group and aggregate
        print("\n--- Example 3: Grouping ---")
        dept_avg = processor.group_and_aggregate('Department', 'Salary', 'mean')
        print("Average salary by department:")
        print(dept_avg)
        
        # Example 4: Add new column
        print("\n--- Example 4: Adding Column ---")
        # Create age categories
        age_categories = []
        for age in processor.data['Age']:
            if age < 25:
                age_categories.append('Young')
            elif age < 35:
                age_categories.append('Middle')
            else:
                age_categories.append('Senior')
        
        processor.add_column('Age_Category', age_categories)
        print("Data with new Age_Category column:")
        print(processor.data[['Name', 'Age', 'Age_Category']])
        
        # Example 5: Save processed data
        print("\n--- Example 5: Saving Data ---")
        processor.save_csv(processor.data, "processed_example.csv")
        
        print("\nAll operations completed successfully!")


if __name__ == "__main__":
    simple_csv_operations()