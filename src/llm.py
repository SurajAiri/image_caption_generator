from litellm import completion
from dotenv import load_dotenv
import os


load_dotenv()

model = "gemini/gemini-1.5-flash"
api_key = os.environ['GOOGLE_API_KEY'] 

def instagram_caption_expert(desc:str):
    prompt = "You are a social media expert. Write a compelling Instagram caption with relevant hashtags for an image of `{image}`. Return only the caption and hashtags—nothing else.".format(image=desc)
    res = completion(model,[{"role":"user","content":prompt}],api_key=api_key)
    return res.choices[0].message.content


import os
import base64
import cv2
import numpy as np
def generate_caption( image: np.ndarray = None) -> str:
    """
    Generate a caption using Google's Gemini model via litellm.
    
    Args:
        image: numpy array containing the image data

    Returns:
        The generated caption text
    """
    try:
        prompt = "You are a social media expert. Write a compelling Instagram caption with relevant hashtags for the given image. Return only the caption and hashtags - nothing else."        
        # Prepare messages
        messages = [{"role": "user", "content": prompt}]
        
        # If image is provided, encode it and include in the request
        if image is not None:
            
            # Convert image to JPEG bytes
            _, buffer = cv2.imencode('.jpg', image)
            image_data = base64.b64encode(buffer).decode('utf-8')
            
            messages = [
                {
                    "role": "user", 
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
                    ]
                }
            ]
        
        # Make the API call
        response = completion(
            model="gemini/gemini-1.5-flash",  # Using the model defined at the top
            messages=messages,
            api_key=api_key,
            temperature=0.7,
            max_tokens=300
        )
        
        # Extract and return the response text
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error generating caption: {str(e)}")
        return f"Error: {str(e)}"