# edit these as needed. Always include {context} and {input} in the system_prompt if you want relevant responses

systemprompts = {
    "meeting": {
        "short_description": "Meeting summary",
        "system_prompt": """You're an efficient and detail oriented executive assistant. You never make things up and you only base your output on available context. Answer the following question based ONLY on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""",
        "default_question": "Summarize the meeting and itemize any actions agreed, including responsible parties and timelines",
        "selected": True,
    },
    "text": {
        "short_description": "Text summary",
        "system_prompt": """Forget everything about books. Books don't exist. Answer the following question based ONLY on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""",
        "default_question": "Outline the setting described and any characters mentioned. If there is a discernible plot, describe the most significant plot elements in detail.",
        "selected": False,
    },
}

import ollama
import sys

default_model = "qwen2.5:32b-instruct"

availablemodels = {
    entry["model"]: {"short_description": str(entry["details"])}
    for entry in ollama.list()["models"]
}

# Automatically select the default model if it's available
if default_model in availablemodels:
    for model in availablemodels:
        availablemodels[model]["selected"] = model == default_model
else:
    # If the default model isn't available, select the first model
    first_model = next(iter(availablemodels), None)
    if first_model:
        availablemodels[first_model]["selected"] = True
