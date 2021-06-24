import pyaudio       # pip install pyaudio
import wave          # pip install Wave
import datetime
import keyboard      # pip install keyboard



print("press 'ctrl+shift+s' to start")
print("press 'ctrl+shift+q' to stop")


if keyboard.is_pressed('ctrl')==True and keyboard.is_pressed('shift')==True and keyboard.is_pressed('s')==True:
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %I-%M-%S')
    filename = f"enter your save location\{time_stamp}.wav"



    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True
                    )

    frames = []  # Initialize array to store frames

    print(datetime.datetime.now().strftime('%Y-%m-%d %I-%M-%S'))
    while True:
        data = stream.read(chunk)
        frames.append(data)
        # press 'ctrl+shift+q' to stop
        if keyboard.is_pressed('ctrl')==True and keyboard.is_pressed('shift')==True and keyboard.is_pressed('q')==True:
            print(datetime.datetime.now().strftime('%Y-%m-%d %I-%M-%S'))
            break
        
    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()