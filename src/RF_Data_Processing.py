import pandas as pd
import os

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
            "QPSK": 4,
        }
        device_type_map = {
            "Halow-U": 1,
            "HackRF": 2,
            "SteamDeck": 3,
        }
        antenna_type_map = {
            "Dipole": 1,
            "Yagi": 2,
            "Directional": 3,
            "Omnidirectional": 4,
        }
        weather_condition_map = {
            "Sunny": 1,
            "Cloudy": 2,
            "Rainy": 3,
        }
        interference_type_map = {
            "None": 1,
            "Intermodulation": 2,
            "Co-channel": 3,
            "Adjacent-channel": 4,
        }
        device_status_map = {
            "Running game": 1,
            "Streaming I/Q data": 2,
            "Transmitting beacon signals": 3,
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
        output_directory = "../Data/Frequency_data"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for frequency in unique_frequencies:
            frequency_mhz = frequency / 1000000.0  # Convert frequency to MHz
            frequency_mhz_str = str(int(frequency_mhz)) + "MHz"
            frequency_df = self.signals[self.signals["Frequency"] == frequency]

            # Save the data frame to a CSV file
            with open(os.path.join(output_directory, f"{frequency_mhz_str}.csv"), "w", newline="") as f:
                frequency_df.to_csv(f, index=False)

    def analyze_correlation(self):
        """Compute the correlation matrix and print the correlated categories."""
        columns_to_analyze = [
            'Timestamp', 'Frequency', 'Signal Strength', 'Modulation', 'Bandwidth', 'Device Type',
            'Antenna Type', 'Temperature', 'Precipitation', 'Weather Condition', 'Interference Type',
            'Device Status'
        ]
        corr_matrix = self.signals[columns_to_analyze].corr()
        for col1 in corr_matrix.columns:
            for col2 in corr_matrix.columns:
                if col1 != col2:
                    correlation = corr_matrix.loc[col1, col2]
                    if correlation >= 0.5 or correlation <= -0.5:
                        print(f"Correlation between {col1} and {col2}: {correlation}")


if __name__ == "__main__":
    data_file = "../data/logged_data.csv"
    rf_data_processing = RFDataProcessing(data_file)

    rf_data_processing.data_description()
    rf_data_processing.create_maps()

    modulation_map, device_type_map, antenna_type_map, weather_condition_map, interference_type_map, device_status_map = rf_data_processing.create_maps()
    rf_data_processing.apply_maps(rf_data_processing.signals, modulation_map, device_type_map, antenna_type_map, weather_condition_map, interference_type_map, device_status_map)

    rf_data_processing.drop_columns()
    rf_data_processing.frequency_parser()
    rf_data_processing.analyze_correlation()
