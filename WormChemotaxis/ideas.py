# Some ideas...

import h5py
import pandas as pd
import matplotlib.pyplot as plt

# Open file
filepath = (
    "Mock_worms/chemotaxis_mock_25825_1_20250725_153953/metadata_featuresN_oneworm.hdf5"
)

with h5py.File(filepath, "r") as f:
    # List all datasets
    print("Datasets:", list(f.keys()))

    # Load trajectories data as DataFrame
    traj_data = pd.DataFrame(f["trajectories_data"][:])

    # Load timeseries features (if present)
    if "timeseries_data" in f:
        timeseries = pd.DataFrame(f["timeseries_data"][:])

    # Load odor patch coordinates
    if "food_cnt_coord" in f:
        odor_patch = f["food_cnt_coord"][:]
        print(f"Odor patch defined by {len(odor_patch)} boundary points")

    # Load skeleton coordinates
    # coords = f['coordinates'][:]  # Shape: (n_frames, n_segments, 2)

print(odor_patch)

# Creating a 2D plot in matplotlib of the odor patch
plt.figure(figsize=(6, 6))

plt.plot(odor_patch[:, 0], odor_patch[:, 1], "r-", label="Odor Patch Boundary")

plt.scatter(
    traj_data["coord_x"], traj_data["coord_y"], s=10, c="blue", label="Worm Trajectory"
)

plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.title("Worm Trajectory and Odor Patch")
plt.legend()
plt.axis("equal")
plt.show()
