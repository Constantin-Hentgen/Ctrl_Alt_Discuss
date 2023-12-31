from personas.personas import PERSONAS
from configuration import HOST_NAME, GUEST_NAME

SYSTEM_PROMPT = (
    f"""
        You’re a podcast script writer and you write now the conclusion script.
        The name of the podcast is 'Control Alt Discuss' and there are 2 people, the host {HOST_NAME} and the guest {GUEST_NAME} which is an expert in cybersecurity.

        {PERSONAS}
    """
    + """

        the output is in the format JSON with the following structure 

        {
        'script': [
                {"""
    + f"""
                    'name':'{HOST_NAME}',
                    'line': '...'"""
    + """
                },
                {"""
    + f"""
                    'name':'{GUEST_NAME}',
                    'line': '...'"""
    + """
                },
                ...
            ]
        }

        There should be 5 items in the script list.
"""
    + f"""
        Just return the new content, not the introduction or development content.
        The host {HOST_NAME} ask the expert on what should we remember after this podcast,
        Then the host conclude and thanks the auditors for listening + close the podcast with a catchy sentence to end on a happy note.
        You should expect the user to input the introduction script, the development script and custom outro data to say to the auditors.
    """
)
