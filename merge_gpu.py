import os
import dask_cudf
from tqdm import tqdm

def merge_csv_files(folder_path, output_file_name='merged.csv'):
    # Get all CSV files in the folder and sort them by file name
    csv_files = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')])

    # Get the first 4 characters of the first CSV file as the new file name
    new_file_name = os.path.basename(csv_files[0])[:4]

    # Build the complete path for the new file
    output_file_path = os.path.join(folder_path, f'{new_file_name}_{output_file_name}')

    # Define the function to read, process, and write data
    def process_csv(file_path):
        # Read CSV file
        df = dask_cudf.read_csv(file_path, dtype='str')

        # Write processed data to a new CSV file
        df.to_csv(output_file_path, index=False, mode='a', single_file=True, header=not os.path.exists(output_file_path))

    # Process data one by one
    for csv_file in tqdm(csv_files, desc='Merging'):
        process_csv(csv_file)

    print(f'Merged data has been saved to {output_file_path}')

# Specify a specific folder as the directory and call the function
specified_folder = 'Example0'
folder_path = os.path.join(os.getcwd(), specified_folder)
merge_csv_files(folder_path)
