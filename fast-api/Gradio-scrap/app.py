import gradio as gr
from gradio_client import Client


set_url = ""

def statementdata_url(url):
    global set_url 
    set_url= url
    return set_url
def outputs_url():
    return set_url
def scrap_statement(name):
    if set_url == "":
        return "Not found url"
    client = Client(set_url)
    result = client.predict(
            name,	# str  in 'parameter_2' Textbox component
            fn_index=0
    )
    return result

with gr.Blocks() as iface:
    with gr.Tab("set_url"):
        url_n_input = gr.Textbox()
        url_n_output = gr.Textbox()
        url_n_button = gr.Button("set")
    with gr.Tab("outputs_url"):
        urls_n_output = gr.Textbox()
        urls_n_button = gr.Button("send")
    with gr.Tab("statement_scrap"):
        st_n_input = gr.Textbox()
        st_n_output = gr.Textbox()
        st_n_button = gr.Button("statement")

    url_n_button.click(statementdata_url, inputs = url_n_input, outputs=url_n_output)
    urls_n_button.click(outputs_url, inputs = None, outputs = urls_n_output)
    st_n_button.click(scrap_statement, inputs=st_n_input, outputs=st_n_output)

iface.launch()