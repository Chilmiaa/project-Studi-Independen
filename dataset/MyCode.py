# -*- coding: utf-8 -*-
"""MyCode

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jO3noSW5LxdJY-bIXD6zqDjE0JF5_omN
"""

import os
from gtts import gTTS
from audioplayer import AudioPlayer

congrats = 'Selamat, Anda telah berhasil mengelola sebuah enveronment!'
language = 'id'
file_name = 'congratulations.mp3'

tts = gTTS(teks=congrats, lang=language)
tts.save(file_name)
AudioPlayer(file_name).play(block=True)
print(congrats)