import pandas as pd
from PIL import Image as PILImage
import numpy as np
from io import BytesIO
from app.models.image import Image, db

def read_and_process_csv(csv_file_path):
    print("inside csv file")
    df = pd.read_csv(csv_file_path)
    
    # Drop rows where any of the required columns ('depth' or any pixel columns) are NaN
    df = df.dropna(subset=['depth'] + [f'col{i}' for i in range(1, 201)])  

    for index, row in df.iterrows():
        depth = row['depth']
        pixel_values = row[1:]  # Extract pixel values
        image_data = np.array(pixel_values, dtype=np.uint8)  # Convert pixel values to uint8
        
        # Reshape the pixel data by keeping orignal height only adjusting width
        image_data = image_data.reshape(1, -1)
        image = PILImage.fromarray(image_data)
        
        # Resize image while maintaining aspect ratio
        new_width = 150
        aspect_ratio = image.width / float(image.height)
        new_height = int(new_width / aspect_ratio)

        # Skip resizing if new height is zero
        if new_height <= 0:
            resized_image = image
        else:
            resized_image = image.resize((new_width, new_height))
  
        # Convert resized image to binary format for storage
        buffer = BytesIO()
        resized_image.save(buffer, format='PNG')
        image_bytes = buffer.getvalue()
        
        # Create and save the image to the database
        if not pd.isna(depth):
            image_model = Image(depth=depth, image_data=image_bytes)
            db.session.add(image_model)
    print("stored image data into db")
    db.session.commit()
