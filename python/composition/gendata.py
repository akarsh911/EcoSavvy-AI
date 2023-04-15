import random
import csv

# Set the number of samples to generate
num_samples = 1000

# Set the range of values for each feature
product_types = ['Laptop', 'Mobile Phone', 'Tablet', 'Desktop Computer']
min_weight = 100  # in grams
max_weight = 10000  # in grams
min_battery = 0  # in milliampere-hours (mAh)
max_battery = 5000  # in milliampere-hours (mAh)
min_screen_size = 3  # in inches
max_screen_size = 20  # in inches
min_ram = 1  # in gigabytes (GB)
max_ram = 64  # in gigabytes (GB)
min_storage = 8  # in gigabytes (GB)
max_storage = 512  # in gigabytes (GB)

# Generate random samples
samples = []
for i in range(num_samples):
    product_type = random.choice(product_types)
    weight = random.randint(min_weight, max_weight)
    battery = random.randint(min_battery, max_battery)
    screen_size = random.uniform(min_screen_size, max_screen_size)
    ram = random.randint(min_ram, max_ram)
    storage = random.randint(min_storage, max_storage)
    samples.append([product_type, weight, battery, screen_size, ram, storage])

# Write the samples to a CSV file
with open('e-waste_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['product_type', 'weight', 'battery',
                    'screen_size', 'ram', 'storage', 'composition'])
    for sample in samples:
        writer.writerow(sample + [random.uniform(0, 100)])
