# TTS


## openai-edge-tts

```sh
git clone https://github.com/travisvn/openai-edge-tts.git
cd openai-edge-tts

# nano .env
cp .env.example .env
nano .env

```

## `.env`
```txt
API_KEY=your_api_key_here
PORT=5050

DEFAULT_VOICE=en-US-AndrewNeural
DEFAULT_RESPONSE_FORMAT=mp3
DEFAULT_SPEED=1.2

DEFAULT_LANGUAGE=en-US

REQUIRE_API_KEY=True
```

```sh
docker build -t openai-edge-tts .
```




---

## opendai-speech

# reference

https://github.com/matatonic/openedai-speech

https://docs.openwebui.com/tutorials/integrations/openedai-speech-integration/


# setup

```sh
cd TTS
git clone https://github.com/matatonic/openedai-speech.git
cd openedai-speech
cp sample.env speech.env


docker build -f Dockerfile.min -t ghcr.io/matatonic/openedai-speech-min .

docker compose -f docker-compose.min.yml up -d

# edit TTS settings
# http://host.docker.internal:8000/v1
# pass: anythingyouwant

```


# example usage

```sh
curl http://localhost:8000/v1/audio/speech -H "Content-Type: application/json" -d '{
    "model": "tts-1",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "Justin",
    "response_format": "mp3",
    "speed": 1.0
  }' > speech.mp3

  ```

  