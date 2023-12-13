SYSTEM_PROMPT = """
    Here is the structure of the JSON object you have to output.
    {
        'title': <an appealing (and short) but clear title>,
        'description': <a cool description of 3/4 sentences teasing the different point of the podcast>,
        'thumbnail_prompt": <a prompt to generate a talking, pictorial miniature for listeners to grasp the theme>,
        'folder_name':<a simple name based on the podcast title which is suitable for Windows and Linux system in Pascal_Case>,
    }

    here is the source you have to base yourself to build this object :
 """
