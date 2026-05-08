import threading
from playsound import playsound
import time


class AudioPlayer(threading.Thread):
    def __init__(self, sound_file):
        threading.Thread.__init__(self)
        self.sound_file = sound_file
        self.playing = True

    def run(self):
        playsound(self.sound_file)
        self.playing = False

    def stop(self):
        self.playing = False


# Пример использования
audio_file = 'alarm.mp3'
player = AudioPlayer(audio_file)

player.start()
print("Играет звук...")

# Дождаться 5 секунд (или любое другое время)
time.sleep(0.01)

# Прекратить разыгрывание
print("Остановка звука...")
player.stop()  # Упомяните stop, если вы хотите явно остановить

player.join()  # Дождаться завершения потока
print("Звук остановлен.")
