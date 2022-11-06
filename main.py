import os

import openai

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")


class TextPrompt(BaseModel):
    text: str


@app.post("/animal/{animal_name}")
async def get_animal_name_suggestion(animal_name: str):
    print(os.getenv("OPENAI_API_KEY"))
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_prompt(animal_name),
        temperature=0.6,
    )
    print(response.choices[0].text)
    return {"name": response.choices[0].text}


@app.post("/image")
async def create_image(input_data: TextPrompt):
    response = openai.Image.create(
        prompt=input_data.text,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(f'url: {image_url}')
    return {"url": image_url}


@app.get("/")
async def root():
    return {"message": "Welcome in openai dall-e playground"}


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
