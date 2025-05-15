from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import numpy as np

class ImageCaption():
    def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
        self.processor = BlipProcessor.from_pretrained(model_name,use_fast=True)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)

    def generate_caption(self, image_path:str):
        """
        Generate a caption for an image given its file path.
        This method takes an image file path as input, loads and processes the image, 
        and uses the model to generate a descriptive caption for the image's content.
        Args:
            image_path (str): Path to the image file for which a caption is needed.
        Returns:
            str: Generated caption describing the image content.
        """
        raw_image = Image.open(image_path).convert("RGB")
        inputs = self.processor(raw_image, return_tensors="pt")
        out = self.model.generate(**inputs)
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption

    def generate_image_caption(self, image:np.ndarray):
        """
        Generates a caption for the given image.
        Args:
            image (np.ndarray): The input image as a numpy array.
        Returns:
            str: The generated caption for the image.
        Description:
            This method processes the input image using the processor, 
            generates a caption using the model, and decodes the output
            to return a human-readable caption.
        """
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        caption = self.processor.decode(outputs[0], skip_special_tokens=True)
        return caption