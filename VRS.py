import os
import datetime
import pyexiv2

def rename_videos(src_dir):
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
            except:
                pass

rename_videos("path/to/src/dir")
