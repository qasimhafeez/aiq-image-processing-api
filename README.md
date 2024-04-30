## README

---

# Image Processing API

## Overview

This project provides a Python-based image processing application that resizes large images, applies custom color maps, and stores them for efficient retrieval based on depth ranges. Built with Flask, the application features a Docker containerized setup for easy deployment and scalability.

## Features

- **Image Resizing:** Reduces image width from 200 pixels to 150 pixels.
- **Custom Color Maps:** Enhances image visualization by applying custom color maps.
- **Depth-based Retrieval:** Fetches images based on user-specified depth ranges via a RESTful API.
- **Docker Support:** Containerized application for straightforward setup and deployment.
- **Caching:** Optional Redis caching to enhance performance for frequent queries (LRU cache).

## Prerequisites

Before you begin, ensure you have Docker and Docker Compose installed on your system. These tools are essential for building and running the application in a containerized environment.

## Installation

1. **Build the Docker container:**

   ```bash
   docker-compose build
   ```

2. **Run the application:**
   ```bash
   docker-compose up
   ```

The application will be accessible at `http://127.0.0.1:5000/`.

## API Usage

### Retrieve Images

**Endpoint:** `/api/get_images`

**Method:** `GET`

**Parameters:**

- `depth_min` (float): The minimum depth of the image to retrieve.
- `depth_max` (float): The maximum depth of the image to retrieve.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:5000/api/get_images?depth_min=9001.5&depth_max=9002.6"
```

**Response:**
A JSON object containing the array of image data that falls within the specified depth range.

## Room for improvements

- Redis can be implement to enchance the problem
- Logger can be added in some part of the application for better messages. For Example, if there data inside csv file is null/empty it should notify.
- Small React application which takes data in base64 and then decode it to show the image layers visually.
- Parallel processing can be implemented, if the CSV file is too large
- We can store data in big chunks to avoid database heatup.

## Thank you
