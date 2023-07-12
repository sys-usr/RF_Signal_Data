```markdown
# RF Data Processing

This Python script is designed to process RF data by performing various operations on a given data file. The script utilizes the `RFDataProcessing` class, which provides methods for data description, column mapping, data transformation, and analysis.

## Requirements

- Python 3.x
- pandas library

## Usage

1. Install the required dependencies by running the following command:

   ```shell
   pip install pandas
   ```

2. Place the RF data file (`logged_data.csv`) in the `data` directory.

3. Update the file path in the `__main__` block of the `rf_data_processing.py` script if needed:

   ```python
   data_file = "data/logged_data.csv"
   ```

4. Run the script using the following command:

   ```shell
   python rf_data_processing.py
   ```

5. The script will execute the following operations in order:

   - Data description: Prints the summary statistics, information, first 10 rows, and shape of the data.
   - Column mapping: Creates maps for specific columns like Modulation, Device Type, Antenna Type, Weather Condition, Interference Type, and Device Status.
   - Apply mapping: Replaces the column values with their respective mapped values using the created maps.
   - Drop columns: Removes unnecessary columns from the data.
   - Frequency parsing: Parses the unique frequencies and saves the corresponding data frames to separate CSV files.
   - Correlation analysis: Computes the correlation matrix and prints the correlated categories.

6. The processed data and analysis results will be displayed in the console output.

## Customization

- If you want to add or remove specific operations, modify the `__main__` block of the `rf_data_processing.py` script accordingly.

- To customize the data file location or name, update the `data_file` variable in the `__main__` block.

- Additional functionality or modifications can be implemented by extending the `RFDataProcessing` class.

## License

This project is free use.