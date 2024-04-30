from flask import Blueprint, request, jsonify, send_file
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from app.models.image import Image, db
from PIL import Image as PILImage, ImageOps

api = Blueprint('api', __name__)

@api.route('/get_images', methods=['GET'])
def get_images():
    try:
        depth_min = float(request.args.get('depth_min', 0))
        depth_max = float(request.args.get('depth_max', float('inf')))
        
        # Query images from the database based on depth range
        images = Image.query.filter(Image.depth >= depth_min, Image.depth <= depth_max).all()
        
        results = []
        for img in images:
            # Decode image from binary data
            image_data = PILImage.open(BytesIO(img.image_data))
            
            # Define the custom color map with red, blue and green colors
            colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0)]  # Red, blue, green
            # Convert image to grayscale
            gray_image = image_data.convert('L')
            # Generate color map values
            colormap_values = [colors[int(i / 255 * (len(colors) - 1))] for i in range(256)]
            # Apply color map
            colored_image = ImageOps.colorize(gray_image, colormap_values[0], colormap_values[-1])
            
            # Convert image to PNG format in memory
            buffer = BytesIO()
            colored_image.save(buffer, format='PNG')
            buffer.seek(0)
            
            # Encode image to base64
            import base64
            image_base64 = base64.b64encode(buffer.read()).decode('ascii')
            
            results.append({'depth': img.depth, 'image': image_base64})
        
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
