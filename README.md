# Video Logo Overlay Tool
This Python script provides a simple way to overlay two logo images onto a video. It is especially useful for adding logos or watermarks to videos for branding or identification purposes.

## Prerequisites
Before you can use this tool, make sure you have the following installed:

- Python 3.x
- OpenCV (cv2) library
- argparse library (usually included in Python standard library)

You can install OpenCV using pip:

```bash
pip install opencv-python-headless -i https://pypi.org/simple 
```
## Usage
### Running the Script
To overlay logos on a video, run the script overlay_logos.py with the following command:
```bash
python overlay_logos.py --background <path_to_video> --left-logo <path_to_left_logo> --right-logo <path_to_right_logo> --output <output_video_path> --scale_factor <scale_factor>
```

- `<path_to_video>`: The path to the input video file.
- `path_to_left_logo>`: The path to the first logo image file.
- `<path_to_right_logo>`: The path to the second logo image file.
- `<output_video_path>`: The path to save the output video file.
- `<scale_factor> (optional)`: Scaling factor for logos (default: 4).
### Example
Here's an example of how to use the script:

```bash
python overlay_logos.py --background resources/background.mp4 --left-logo resources/zkverse.png --right-logo resources/partners/tensor.png --output output/zktensor.mp4 --scale_factor 6
```

This command will overlay `zkverse.png` on the left side of each frame and `tensor.png` on the right side of each frame in the `background.mp4`, and save the resulting video as `zktensor.mp4`. The scale factor for the logos is set to 6.

### Example Usage with example.py
For a practical demonstration of how to use the Video Logo Overlay Tool, refer to the `example.py` file included in this package. This file contains a sample script that illustrates the basic usage of the tool with predefined paths and parameters.

#### How to Run the Example
To run the example, navigate to the directory containing `example.py` and execute the following command in your terminal:

```bash
python example.py
```

The `example.py` script is pre-configured with sample paths for the background video, left and right logos, and the output video path. It also sets an example scale factor for the logos. Running this script will produce an output video demonstrating the overlay capabilities of the tool.

#### Input Structure Example
```
./resources
│   background.mp4
│   zkverse.png
└───partners
        madlads.jpg
        tensor.png
```

This structure is helpful for users to understand the expected directory setup for the script.

#### Customizing the Example
You can modify the `example.py` file to test different videos, logos, and scale factors. This is an excellent way to familiarize yourself with the tool's functionality and to see firsthand how various inputs affect the final output.

## Features
Supports overlaying two logo images on a video.
Resizes the logos to fit the video frame while maintaining aspect ratio.
Customizable scaling factor for logos.
Output video is saved in the mp4 format.
## Error Handling
The script includes error handling to check for missing or invalid file paths and provides informative error messages.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This script utilizes the OpenCV library for image and video processing.
Feel free to customize the script to suit your specific needs and branding requirements.