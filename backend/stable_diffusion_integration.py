import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Load Stable Diffusion pipeline
model_id = "CompVis/stable-diffusion-v1-4"
pipeline = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True)

# Function to generate images

def generate_image(prompt):
    with autocast("cuda"):
        image = pipeline(prompt, guidance_scale=7.5).images[0]
    return image

# Example of usage
if __name__ == '__main__':
    prompt = "A fantasy landscape with mountains and rivers"
    image = generate_image(prompt)
    image.save("output_image.png")