from configuration import SUBJECT

SYSTEM_PROMPT = (
    f"""
    In the context of a podcast IT you generate metadata.
    Output a JSON object which contains the plan of the article.
    You have to make it a story telling line.
    The subject of the podcast is {SUBJECT}, every part description should contain the subject.
    """
    + """
    Here’s an example about a subject like "Firewall" (just replace some stuff with the subject):
    Replace "firewall" by whatever technical mean was involved (could be edr, social engineering, ids, ips...)

    {
        "plan": [
            {
                "title": "What is a firewall ?",
                "description": "Explain really simply what is a firewall to someone which is not familiar to informatics."
            },
            {
                "title": "When and how was it invented ?",
                "description": "give context : dates, names, first famous firewall"
            },
            {
                "title": "How does it work technically",
                "description": "explaining the different mechanisms involved."
            },
            {
                "title": "What are the last evolution of it, what should we expect for the future",
                "description": "what are the big names of firewalls today, is it about to change ? if yes how and what direction is it taking?"
            }
        ]
    }
"""
)
