# VRS
Script for renaming multiple videos in serial order for organizing them properly for the overall productivity.


This is a Python script that renames videos in a given directory based on their original date and time. The script uses the pyexiv2 library to extract the original date and time of each video file, and then uses this information to construct the new file name.

The script starts by importing the necessary libraries and defining the rename_videos function that takes a single parameter, src_dir, which is the path to the directory containing the videos that need to be renamed.

The function then uses the os.listdir(src_dir) function to get a list of all the files in the source directory. It then iterates over each file in the directory, checks if the file is a video file by checking the file extension and if true it will extract the metadata of the file using the pyexiv2 library. Then it reads the metadata and it looks for the key "Exif.Photo.DateTimeOriginal" to get the original date and time of the video file.

The script then uses the os.path.join() function to construct the full path to the source and destination files. Then it renames the source file to the new file name using the os.rename() function.

Finally, the script calls the rename_videos function and passes in the path to the source directory as the argument. This will rename all the video files in the directory based on their original date and time.

It's important to note that the script uses a try-except block to handle any exceptions that may occur while reading the metadata or trying to rename the files.


# VSDT

This script renames and sorts video files based on the date and time they were recorded. It first iterates through all files in the source directory, checks if the file is a video file by checking the file extension, and if it is, it reads the metadata of the video to get the date and time it was recorded. The script then renames the file by appending the date and time to the file name. The script then creates a list of tuples where each tuple contains the path of the video file and the date and time it was recorded.

After that, the script sorts the list of tuples based on the recorded date and time using the sort() method and a lambda function as the key. Finally, it iterates through the sorted list of tuples and renames the files to their index in the list, this is done so that the files are in sequence in the directory. It pads the index number with zeroes so that the files are sorted lexicographically, this is done by using the zfill() method.
