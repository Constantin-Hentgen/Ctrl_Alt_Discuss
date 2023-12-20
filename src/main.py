# local import
from pipeline import pipeline

if __name__ == "__main__":
    pipeline(
        topic="The WannaCry ransomware attack was a worldwide cyberattack in May 2017 by the WannaCry ransomware cryptoworm",
        article_url="https://www.malwarebytes.com/wannacry",
        reference="source : malwarebytes.com | The WannaCry ransomware attack was a worldwide cyberattack in May 2017 by the WannaCry ransomware cryptoworm",
        with_thumbnail=False,
        with_audio=True,
    )
