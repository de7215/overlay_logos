import glob
import logging
import os
from overlay_logos import overlay_logos

# Configure logging to display information messages
logging.basicConfig(level=logging.INFO)

# Determine the directory in which this script is located
script_root = os.path.dirname(os.path.abspath(__file__))

# Iterate over all files in the 'partners' subdirectory of 'resources'
for filepath in glob.glob(f'{script_root}/resources/partners/*'):
    # Check if the current item is a file
    if os.path.isfile(filepath):
        # Extract the file name without its extension
        name, _ = os.path.splitext(os.path.basename(filepath))

        # Call the overlay_logos function to overlay logos on a video background
        overlay_logos(
            background=f'{script_root}/resources/background.mp4',  # Path to the background video
            left_logo=f'{script_root}/resources/zkverse.png',  # Path to the left logo
            right_logo=filepath,  # Path to the right logo (from partners directory)
            output_path=f'output/{name}.mp4',  # Output file path and name
            scale_factor=4  # Scale factor for the overlay process
        )
