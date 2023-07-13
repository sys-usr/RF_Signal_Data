## Data Source
 - https://www.kaggle.com/datasets/suraj520/rf-signal-data

# RF Data Processing

This Python script is designed to process RF data by performing various operations on a given data file. The script utilizes the `RFDataProcessing` class, which provides methods for data description, column mapping, data transformation, and analysis.

## Requirements

- Python 3.x
- pandas library
- matplotlib library

## Usage

1. Install the required dependencies by running the following command:

   ```shell
   pip install pandas matplotlib
   ```

2. Place the RF data file (`logged_data.csv`) in the `RF_Signal_Data/Data` directory.

3. Run the script using the following command:

   ```shell
   python src/RF_Data_Processing.py [-h] [-d] [-m] [-a] [-dc] [-f] [-c] [-p] [-all] data_file
   ```

4. The script accepts the following optional arguments:

   - `-h`, `--help`: Show help information for the available arguments.
   - `-d`, `--data-description`: Print data description.
   - `-m`, `--create-maps`: Create column maps.
   - `-a`, `--apply-maps`: Apply column maps.
   - `-dc`, `--drop-columns`: Drop columns.
   - `-f`, `--frequency-parser`: Parse frequencies and save to CSV files.
   - `-c`, `--correlation-analysis`: Perform correlation analysis.
   - `-p`, `--plot-graphs`: Plot graphs.
   - `-all`, `--all-functions`: Run all functions.

5. The script will execute the selected operations in the specified order.

6. The processed data and analysis results will be displayed in the console output.

## Graphs



## License

This project is free to use.

## File Structure

```
RF_Data
└─ RF_Signal_Data
   ├─ Data
   │  ├─ Frequency_data
   │  │  ├─ 100MHz.csv
   │  │  ├─ 120MHz.csv
   │  │  ├─ 140MHz.csv
   │  │  ├─ 160MHz.csv
   │  │  ├─ 70MHz.csv
   │  │  └─ 90MHz.csv
   │  ├─ logged_data.csv
   │  └─ Modulation_data
   │     ├─ 1.csv
   │     ├─ 2.csv
   │     ├─ 3.csv
   │     ├─ 4.csv
   │     ├─ 5.csv
   │     └─ 6.csv
   ├─ notebooks
   │  └─ rf_signal_data.ipynb
   ├─ README.md
   └─ src
      └─ RF_Data_Processing.py
```