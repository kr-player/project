import pygame
import soundfile as sf
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# 음성 파일 경로
file_path = "MJ.wav"

# pygame 초기화
pygame.init()

# 오디오 파일 재생
pygame.mixer.music.load(file_path)
pygame.mixer.music.play()

# 오디오 파일 메타 정보 출력
info = sf.info(file_path)
print("Sample Rate:", info.samplerate)
print("Duration:", info.duration, "seconds")

# 음성 파일 재생이 끝날 때까지 대기
pygame.time.wait(int(info.duration * 1000))  # milliseconds

# 샘플링 속도 변환 (44kHz에서 22kHz로)
y, sr = librosa.load(file_path, sr=22050)

# 음성 파형 그리기
plt.figure(figsize=(10, 5))
librosa.display.waveshow(y, sr=sr)
plt.ylabel("Amplitude")
plt.show()

# Fourier 변환 (STFT)
n_fft = 2048
hop_length = 512
stft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
magnitude = np.abs(stft)

# 프리에 변환
y_fft = np.fft.fft(y)
y_mag = np.abs(y_fft)

# 스펙트로그램 시각화
plt.figure(figsize=(10, 5))
librosa.display.specshow(librosa.amplitude_to_db(magnitude, ref=np.max), y_axis="log", x_axis="time")
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram")
plt.show()

# 프리에 변환 결과 시각화
plt.figure(figsize=(10, 5))
plt.plot(y_mag)
plt.title("Fourier Transform (Frequencies)")
plt.xlabel("Frequency Bins")
plt.ylabel("Magnitude")
plt.show()

# 음성 파일 일부 잘라서 저장
start_time = 30  # 시작 시간 (초)
end_time = 40  # 종료 시간 (초)

# 음성 파일 일부 잘라서 저장
y_cut = y[start_time * sr : end_time * sr]
sf.write("cut_audio.wav", y_cut)
