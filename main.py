import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

count_info_path = "GSE60450_GeneLevel_NormalizedCPM.and_.TMM_data.csv"
sample_info_path = "GSE60450_filtered_metadata-1.csv"

# Set display options to show all columns
pd.set_option('display.max_columns', None)
# Optional: Adjust width if columns are wrapping
pd.set_option('display.width', 1000)  # Adjust as needed
# Optional: Show more rows if needed
pd.set_option('display.max_rows', None)

count = pd.read_csv(count_info_path)
sample_info = pd.read_csv(sample_info_path)
