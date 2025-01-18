```
import json

# Step 1: Create a dictionary (example data or user-defined)
temperature_data = {
    "1850": [-0.6746, -0.3334, -0.5913, -0.5887, -0.5088, -0.3442, -0.1598, -0.2077, -0.3847, -0.5331, -0.2825, -0.4037],
    "1851": [-0.2007, -0.4693, -0.6461, -0.5421, -0.1976, -0.1367, -0.0968, -0.1018, -0.0912, -0.0084, -0.0819, -0.2275],
    "2024": [1.1516, 1.2902, 1.2515, 1.2053, 1.0745, 1.1154, 1.1398, None, None, None, None, None]
}

# Step 2: Write the dictionary to a Python file
output_file_name = "temperature_data_dict.py"

with open(output_file_name, "w") as file:
    # Add a comment and write the dictionary as Python code
    file.write("# Temperature data dictionary\n")
    file.write("temperature_data = ")
    file.write(json.dumps(temperature_data, indent=4))

print(f"Dictionary saved to {output_file_name}")
```
