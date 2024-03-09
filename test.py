import e57
import csv

# Replace "e57_file.e57" with your actual file path
e57_data = e57.read_points("File Type E57 TEST Scans/1_Mudroom_Garage_and_Laundry_Door.e57")
# Select desired data fields (adjust according to your needs)
print(e57_data)
"""
point_cloud = e57_data.points  # Assuming data is at index 0 in your file
x_coords = [point_cloud[i][0] for i in range(len(point_cloud))]
y_coords = [point_cloud[i][1] for i in range(len(point_cloud))]
z_coords = [point_cloud[i][2] for i in range(len(point_cloud))]

# Prepare CSV header
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["X", "Y", "Z"])
    
    for x, y, z in zip(x_coords, y_coords, z_coords):
        writer.writerow([x, y, z])

print("Successfully converted e57 data to CSV!")
"""
