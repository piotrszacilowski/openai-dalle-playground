import os

import openai

from fastapi import FastAPI

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")


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
