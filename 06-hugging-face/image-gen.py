from huggingface_hub import InferenceClient

prompt = input("Enter a prompt for image generation: ")

client = InferenceClient(
    api_key=""
)

image = client.text_to_image(
    prompt=prompt,
    model="black-forest-labs/FLUX.1-dev"
)

image.show()
image.save("output.png")