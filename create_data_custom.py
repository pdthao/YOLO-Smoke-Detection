import yaml

# Read class names from classes.txt
with open("D:/waferData/degas/labelApp/data/predefined_classes.txt", "r") as f:
    classes = [line.strip() for line in f if line.strip()]

# Create the YAML configuration dictionary
data_config = {
    "train": "D:/waferData/degas/label/train/",  # update this path as needed
    "val": "D:/waferData/degas/label/val/",      # update this path; you can also point to the same folder as train if needed
    "nc": len(classes),               # number of classes
    "names": classes                  # list of class names
}

# Write the configuration to data_custom.yaml
with open("data_custom.yaml", "w") as f:
    yaml.dump(data_config, f, default_flow_style=False)
