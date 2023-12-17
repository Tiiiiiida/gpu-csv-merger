# CSV合并工具

这个仓库包含一个多功能的CSV合并工具，具有GPU（CUDA）和CPU版本，可有效合并多个CSV文件。该工具利用RAPIDS cuDF和Dask库进行GPU加速。

## 特点

* **GPU（CUDA）和CPU版本：** 根据你的硬件配置选择适当的版本。
* **高效合并：** 将多个CSV文件合并为单个合并的CSV文件。
* **灵活命名：** 自定义合并的CSV文件的命名约定。
* **支持大文件：** 轻松处理大型CSV文件。

**GPU版本的其他功能：**

* **CUDA加速：** 利用CUDA的强大功能，与CPU计算相比，CUDA加速速度显着更快。

## 用法

### GPU版本（需要Linux，NVIDIA GPU支持CUDA）：

```bash
python merge_gpu.py --folder_path /path/to/csv/files
```

### CPU版本：

```bash
python merge_cpu.py --folder_path /path/to/csv/files
```

**注意：** 指定的文件夹是相对于当前目录而不是绝对路径。如果你需要修改目录的指定方式，请简单地调整以下行：

```python
# Specify a specific folder as the directory and call the function
specified_folder = 'Example0'
folder_path = os.path.join(os.getcwd(), specified_folder)
merge_csv_files(folder_path)
```

## 要求

* **GPU版本：**
  * Python 3.x
  * RAPIDS cuDF
  * Dask（用于Dask cuDF支持）
  * Linux环境
  * 支持CUDA的NVIDIA GPU
* **CPU版本：**
  * Python 3.x

**注意：**

* GPU版本需要支持CUDA的NVIDIA GPU的Linux环境。
* RAPIDS与Windows不兼容。
* CUDA不支持macOS.
* 有关安装RAPIDS的详细说明，请参见RAPIDS文档。

## 举例

为了演示，提供了一个名为 `Example0`的文件夹，其中包含三个CSV文件：`file0.csv`，`file1.csv`和 `file2.csv`。 您可以通过指定文件夹路径在此示例上运行该工具。

```bash
python merge_gpu.py --folder_path Example0
```
