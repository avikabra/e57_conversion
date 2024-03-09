import numpy as np
import open3d as o3d
from sklearn.cluster import KMeans, DBSCAN, OPTICS
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Read point cloud:
pcd = o3d.io.read_point_cloud("File Type E57 TEST Scans/C.pcd")
# Get points and transform it to a numpy array:
points = np.asarray(pcd.points).copy()

# Get labels:
labels = model.labels_
# Get the number of colors:
n_clusters = len(set(labels))

# Mapping the labels classes to a color map:
colors = plt.get_cmap("tab20")(labels / (n_clusters if n_clusters > 0 else 1))
# Attribute to noise the black color:
colors[labels < 0] = 0
# Update points colors:
pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

# Display:
o3d.visualization.draw_geometries([pcd])
# Normalisation:
scaled_points = StandardScaler().fit_transform(points)
# Clustering:
model = KMeans(n_clusters=4)
model.fit(scaled_points)
# Normalisation:
scaled_points = StandardScaler().fit_transform(points)
# Clustering:
model = DBSCAN(eps=0.15, min_samples=10)
model.fit(scaled_points)
# Project points on OXZ plane:
points[:, 1] = 0
pcd_projected = o3d.geometry.PointCloud()  # create point cloud object
pcd_projected.points = o3d.utility.Vector3dVector(points)  # set pcd_np as the point cloud points
o3d.visualization.draw_geometries([pcd_projected])
# projection: caonsider the x and z coordinates (y=0)
points_xz = points[:, [0, 2]]

# Normalisation:
scaled_points = StandardScaler().fit_transform(points_xz)

# Clustering:
model = DBSCAN(eps=0.15, min_samples=10)
model.fit(scaled_points)
