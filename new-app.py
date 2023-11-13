import gradio as gr

TARGET_LANGUAGE = {"French": "fr", "German": "de", "Spanish": "es", "Italian": "it"}
FONT_TYPE = {"Arial": "./fonts/Arial.ttf"}
FONT_COLOR = {"Blue": "blue", "Black": "black"}
FONT_SIZE = {"7": 7, "8": 8, "9": 9}


## Function to process the input image
# def process_image(image, data, language, font_type, font_size, font_color):
#     image = image[..., ::-1]
#     return image, language, font_type, font_size, font_color


def process_image(image):
    image = image[..., ::-1]
    return image, gr.Radio(visible=True, interactive=True)


# Function to perform another action on the processed image
def another_function(image):
    image = image[..., ::-1]
    return image


# with gr.Blocks() as demo:
#     image = gr.Image(label="Input Image")
#     data = gr.UploadButton(label="JSON File")
#     language = gr.Dropdown(
#         label="Target Language", choices=list(TARGET_LANGUAGE.keys())
#     )
#     font_type = gr.Dropdown(label="Font Type", choices=list(FONT_TYPE.keys()))
#     font_size = gr.Dropdown(label="Font Size", choices=list(FONT_SIZE.keys()))
#     font_color = gr.Dropdown(label="Font Color", choices=list(FONT_COLOR.keys()))
#     translate = gr.Button("Translate")
#     output = gr.Image(label="Translation Output")
#     translate.click(
#         fn=process_image,
#         inputs=[image, data, language, font_type, font_size, font_color],
#         outputs=[output, gr.Text(), gr.Text(), gr.Text(), gr.Text()],
#     )

# demo.launch()


# def display_options(choice):
#     if choice == "Edit":
#         return gr.Button(visible=True, interactive=True), gr.Image(visible=True)
#     elif choice == "I am good!":
#         return gr.Button(visible=False), gr.Image(visible=False)


def update_visibility():
    return gr.Image(visible=True)


def display_options(choice):
    # print("====== Start")
    # print("choice: ", choice)
    # print("====== End")
    # print()

    if choice == "edit":
        return [
            gr.Dropdown(visible=True, interactive=True),
            gr.Dropdown(visible=True, interactive=True),
            gr.Dropdown(visible=True, interactive=True),
            gr.Button(visible=True, interactive=True),
        ]
    else:
        return [
            gr.Dropdown(visible=False),
            gr.Dropdown(visible=False),
            gr.Dropdown(visible=False),
            gr.Button(visible=False),
        ]


with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Image Translation
        This is a demo for Image Tranlation App
        """
    )

    image = gr.Image(label="Input Image")
    data = gr.UploadButton(label="JSON File")
    language = gr.Dropdown(
        label="Target Language", choices=list(TARGET_LANGUAGE.keys())
    )

    font_type = gr.Dropdown(label="Font Type", choices=list(FONT_TYPE.keys()))
    font_size = gr.Dropdown(label="Font Size", choices=list(FONT_SIZE.keys()))
    font_color = gr.Dropdown(label="Font Color", choices=list(FONT_COLOR.keys()))
    translate = gr.Button("Translate")
    output = gr.Image(label="Translation Output", interactive=False)
    radio = gr.Radio(
        ["edit", "none"], label="Do you want to edit this output?", visible=False
    )

    translate.click(fn=process_image, inputs=image, outputs=[output, radio])

    output_image = gr.Image(label="Output Image", visible=False)

    font_type = gr.Dropdown(
        label="Font Type", choices=list(FONT_TYPE.keys()), visible=False
    )
    font_size = gr.Dropdown(
        label="Font Size", choices=list(FONT_SIZE.keys()), visible=False
    )
    font_color = gr.Dropdown(
        label="Font Color", choices=list(FONT_COLOR.keys()), visible=False
    )

    edit_button = gr.Button("Edit Image", visible=False)

    radio.change(
        fn=display_options,
        inputs=radio,
        outputs=[font_type, font_size, font_color, edit_button],
    )

    edit_button.click(fn=another_function, inputs=output, outputs=output_image)


demo.launch()
