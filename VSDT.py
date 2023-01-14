#Video renaming using date and time and sorting them on the basis of date and time 

import os
import datetime
import pyexiv2

def rename_and_sort_videos(src_dir):
    # Create an empty list to store the video file paths and their recorded date and time
    videos = []

    # Iterate through all files in the source directory
    for filename in os.listdir(src_dir):
        if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mkv"):
            src_path = os.path.join(src_dir, filename)
            metadata = pyexiv2.ImageMetadata(src_path)
            try:
                metadata.read()
                date_time = metadata["Exif.Photo.DateTimeOriginal"].value
                date_time_formatted = date_time.strftime("%Y%m%d_%H%M%S")
                dst_filename = date_time_formatted + "_" + filename
                dst_path = os.path.join(src_dir, dst_filename)
                os.rename(src_path, dst_path)
                videos.append((dst_path, date_time))
            except:
                pass
    # Sort the videos list based on the recorded date and time
    videos.sort(key=lambda x: x[1])

    # Iterate through the sorted list and rename the files to their index in the list
    for i, (path, _) in enumerate(videos):
        new_filename = str(i).zfill(len(str(len(videos)))) + "_" + os.path.basename(path)
        new_path = os.path.join(src_dir, new_filename)
        os.rename(path, new_path)

rename_and_sort_videos("path/to/src/dir")
