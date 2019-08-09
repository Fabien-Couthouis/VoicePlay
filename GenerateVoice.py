# GenerateVoice.py
# Fabien Couthouis
import re
from ibm_watson import TextToSpeechV1


# Read ibm-credentials
with open('ibm-credentials.env', 'r') as env_file:
    cred_str = env_file.read()
    apikey = re.findall(
        r'TEXT_TO_SPEECH_IAM_APIKEY=(.+)\n', cred_str)[0]
    url = re.findall(r'TEXT_TO_SPEECH_URL=(.+)', cred_str)[0]

T2S = TextToSpeechV1(
    iam_apikey=apikey,
    url=url
)

# Disable SSL verification to avoid any proxy issue
T2S.disable_SSL_verification()


def generate_voice(text, fpath):
    voice = 'fr-FR_ReneeV3Voice'
    with open(fpath, 'wb') as audio_file:
        audio_file.write(
            T2S.synthesize(
                text,
                voice=voice,
                accept='audio/mp3'
            ).get_result().content)
    return
