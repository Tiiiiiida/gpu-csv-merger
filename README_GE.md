# CSV-Zusammenführungstool

Dieses Repository enthält ein vielseitiges CSV-Zusammenführungstool mit sowohl GPU- (CUDA-) als auch CPU-Versionen für eine effiziente Konsolidierung mehrerer CSV-Dateien. Das Tool nutzt die RAPIDS cuDF- und Dask-Bibliotheken für die GPU- bzw. CPU-Beschleunigung.

## Eigenschaften

* **GPU (CUDA) und CPU-Versionen:** Wählen Sie die entsprechende Version basierend auf Ihrer Hardwarekonfiguration aus.
* **Effiziente Zusammenführung:** Konsolidieren Sie mehrere CSV-Dateien zu einer einzigen zusammengeführten CSV-Datei.
* **Flexible Benennung:** Passen Sie die Namenskonvention für die zusammengeführte CSV-Datei an.
* **Unterstützung für große Dateien:** Verarbeitet große CSV-Dateien mühelos.

**Zusätzliche Funktionen für die GPU-Version:**

* **CUDA-Beschleunigung:** Nutzt die Leistung von CUDA für deutlich schnellere CSV-Zusammenführungsoperationen im Vergleich zur CPU-Berechnung.

## Verwendung

### GPU-Version (Linux, NVIDIA-GPU mit CUDA-Unterstützung erforderlich):

```bash
python merge_gpu.py --folder_path /path/to/csv/files
```

### CPU-Version:

```bash
python merge_cpu.py --folder_path /path/to/csv/files
```

**Hinweis:** Der angegebene Ordner ist relativ zum aktuellen Verzeichnis und nicht absolut. Wenn Sie die Art und Weise ändern müssen, wie das Verzeichnis angegeben wird, passen Sie einfach die folgenden Zeilen an:

```python
# Geben Sie einen bestimmten Ordner als Verzeichnis an und rufen Sie die Funktion auf
specified_folder = 'Beispiel0'
folder_path = os.path.join(os.getcwd(), specified_folder)
merge_csv_files(folder_path)
```

## Anforderungen

* **GPU-Version:**
  * Python 3.x
  * RAPIDS cuDF
  * Dask (für Dask cuDF-Unterstützung)
  * Linux-Umgebung
  * NVIDIA-GPU mit CUDA-Unterstützung
* **CPU-Version:**
  * Python 3.x

**Hinweis:**

* Die GPU-Version erfordert eine Linux-Umgebung mit einer NVIDIA-GPU, die CUDA unterstützt.
* RAPIDS ist nicht mit Windows kompatibel.
* CUDA unterstützt macOS nicht.
* Weitere Informationen zur Installation von RAPIDS finden Sie in der RAPIDS-Dokumentation.

## Beispiel

Zu Demonstrationszwecken wurde ein Ordner namens `Beispiel0` bereitgestellt, der drei CSV-Dateien enthält: `file0.csv`, `file1.csv` und `file2.csv`. Sie können das Tool auf diesem Beispiel ausführen, indem Sie den Ordnerpfad angeben.

```bash
python merge_gpu.py --folder_path Beispiel0
```
