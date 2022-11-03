# openai dall-e playground

A playground to work with the [Dall-e API](https://openai.com/blog/dall-e-api-now-available-in-public-beta/) based on FastAPI framework.

## Setup

1. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

2. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

3. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

4. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

5. Run the app

   ```bash
   $ uvicorn main:app --reload
   ```

You should now be able to access the app at [http://localhost:8000](http://localhost:8000)!

Based on [OpenAI Flask tutorial](https://beta.openai.com/docs/quickstart) but made in FastAPI ❤️
