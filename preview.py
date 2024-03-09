import e57
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def preview_e57(input_file):
    # Open the E57 file
    reader = e57.read_points(input_file)

    # Initialize lists to store coordinates
    x_coords = []
    y_coords = []
    z_coords = []

    # Iterate over each point record in the E57 file
    for data in reader.read_scan_data(0):  # Assuming there is only one scan in the E57 file
        # Extract coordinates
        x = data.cartesianX
        y = data.cartesianY
        z = data.cartesianZ

        # Append coordinates to lists
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)

    # Create 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_coords, y_coords, z_coords, s=1, c='b', marker='o')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Preview of E57 Point Cloud')

    # Show plot
    plt.show()

# Example usage
input_file = "File Type E57 TEST Scans/1_Mudroom_Garage_and_Laundry_Door.e57"  # Specify the path to your input E57 file
preview_e57(input_file)
