import time
import datetime
import pygame

def set_alarm(alrm_time):
    print(f"Alarm has been set to {alrm_time}")
    sound_file = "videoplayback.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alrm_time:
            print("WAKE UP SUNSHINE!!!!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play(-1)  # -1 makes it loop

            # Keep the alarm playing until stopped manually
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nAlarm stopped!")
                pygame.mixer.music.stop()
                is_running = False

        time.sleep(1)


if __name__ == '__main__':
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
