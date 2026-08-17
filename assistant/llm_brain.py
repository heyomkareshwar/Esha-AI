import json
import urllib.request


class LLMBrain:

    def __init__(
        self,
        model="mistral:latest",
        host="http://localhost:11434"
    ):
        self.model = model
        self.host = host

    def ask(self, prompt):

        url = f"{self.host}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        data = json.dumps(
            payload
        ).encode("utf-8")

        request = urllib.request.Request(
            url,
            data=data,
            headers={
                "Content-Type":
                    "application/json"
            }
        )

        try:

            with urllib.request.urlopen(
                request,
                timeout=120
            ) as response:

                result = json.loads(
                    response.read().decode(
                        "utf-8"
                    )
                )

            return result.get(
                "response",
                ""
            ).strip()

        except Exception as error:

            print(
                "[LLM ERROR]",
                error
            )

            return (
                "I'm having trouble "
                "connecting to my AI brain."
            )