from rss_aggregator import build_prompt, get_random_rss_source, fetch_article_content

RSS_LIST = [
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
]
OUTPUT_PATH = r"C:\Users\Constantin\Desktop\ByteBeacon\output"
ROOT_PATH = r"C:\Users\Constantin\Desktop\ByteBeacon"
GPT_MODEL = "gpt-3.5-turbo-1106"
STABLE_DIFFUSION_MODEL = "dall-e-3"

# rss_source_url = get_random_rss_source(list_rss_feed_urls=RSS_LIST)
# article = build_prompt(rss_source_url=rss_source_url)

custom_article_url = "https://www.nationalgeographic.com/history/history-magazine/article/roman-emperor-believed-god-assassinated"
article = fetch_article_content(custom_article_url)

# specialization subject : History
PREPROMPT = (
    """
        You’re a podcast script writer specialized in History and you write specific part of the podcast on demand.
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


PREPROMPT_METADATA = """
    Here is the structure of the JSON object you have to output.
    {
        'title': <an appealing (and short) but clear title>,
        'description': <a cool description of 3/4 sentences teasing the different point of the podcast>,
        'thumbnail_prompt": <a prompt to generate a talking, pictorial miniature for listeners to grasp the theme>,
        'folder_name':<a simple name based on the podcast title which is suitable for Windows and Linux system in Pascal_Case>,
    }

    here is the source you have to base yourself to build this object :
 """

PROMPT_PLAN = """
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


PROMPT_INTRODUCTION = """
    You’re allowed to mention speakers names

    - welcoming of the auditors\n
    - Quick introduction of Emily the host and introduce the expert Michael'\n
    - announcement of the article by quoting it (title, author, source) which is the WHOLE reason of the podcast\n
    - announce the plan which is the following :
"""

PROMPT_DEVELOPMENT = """
    You’re not allowed to mention the speakers names but in the JSON Object just write Emily instead of Host and Michael instead of Guest.
    The Host should introduce the part of the plan which is gonna be touched upon.
    The Host should barely talk, just asking the expert and let him speak.
    There should be at least 10 items in the script list (to cover the subject properly).
    in the line attribute never use the word 'Emily' or 'Michael'
    The host question should be transitioning from the last answer of the guest.

    the schema is as following :
    {
        'chapter_title': <name of the part of the plan>,
        'chapter_description': <description of the part of the plan,
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
    }
"""

PROMPT_CONCLUSION = """
    Conclusion:

    The host Emily ask the expert on what should we remember after this podcast,
    what are the key debates that can comes from this subject
    Then the host conclude and thanks the auditors for listening + close the podcast with a catchy sentence to end on a happy note.
"""
