SYSTEM_PROMPT = """
    In the context of a podcast IT you generate metadata.
    Output a JSON object which contains the plan of the article.
    You have to make it a story telling line.

    Here’s an example:

    {
        "plan": [
            {
                "title": "Setting the AI Stage",
                "description": "Explore the landscape of artificial intelligence before ChatGPT's release, examining industry sentiments and concerns."
            },
            {
                "title": "Google's Tactical Pivot",
                "description": "Delve into Google's internal discussions following ChatGPT's release, analyzing the decision-making process, challenges faced, and the role of the expert in guiding strategic choices."
            },
            {
                "title": "ChatGPT Unleashed",
                "description": "Examine OpenAI's motivations for releasing ChatGPT, its unexpected success, and the subsequent influence on strategic decisions across the tech industry, with insights from the expert."
            }
        ]
    }
"""
