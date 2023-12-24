import gradio as gr
import threading
import time

counter = 0

def background_task():
    global counter
    while True:
        counter += 2
        print(f"Counter: {counter}")
        time.sleep(2)  # Sleep for 5 seconds

def add_two():
    return counter

# Start the background task in a separate thread
background_thread = threading.Thread(target=background_task)
background_thread.daemon = True
background_thread.start()

iface = gr.Interface(fn=add_two, 
                     inputs= None,
                     outputs="text",
                     live=True, 
                     capture_session=True)
iface.launch()
