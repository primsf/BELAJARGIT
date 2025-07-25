import pandas as pd
import glob as gb
import os
import warnings
from pandas.errors import DtypeWarning
from tqdm import tqdm

# Filter Warning code
warnings.filterwarnings("ignore", category=DtypeWarning)
warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

# tqdm works in pandas function
tqdm.pandas()

# set the path to the folder containing the files
Input_path = input('Input Address Path: ')
print(f"Checking path: {Input_path}")

# Script to check if the path has CSV files or not
def check_csv_files(path):
    """
    Check if the given path contains CSV files and provide detailed information
    
    Args:
        path (str): The directory path to check
    
    Returns:
        dict: Information about CSV files found
    """
    
    # Check if the path exists
    if not os.path.exists(path):
        print(f"❌ Error: Path '{path}' does not exist!")
        return None
    
    # Check if it's a directory
    if not os.path.isdir(path):
        print(f"❌ Error: '{path}' is not a directory!")
        return None
    
    # Search for CSV files using glob
    csv_pattern = os.path.join(path, "*.csv")
    csv_files = gb.glob(csv_pattern)
    
    # Also check for CSV files in subdirectories
    csv_pattern_recursive = os.path.join(path, "**/*.csv")
    csv_files_recursive = gb.glob(csv_pattern_recursive, recursive=True)
    
    result = {
        'path': path,
        'csv_files_current_dir': csv_files,
        'csv_files_all_dirs': csv_files_recursive,
        'total_csv_files': len(csv_files_recursive)
    }
    
    return result

# Check for CSV files in the specified path
print("\n" + "="*50)
print("CSV FILE CHECKER")
print("="*50)

csv_info = check_csv_files(Input_path)

if csv_info:
    total_files = csv_info['total_csv_files']
    
    if total_files == 0:
        print(f"❌ No CSV files found in '{Input_path}' or its subdirectories.")
    else:
        print(f"✅ Found {total_files} CSV file(s) in total!")
        
        # Files in current directory
        current_dir_files = csv_info['csv_files_current_dir']
        if current_dir_files:
            print(f"\n📁 CSV files in current directory ({len(current_dir_files)}):")
            for i, file in enumerate(current_dir_files, 1):
                file_name = os.path.basename(file)
                file_size = os.path.getsize(file) / (1024 * 1024)  # Size in MB
                print(f"  {i}. {file_name} ({file_size:.2f} MB)")
        
        # All files (including subdirectories)
        all_files = csv_info['csv_files_all_dirs']
        if len(all_files) > len(current_dir_files):
            print(f"\n📂 All CSV files (including subdirectories):")
            for i, file in enumerate(all_files, 1):
                relative_path = os.path.relpath(file, Input_path)
                file_size = os.path.getsize(file) / (1024 * 1024)  # Size in MB
                print(f"  {i}. {relative_path} ({file_size:.2f} MB)")
        
        # Optional: Quick preview of the first CSV file
        if all_files:
            print(f"\n🔍 Quick preview of '{os.path.basename(all_files[0])}':")
            try:
                sample_df = pd.read_csv(all_files[0], nrows=5)
                print(f"   Shape: {sample_df.shape}")
                print(f"   Columns: {list(sample_df.columns)}")
                print("\n   First 3 rows:")
                print(sample_df.head(3).to_string(index=False))
            except Exception as e:
                print(f"   ❌ Could not read file: {str(e)}")

print("\n" + "="*50)