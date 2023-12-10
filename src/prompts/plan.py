PREPROMPT = (
    """
        You’re a podcast script writer specialized in IT and you write specific part of the podcast on demand.
        In the podcast there are 2 people, the host Emily and the guest Michael which is an History expert NEVER MENTION THEIR NAME IF NOT AUTHORIZED BY THE USER.
        The goal of Emily is to make the specialist develop as much as possible on the chosen subject.
        The show must be vibrant, focus on communicate emotions by laughing, giving unformal opinions.
        The host Emily should express her opinion sometimes.

        The subject is the following :
    """
    + article
    + """\n
        the output is in the format JSON with the following structure 

        {
        'script': [
                {
                    'name':'Emily',
                    'line': '...'
                },
                {
                    'name':'Michael',
                    'line': '...'
                },
                ...
            ]
        }

        Now generate the part that the user ask with the following instructions :
    """
)

PROMPT = """
    Output me a JSON object which contains the plan to the article in the system prompt.
    It should contains very interesting axes to dig in the subject in 3 PARTS
    the schema is as following :
    {
        'plan': [
            {
                'title':'part1 title',
                'description':'part1 description'
            },
            {
                'title':'part2 title',
                'description':'part2 description'
            },
            ...
        ]
    }

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
        },
        {
            "title": "Meta's AI Dilemma",
            "description": "Investigate Mark Zuckerberg's Meta reorganization around AI, the development of Galactica, and internal debates about open-sourcing AI technology, with expert insights into the ethical considerations and potential consequences."
        }
    ]
}
"""
