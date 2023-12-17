# CSV Merge Tool

This repository contains a versatile CSV merging tool with both GPU (CUDA) and CPU versions for efficient consolidation of multiple CSV files. The tool leverages RAPIDS cuDF and Dask libraries for GPU and CPU acceleration, respectively.

## Languages

- [中文](README_CN.md)
- [Deutsch](README_GE.md)

## Features

- **GPU (CUDA) and CPU Versions:** Choose the appropriate version based on your hardware configuration.
- **Efficient Merging:** Consolidate multiple CSV files into a single merged CSV file.
- **Flexible Naming:** Customize the naming convention for the merged CSV file.
- **Support for Large Files:** Handles large CSV files with ease.

**Additional Features for GPU Version:**

- **CUDA Acceleration:** Utilizes the power of CUDA for significantly faster CSV merging operations compared to CPU computation.

## Usage

### GPU Version (Linux, NVIDIA GPU with CUDA support required):

```bash
python merge_gpu.py --folder_path /path/to/csv/files
```

### CPU Version:

```bash
python merge_cpu.py --folder_path /path/to/csv/files
```

**Note:** The folder specified is relative to the current directory, not an absolute path. If you need to modify the way the directory is specified, simply adjust the following lines:

```python
# Specify a specific folder as the directory and call the function
specified_folder = 'Example0'
folder_path = os.path.join(os.getcwd(), specified_folder)
merge_csv_files(folder_path)
```

## Requirements

- **GPU Version:**

  - Python 3.x
  - RAPIDS cuDF
  - Dask (for Dask cuDF support)
  - Linux environment
  - NVIDIA GPU with CUDA support
- **CPU Version:**

  - Python 3.x

**Note:**

- The GPU version requires a Linux environment with an NVIDIA GPU that supports CUDA.
- RAPIDS is not compatible with Windows.
- CUDA does not support macOS.
- For detailed instructions on installing RAPIDS, please refer to the [RAPIDS documentation](https://docs.rapids.ai/install).

## Example

For demonstration purposes, a folder named `Example0` has been provided, containing three CSV files: `file0.csv`, `file1.csv`, and `file2.csv`. You can run the tool on this example by specifying the folder path.

```bash
python merge_gpu.py --folder_path Example0
```
