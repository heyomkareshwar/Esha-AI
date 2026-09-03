import os
from io import BytesIO

from dotenv import load_dotenv
from google import genai


load_dotenv()


class GeminiVision:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured."
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def analyze(self, image, prompt):

        buffer = BytesIO()

        image.save(
            buffer,
            format="PNG"
        )

        image_bytes = buffer.getvalue()

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=[
                prompt,
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": image_bytes,
                    }
                },
            ],
        )

        return response.text.strip()