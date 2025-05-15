import gradio as gr
from caption import ImageCaption
from llm import instagram_caption_expert, generate_caption

captioner = ImageCaption()

def image_caption(image):
    try:
        # caption = captioner.generate_image_caption(image)
        # res = instagram_caption_expert(caption)
        res = generate_caption(image)
        return "test", res
    except Exception as e:
        print(f"Error occurred while generating caption: {e}")
        return "Error {e}", "Error"

app = gr.Interface(image_caption, inputs=gr.Image(height=400), outputs=["text","text"])

if __name__ == "__main__":
    app.launch(debug=True)