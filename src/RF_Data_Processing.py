import pandas as pd
import os
import matplotlib.pyplot as plt
import argparse


class RFDataProcessing:
    """Class for processing RF data."""

    def __init__(self, data_file):
        """Initialize the class with the data file."""
        self.data_file = data_file
        self.signals = pd.read_csv(data_file)

    def data_description(self):
        """Print the summary statistics, information, first 10 rows, and shape of the data."""
        print(self.signals.describe())
        print(self.signals.info())
        print(self.signals.head(10))
        print(self.signals.shape)

    @staticmethod
    def create_maps():
        """Create maps for the following columns: Modulation, Device Type, Antenna Type, Weather Condition, Interference Type, and Device Status."""
        modulation_map = {
            "8PSK": 5,
            "AM": 1,
            "BPSK": 3,
            "FM": 2,
            "QAM": 6,
            "QPSK": 4
        }
        device_type_map = {
            "Halow-U": 1,
            "HackRF": 2,
            "SteamDeck": 3
        }
        antenna_type_map = {
            "Dipole": 1,
            "Yagi": 2,
            "Directional": 3,
            "Omnidirectional": 4
        }
        weather_condition_map = {
            "Sunny": 1,
            "Cloudy": 2,
            "Rainy": 3
        }
        interference_type_map = {
            "None": 1,
            "Intermodulation": 2,
            "Co-channel": 3,
            "Adjacent-channel": 4
        }
        device_status_map = {
            "Running game": 1,
            "Streaming I/Q data": 2,
            "Transmitting beacon signal": 3
        }
        return modulation_map, device_type_map, antenna_type_map, weather_condition_map, interference_type_map, device_status_map
    
    def apply_maps(self, data, modulation_map, device_type_map, antenna_type_map, weather_condition_map, interference_type_map, device_status_map):
        """Apply the created maps to the data."""
        data["Modulation"] = data["Modulation"].replace(modulation_map)
        data["Device Type"] = data["Device Type"].replace(device_type_map)
        data["Antenna Type"] = data["Antenna Type"].replace(antenna_type_map)
        data["Weather Condition"] = data["Weather Condition"].replace(weather_condition_map)
        data["Interference Type"] = data["Interference Type"].replace(interference_type_map)
        data["Device Status"] = data["Device Status"].replace(device_status_map)

    def drop_columns(self):
        """Drop the specified columns from the data."""
        columns_to_drop = [
            'Location', 'Battery Level', 'Humidity', 'Wind Speed', 'Power Source', 'CPU Usage', 'Memory Usage',
            'Disk Usage', 'System Load', 'Latitude', 'Longitude', 'Altitude(m)', 'Air Pressure', 'I/Q Data'
        ]
        self.signals = self.signals.drop(columns=columns_to_drop)

    def frequency_parser(self):
        unique_frequencies = self.signals["Frequency"].unique()
        output_directory = "../RF_Signal_Data/Data/Frequency_data"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for frequency in unique_frequencies:
            frequency_mhz = frequency / 1000000.0  # Convert frequency to MHz
            frequency_mhz_str = str(int(frequency_mhz)) + "MHz"
            frequency_df = self.signals[self.signals["Frequency"] == frequency]

            # Save the data frame to a CSV file
            with open(os.path.join(output_directory, f"{frequency_mhz_str}.csv"), "w", newline="") as f:
                frequency_df.to_csv(f, index=False)

    def modulation_parser(self):
        unique_modulations = self.signals["Modulation"].unique()
        output_directory = "../RF_Signal_Data/Data/Modulation_data"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for modulation in unique_modulations:
            modulation_df = self.signals[self.signals["Modulation"] == modulation]

            # Save the data frame to a CSV file with the modulation type as the file name
            file_name = f"{modulation}.csv"
            file_path = os.path.join(output_directory, file_name)
            modulation_df.to_csv(file_path, index=False)

    def analyze_correlation(self):
        """Compute the correlation matrix and print the correlated categories."""
        columns_to_analyze = [
            'Timestamp', 'Frequency', 'Signal Strength', 'Modulation', 'Bandwidth', 'Device Type',
            'Antenna Type', 'Temperature', 'Precipitation', 'Weather Condition', 'Interference Type',
            'Device Status'
        ]
        corr_matrix = self.signals[columns_to_analyze].corr(numeric_only=True)
        correlations_found = False  # Flag to check if any correlations are found

        for col1 in corr_matrix.columns:
            for col2 in corr_matrix.columns:
                if col1 != col2 and (col1 != 'Device Status' or col2 != 'Device Type'):  # Exclude correlation between 'Device Status' and 'Device Type'
                    correlation = corr_matrix.loc[col1, col2]
                    if correlation >= 0.5 or correlation <= -0.5:
                        print(f"Correlation between {col1} and {col2}: {correlation}")
                        correlations_found = True

        if not correlations_found:
            print("No correlations found in data")
    
    def plot_graph(self, filename):
        """Plot the graph with average 'Signal Strength' for each 'Modulation' type."""
        df = pd.read_csv(filename)
        avg_signal_strength = df.groupby('Modulation')['Signal Strength'].mean()

        modulations = avg_signal_strength.index
        avg_signal_strength_values = avg_signal_strength.values

        plt.barh(modulations, avg_signal_strength_values)
        plt.xlabel('Average Signal Strength')
        plt.ylabel('Modulation')
        plt.title(f"Average Signal Strength by Modulation for {filename}")

        for i, v in enumerate(avg_signal_strength_values):
            plt.text(v, i, str(round(v, 2)), color='black', ha='left', va='center')

        plt.gca().invert_yaxis()
        plt.show()

    def analyze_original_data(self):
        """Analyze correlation on the original signals DataFrame."""
        print("Correlation analysis for the original data:")
        self.signals = pd.read_csv(self.data_file)  # Restore the original signals DataFrame
        self.analyze_correlation()
    
    def analyze_frequency(self):
        """Analyze correlation and plot graphs for each file in the Frequency_data directory."""
        output_directory = "../RF_Signal_Data/Data/Frequency_data"
        for filename in os.listdir(output_directory):
            if filename.endswith(".csv"):
                file_path = os.path.join(output_directory, filename)
                print(f"Correlation analysis for file: {filename}")
                rf_data_processing.signals = pd.read_csv(file_path)  # Update the signals DataFrame
                rf_data_processing.analyze_correlation()
                rf_data_processing.plot_graph(file_path)
                print("-" * 30)

    def analyze_modulation(self):
        """Analyze correlation and plot graphs for each file in the Modulation_data directory."""
        output_directory = "../RF_Signal_Data/Data/Modulation_data"
        for filename in os.listdir(output_directory):
            if filename.endswith(".csv"):
                file_path = os.path.join(output_directory, filename)
                print(f"Correlation analysis for file: {filename}")
                self.signals = pd.read_csv(file_path)  # Update the signals DataFrame
                self.analyze_correlation()
                self.plot_graph(file_path)
                print("-" * 30)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RF Data Processing")
    parser.add_argument("data_file", type=str, help="Path to the RF data file")
    parser.add_argument("-d", "--data-description", action="store_true", help="Print data description")
    parser.add_argument("-m", "--create-maps", action="store_true", help="Create column maps")
    parser.add_argument("-a", "--apply-maps", action="store_true", help="Apply column maps")
    parser.add_argument("-dc", "--drop-columns", action="store_true", help="Drop columns")
    parser.add_argument("-f", "--frequency-parser", action="store_true", help="Parse frequencies and save to CSV files")
    parser.add_argument("-c", "--correlation-analysis", action="store_true", help="Perform correlation analysis")
    parser.add_argument("-p", "--plot-graphs", action="store_true", help="Plot graphs")
    parser.add_argument("-all", "--all-functions", action="store_true", help="Run all functions")

    args = parser.parse_args()

    data_file = args.data_file
    rf_data_processing = RFDataProcessing(data_file)

    if args.all_functions:
        args.data_description = True
        args.create_maps = True
        args.apply_maps = True
        args.drop_columns = True
        args.frequency_parser = True
        args.correlation_analysis = True
        args.plot_graphs = True

    if args.data_description:
        rf_data_processing.data_description()

    if args.create_maps:
        modulation_map, device_type_map, antenna_type_map, weather_condition_map, interference_type_map, device_status_map = rf_data_processing.create_maps()

    if args.apply_maps:
        rf_data_processing.apply_maps(rf_data_processing.signals, modulation_map, device_type_map, antenna_type_map, weather_condition_map, interference_type_map, device_status_map)

    if args.drop_columns:
        rf_data_processing.drop_columns()

    if args.frequency_parser:
        rf_data_processing.frequency_parser()

    if args.correlation_analysis:
        if args.data_file == "data/logged_data.csv":
            rf_data_processing.analyze_original_data()
        else:
            rf_data_processing.analyze_frequency()
            rf_data_processing.analyze_modulation()

    if args.plot_graphs:
        if args.data_file == "data/logged_data.csv":
            print("Graph plotting is not applicable for the original data file.")
        else:
            rf_data_processing.analyze_frequency()
            rf_data_processing.analyze_modulation()
