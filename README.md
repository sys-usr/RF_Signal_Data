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
   python src/RF_Data_Processing.py
   ```

4. The script will execute the following operations in order:

   - Data description: Prints the summary statistics, information, first 10 rows, and shape of the data.
   - Column mapping: Creates maps for specific columns like Modulation, Device Type, Antenna Type, Weather Condition, Interference Type, and Device Status.
   - Apply mapping: Replaces the column values with their respective mapped values using the created maps.
   - Drop columns: Removes unnecessary columns from the data.
   - Frequency parsing: Parses the unique frequencies and saves the corresponding data frames to separate CSV files in the `RF_Signal_Data/Data/Frequency_data` directory.
   - Modulation parsing: Parses the unique modulations and saves the corresponding data frames to separate CSV files in the `RF_Signal_Data/Data/Modulation_data` directory.
   - Correlation analysis and graphs: Analyzes correlation and plots graphs for each file in the Frequency_data and Modulation_data directories.

5. The processed data and analysis results will be displayed in the console output.

## Customization

- To modify the data file or its location, update the `data_file` variable in the `__main__` block of the `src/RF_Data_Processing.py` script.

- Additional functionality or modifications can be implemented by extending the `RFDataProcessing` class.

    - Future planned code would be to make customization possible with argparse.

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
