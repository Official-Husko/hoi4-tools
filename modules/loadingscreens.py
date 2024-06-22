# Import Standard Libraries
import os
import glob
from PIL import Image

# Import Third-Party Libraries


# Import Local Libraries


class LoadingScreens:
    def __init__(self, path_to_project):
        self.path_to_project = path_to_project
        self.loadingscreens_path = os.path.join(self.path_to_project, "gfx", "loadingscreens")

    def process_images(self):

        # Get all files in loadingscreens_path and convert them to dds using PIL without resizing
        for image_file in glob.glob(os.path.join(self.loadingscreens_path, ('*.png', '*.jpg', '*.jpeg'))):

            # Create DDS file path in the same directory as original image
            dds_filename = os.path.splitext(os.path.basename(image_file))[0] + ".dds"
            dds_path = os.path.join(os.path.dirname(image_file), dds_filename)

            # Save resized image as DDS in the same directory
            with Image.open(image_file) as img:
                img.save(dds_path, format='DDS')