import personas.michael, personas.daniel
from configuration import HOST_NAME, GUEST_NAME

PERSONAS = f"""
    Here is the personas of {HOST_NAME} and {GUEST_NAME} :\n
    {personas.daniel.DANIEL_PERSONA}\n
    {personas.michael.MICHAEL_PERSONA}
"""
