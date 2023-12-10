# local imports
from thumbnail_generator import generate_thumbnail
from content_generator import generate_podcast_content, generate_metadata
from configuration import OUTPUT_PATH
from soundfile_management import generate_audio_file


if __name__ == "__main__":
    podcast_content = generate_podcast_content()

    generate_thumbnail(
        prompt=podcast_content["thumbnail_prompt"],
        folder_name=podcast_content["folder_name"],
    )

    # generate_audio_file(script=podcast_content["script"])

    print("Podcast ready to be uploaded :)")
