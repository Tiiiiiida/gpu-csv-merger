import pandas as pd
import os
from tqdm import tqdm

def merge_csv_files(folder_path, output_file_name='merged.csv'):
    # Get all CSV files in the folder and sort them by file name
    csv_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.csv')])

    # Initialize an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    # Get the first 4 characters of the first CSV file as the new file name
    new_file_name = csv_files[0][:4]

    # Build the complete path for the new file
    output_file_path = os.path.join(folder_path, f'{new_file_name}_{output_file_name}')

    # Read and merge CSV files into the DataFrame one by one
    for csv_file in tqdm(csv_files, desc='Merging'):
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        merged_data = pd.concat([merged_data, df], ignore_index=True)
        
        # Write the merged data to a new CSV file using append mode
        merged_data.to_csv(output_file_path, index=False, mode='a', header=not os.path.exists(output_file_path))
        merged_data = pd.DataFrame()  # Clear the DataFrame for the next file

    print(f'Merged data has been saved to {output_file_path}')

# Specify a specific folder as the directory and call the function
specified_folder = 'Example0'
folder_path = os.path.join(os.getcwd(), specified_folder)
merge_csv_files(folder_path)
