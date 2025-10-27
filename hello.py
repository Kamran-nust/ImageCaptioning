# The code creates a Gradio interface called demo using the gr.Interface class. 
# It wraps the greet function with a simple text-to-text user interface that you could interact with.

# The gr.Interface class is initialized with 3 required parameters:

    # fn: the function to wrap a UI around
    # inputs: which component(s) to use for the input (e.g. “text”, “image” or “audio”)
    # outputs: which component(s) to use for the output (e.g. “text”, “image” or “label”)

# The last line demo.launch() launches a server to serve your demo. 

import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860)