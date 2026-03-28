# Setting up Stable Diffusion on Google Colab

Follow these step-by-step instructions to set up Stable Diffusion using Google Colab.

## Step 1: Open Google Colab
1. Go to [Google Colab](https://colab.research.google.com/).

## Step 2: Create a New Notebook
1. Click on `File` in the menu.
2. Select `New Notebook` from the dropdown.

## Step 3: Set Up Runtime
1. In the menu, click on `Runtime`.  
2. Select `Change runtime type`.  
3. Set the hardware accelerator to `GPU`.

## Step 4: Install Required Libraries
Run the following code in a cell to install the necessary libraries:
```python
!pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
!pip install transformers
!pip install diffusers
!pip install accelerate
!pip install -U scikit-image
```

## Step 5: Load the Model
Use the following code snippet to load the Stable Diffusion model:
```python
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")
```

## Step 6: Generate Images
To generate images, use this code:
```python
prompt = "A fantasy landscape with mountains and a river"
image = pipe(prompt).images[0]
image.save("output.png")
image.show()
```

## Step 7: Download the Generated Image
You can download the generated image with:
```python
from google.colab import files
files.download("output.png")
```

## Final Steps
You can modify the prompt in Step 6 to create different images. Enjoy generating art with Stable Diffusion!