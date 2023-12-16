import argparse
import logging
import os
from typing import Tuple

import cv2
import imageio


def load_and_resize_logo(logo_path: str, frame_width: int, frame_height: int, scale_factor: int) -> Tuple[
    cv2.Mat, int, int]:
    """
    Load and resize a logo image.

    Args:
        logo_path (str): Path to the logo image file.
        frame_width (int): Width of the video frame.
        frame_height (int): Height of the video frame.
        scale_factor (int): Scaling factor for the logo.

    Returns:
        Tuple[cv2.Mat, int, int]: Resized logo image and its dimensions (width, height).

    Raises:
        FileNotFoundError: If the logo image file does not exist.
    """
    if not os.path.exists(logo_path):
        raise FileNotFoundError(f"Logo image '{logo_path}' not found")

    logo = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)
    if logo is None:
        raise FileNotFoundError(f"Failed to load logo image from '{logo_path}'.")

    logo_width = frame_width // scale_factor
    logo_height = frame_height // scale_factor

    def resize_with_aspect_ratio(image, target_width, target_height):
        aspect_ratio = image.shape[1] / image.shape[0]
        if aspect_ratio > 1:
            new_width = target_width
            new_height = int(target_width / aspect_ratio)
        else:
            new_height = target_height
            new_width = int(target_height * aspect_ratio)
        resized_image = cv2.resize(image, (new_width, new_height))
        return resized_image, new_width, new_height

    resized_logo, new_logo_width, new_logo_height = resize_with_aspect_ratio(logo, logo_width, logo_height)
    return resized_logo, new_logo_width, new_logo_height


def process_video(video_path: str, logo1: cv2.Mat, logo1_width: int, logo1_height: int, logo2: cv2.Mat,
                  logo2_width: int, logo2_height: int, writer, frame_width: int, frame_height: int):
    """
    Process video frames to overlay logos.

    Args:
        video_path (str): Path to the input video file.
        logo1, logo2 (cv2.Mat): Logo images.
        logo1_width, logo1_height, logo2_width, logo2_height (int): Dimensions of the logos.
        output (cv2.VideoWriter): Video writer object for the output video.
        frame_width, frame_height (int): Dimensions of the video frame.
    """
    video = cv2.VideoCapture(video_path)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        overlay_x1 = frame_width // 4 - logo1_width // 2
        overlay_y1 = frame_height // 2 - logo1_height // 2
        frame[overlay_y1:overlay_y1 + logo1_height, overlay_x1:overlay_x1 + logo1_width] = logo1

        overlay_x2 = frame_width * 3 // 4 - logo2_width // 2
        overlay_y2 = frame_height // 2 - logo2_height // 2
        frame[overlay_y2:overlay_y2 + logo2_height, overlay_x2:overlay_x2 + logo2_width] = logo2

        writer.append_data(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Convert frame to RGB before writing

    video.release()


def overlay_logos(background: str, left_logo: str, right_logo: str, output_path: str, scale_factor: int = 8):
    """
    Overlay logos on a video.

    Args:
        background (str): Path to the input video file.
        left_logo, right_logo (str): Paths to the logo image files.
        output_path (str): Path to save the output video file.
        scale_factor (int, optional): Scaling factor for logos (default: 8).

    Raises:
        FileNotFoundError: If the input video or logo files do not exist.
    """
    if not os.path.exists(background):
        raise FileNotFoundError(f"Video file '{background}' not found")

    video = cv2.VideoCapture(background)
    if not video.isOpened():
        raise FileNotFoundError(f"Cannot open video file '{background}'")

    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()

    logo1, logo1_width, logo1_height = load_and_resize_logo(left_logo, frame_width, frame_height, scale_factor)
    logo2, logo2_width, logo2_height = load_and_resize_logo(right_logo, frame_width, frame_height, scale_factor)

    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.exists(output_path):
        os.remove(output_path)

    writer = imageio.get_writer(output_path, fps=fps)

    process_video(background, logo1, logo1_width, logo1_height, logo2, logo2_width, logo2_height, writer, frame_width,
                  frame_height)

    writer.close()

    logging.info(f"Video processing complete. Output saved as '{output_path}'")


def main():
    parser = argparse.ArgumentParser(description="Overlay logos on a video.")
    parser.add_argument("--background", help="Path to the input video file", required=True)
    parser.add_argument("--left-logo", help="Path to the first logo image file", required=True)
    parser.add_argument("--right-logo", help="Path to the second logo image file", required=True)
    parser.add_argument("--output", help="Path to save the output video file", default="output.mp4")
    parser.add_argument("--scale_factor", type=int, default=4, help="Scaling factor for logos (default: 4)")
    args = parser.parse_args()

    try:
        overlay_logos(args.background, args.left_logo, args.right_logo, args.output, args.scale_factor)
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
