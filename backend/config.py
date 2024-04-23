from diart import PipelineConfig
from enum import Enum

TRANSCRIPTION_DEVICE = "cpu"  # use 'cpu' if it doesn't work
COMPUTE_TYPE = "float32"#"int8_float16"  # use float32 with cpu

SLIDING_WINDOW_LENGTH = 5
PROBABILITY_THRESHOLD = 0.5  # Diart will recognize a speaker if the probability of them speaking is higher than this
MINIMUM_SPEECH_IMPROVEMENT_LENGTH = 0.1  # Diart will self-improve its speaker recognition for a speaker if the speaker speaks for longer than this
NEW_SPEAKER_THRESHOLD = 0.57  # Threshold for new speaker detection, the lower, the more sensitive Diart is to speech differences and will be more likely to generate new speakers
STEP = 0.5

DIARIZATION_PIPELINE_CONFIG = PipelineConfig(
    duration=SLIDING_WINDOW_LENGTH,
    step=STEP,
    latency="min",
    tau_active=PROBABILITY_THRESHOLD,
    rho_update=MINIMUM_SPEECH_IMPROVEMENT_LENGTH,
    delta_new=NEW_SPEAKER_THRESHOLD
)

PARAMETERS = {
    "language",
    "model",
    "transcribeTimeout",
    "beamSize",
    "transcriptionMethod"
}

SPEAKER_MAPPING = {
    -1: "unknown"
}

SPEECH_CONFIDENCE_THRESHOLD = 0.3  # The minimal amount of confidence to determine speech presence in batch (e.g. 0.5 means 50% chance at minimum)

SAMPLE_RATE = 16000

TEMP_FILE_PATH = "temp/batch.wav"  # Path to the temporary file used for batch transcription in SequentialClient


class ClientState(Enum):
    NOT_INITIALIZED = "not_initialized"
    INITIALIZED = "initialized"
    ENDING_STREAM = "ending_stream"
    DISCONNECTED = "disconnected"


class WhisperModelSize(Enum):
    TINY = 'tiny'
    TINY_ENGLISH = 'tiny.en'
    BASE = 'base'
    BASE_ENGLISH = 'base.en'
    SMALL = 'small'
    SMALL_ENGLISH = 'small.en'
    MEDIUM = 'medium'
    MEDIUM_ENGLISH = 'medium.en'
    LARGE_V1 = 'large-v1'
    LARGE_V2 = 'large-v2'


NON_ENGLISH_SPECIFIC_MODELS = [WhisperModelSize.LARGE_V1, WhisperModelSize.LARGE_V2]  # Models that don't have an English-only version

REQUIRED_AUDIO_TYPE = "float32"

# Language code mapping
LANGUAGE_MAPPING = {
    "english": "en",
    "chinese": "zh",
    "german": "de",
    "spanish": "es",
    "russian": "ru",
    "korean": "ko",
    "french": "fr",
    "japanese": "ja",
    "portuguese": "pt",
    "turkish": "tr",
    "polish": "pl",
    "catalan": "ca",
    "dutch": "nl",
    "arabic": "ar",
    "swedish": "sv",
    "italian": "it",
    "indonesian": "id",
    "hindi": "hi",
    "finnish": "fi",
    "vietnamese": "vi",
    "hebrew": "he",
    "ukrainian": "uk",
    "greek": "el",
    "malay": "ms",
    "czech": "cs",
    "romanian": "ro",
    "danish": "da",
    "hungarian": "hu",
    "tamil": "ta",
    "norwegian": "no",
    "thai": "th",
    "urdu": "ur",
    "croatian": "hr",
    "bulgarian": "bg",
    "lithuanian": "lt",
    "latin": "la",
    "maori": "mi",
    "malayalam": "ml",
    "welsh": "cy",
    "slovak": "sk",
    "telugu": "te",
    "persian": "fa",
    "latvian": "lv",
    "bengali": "bn",
    "serbian": "sr",
    "azerbaijani": "az",
    "slovenian": "sl",
    "kannada": "kn",
    "estonian": "et",
    "macedonian": "mk",
    "breton": "br",
    "basque": "eu",
    "icelandic": "is",
    "armenian": "hy",
    "nepali": "ne",
    "mongolian": "mn",
    "bosnian": "bs",
    "kazakh": "kk",
    "albanian": "sq",
    "swahili": "sw",
    "galician": "gl",
    "marathi": "mr",
    "punjabi": "pa",
    "sinhala": "si",
    "khmer": "km",
    "shona": "sn",
    "yoruba": "yo",
    "somali": "so",
    "afrikaans": "af",
    "occitan": "oc",
    "georgian": "ka",
    "belarusian": "be",
    "tajik": "tg",
    "sindhi": "sd",
    "gujarati": "gu",
    "amharic": "am",
    "yiddish": "yi",
    "lao": "lo",
    "uzbek": "uz",
    "faroese": "fo",
    "haitian creole": "ht",
    "pashto": "ps",
    "turkmen": "tk",
    "nynorsk": "nn",
    "maltese": "mt",
    "sanskrit": "sa",
    "luxembourgish": "lb",
    "myanmar": "my",
    "tibetan": "bo",
    "tagalog": "tl",
    "malagasy": "mg",
    "assamese": "as",
    "tatar": "tt",
    "hawaiian": "haw",
    "lingala": "ln",
    "hausa": "ha",
    "bashkir": "ba",
    "javanese": "jv",
    "sundanese": "su",
}
