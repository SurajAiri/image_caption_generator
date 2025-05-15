import gradio as gr
from src.caption import ImageCaption
from src.llm import  generate_caption

captioner = ImageCaption()

def image_caption(image):
    try:
        res = generate_caption(image)
        return  res
    except Exception as e:
        print(f"Error occurred while generating caption: {e}")
        return "Error {e}"

app = gr.Interface(
    fn=image_caption, 
    inputs=gr.Image(height=400), 
    outputs=gr.Text(label="Instagram caption with relevant hashtag"),
    title="Instagram Caption Generator v2",
    description="Upload an image to generate an engaging Instagram caption with relevant hashtags. This directly sends image to llm model so require multi-modal model support and can be costly"
)

if __name__ == "__main__":
    app.launch(share=True)