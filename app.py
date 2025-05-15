import gradio as gr
from src.caption import ImageCaption
from src.llm import instagram_caption_expert, generate_caption

captioner = ImageCaption()

def image_caption(image):
    try:
        caption = captioner.generate_image_caption(image)
        res = instagram_caption_expert(caption)
        return caption, res
    except Exception as e:
        print(f"Error occurred while generating caption: {e}")
        return f"Error {e}", "Error"

app = gr.Interface(image_caption, inputs=gr.Image(height=400,label="Input Image"), outputs=[gr.Text(label="Image description"),gr.Text(label="Instagram caption with hashtag")],title="Instagram Caption Generator v1",
    description="Upload an image to generate an engaging Instagram caption with relevant hashtags. This is firstly generate image description locally and then sends that image description to llm so can be cheap but might not be that much accurate.")

if __name__ == "__main__":
    app.launch(debug=True)