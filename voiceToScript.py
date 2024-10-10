from vosk import Model, KaldiRecognizer
import wave
import json
from pydub import AudioSegment


model_path = "voskModel/vosk-model-small-en-us-0.15"

class VoiceToScript:
    def __init__(self, model_path, audio_path):
        self.audio = audio_path
        self.wav_audio = self.convert_mp3_to_wav()
        self.audio_trans = wave.open(self.wav_audio, 'rb')
        self.vosk_model = Model(model_path)
        self.vosk_recognizer = KaldiRecognizer(self.vosk_model, 16000)

    def convert_mp3_to_wav(self):
        audio = AudioSegment.from_mp3(self.audio)
        wav_path = "converted_audio.wav"
        audio.export(wav_path, format="wav")
        return wav_path
    
    def load_audio_data(self):
        with wave.open(self.wav_audio, 'rb') as audio_file:
            return audio_file.readframes(audio_file.getnframes())

    def transcribe(self):
        
        self.vosk_recognizer.AcceptWaveform(self.load_audio_data())
        try:
            result = self.vosk_recognizer.Result()
            if result:
                return result
            else:
                return self.vosk_recognizer.PartialResult()
                
        except Exception as e:
            return "Erreur lors de la reconnaissance vocale Vosk : {0}".format(e)


# Exemple d'utilisation
if __name__ == "__main__":
    audio_path = "audio/test1.mp3"

    try:
        voice_to_script = VoiceToScript(model_path, audio_path)
        transcription_result = voice_to_script.transcribe()
        print("Résultat de la transcription : {}".format(transcription_result).split('"')[3])
    except Exception as e:
        print("Erreur globale : {0}".format(e))