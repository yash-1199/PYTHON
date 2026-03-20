import csv
import psutil
import os

def get_total_ram():
    return psutil.virtual_memory().total / (1024 ** 3)  # GB

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)  # MB

def read_csv(file_path):
    data = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data

# Get total RAM
print(f"Total RAM: {get_total_ram():.2f} GB")

# Directory
data_dir = "Data\\raw\\"

csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

for csv_file in csv_files:
    file_path = os.path.join(data_dir, csv_file)
    print(f"\nReading {csv_file}:")
    print("Before reading:", get_memory_usage(), "MB")
    data = read_csv(file_path)
    print("After reading:", get_memory_usage(), "MB")
    print(f"Loaded {len(data)} rows")

# Load all files at once
print("\nLoading all files at once:")
print("Before loading all:", get_memory_usage(), "MB")

all_data = {}
total_rows = 0
for csv_file in csv_files:
    file_path = os.path.join(data_dir, csv_file)
    all_data[csv_file] = read_csv(file_path)
    total_rows += len(all_data[csv_file])

print("After loading all:", get_memory_usage(), "MB")
print(f"Total rows loaded: {total_rows}")

# Verify data is loaded by printing a sample from the first file
if csv_files:
    first_file = csv_files[0]
    if all_data[first_file]:
        print(f"\nSample data from {first_file}:")
        print(all_data[first_file][0])  # Print the first row