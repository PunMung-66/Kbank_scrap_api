from gradio_client import Client

client = Client("https://punnawat01-gradio-scrap.hf.space/")
result = client.predict(
				"Pun_o_o",	# str in 'parameter_3' Textbox component
				fn_index=0
)
print(result)