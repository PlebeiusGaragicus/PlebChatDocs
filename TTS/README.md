https://github.com/matatonic/openedai-speech

https://docs.openwebui.com/tutorials/integrations/openedai-speech-integration/

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
    "voice": "alloy",
    "response_format": "mp3",
    "speed": 1.0
  }' > speech.mp3

  ```

  