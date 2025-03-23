import numpy as np
from PIL import Image

def flip_image(image_array):
    """Flip the image both horizontally and vertically."""
    return np.flipud(np.fliplr(image_array))

def add_noise(image_array, intensity=30):
    """Add random noise to the image."""
    noise = np.random.randint(-intensity, intensity, image_array.shape, dtype=np.int16)
    noisy_image = image_array.astype(np.int16) + noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

def brighten_channels(image_array, value=40):
    """Increase the brightness of each channel by a fixed value."""
    brightened_image = image_array.astype(np.int16) + value
    return np.clip(brightened_image, 0, 255).astype(np.uint8)

def apply_mask(image_array, mask_size=(100, 100)):
    """Apply a black mask at the center of the image."""
    h, w, _ = image_array.shape
    x_start = (w - mask_size[0]) // 2
    y_start = (h - mask_size[1]) // 2
    image_array[y_start:y_start + mask_size[1], x_start:x_start + mask_size[0]] = [0, 0, 0]
    return image_array

# Load the image using PIL
image_path = "images/birds.jpg"  # Change the path if needed
image = Image.open(image_path)
image_array = np.array(image)

# Apply the transformations
flipped = flip_image(image_array)
noisy = add_noise(image_array)
brightened = brighten_channels(image_array)
masked = apply_mask(image_array.copy())

# Save the transformed images
Image.fromarray(flipped).save("flipped_birds.jpg")
Image.fromarray(noisy).save("noisy_birds.jpg")
Image.fromarray(brightened).save("brightened_birds.jpg")
Image.fromarray(masked).save("masked_birds.jpg")
