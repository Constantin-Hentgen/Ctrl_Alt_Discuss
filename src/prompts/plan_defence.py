SYSTEM_PROMPT = """
    In the context of a podcast IT you generate metadata.
    Output a JSON object which contains the plan of the article.
    You have to make it a story telling line.

    Here’s an example about a subject like "the worm stuxnet" (just replace some stuff with the subject):
    Replace the worm by whatever technical mean was involved (could be virus, social engineering...)

    {
        "plan": [
            {
                "title": "What is a Worm in cybersecurity ?",
                "description": "As introduced as a worm, the goal is to popularize the theory behind so even someone ignorant in cybersecurity understand."
            },
            {
                "title": "And Stuxnet in all that ?",
                "description": "Contextualization of Stuxnet as the application of this theory, with dates, places, people."
            },
            {
                "title": "The technical specifities of stuxnet",
                "description": "Examine OpenAI's motivations for releasing ChatGPT, its unexpected success, and the subsequent influence on strategic decisions across the tech industry, with insights from the expert."
            },
            {
                "title": "Who did it, the authors, the customers, the use of it ?",
                "description": "Investigation about every stakeholders in the attack, giving insights about people, their relations between eachothers."
            },
            {
                "title": "Is it still in use, is it still dangerous ?",
                "description": "We can get from Michael some opinion about the experts in IT security : is it still something to fear nowadays."
            }
        ]
    }
"""
