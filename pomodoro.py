import time
import sys

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f'Time left: {mins:02}:{secs:02}'
        print(time_format, end='\r')
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    print(' ' * 20, end="\r")

def pomodoro_timer(work_duration=50*60, break_duration=10*60):
    total_sessions = 0
    
    while True:
        total_sessions += 1
        print(f"\nWork session #{total_sessions} started. Sometimes i like to dream about my future")
        countdown(work_duration)
        
        print("\nTime's up! Take a 10-minute break.")
        countdown(break_duration)  
        
        print(f"\nBreak over! Starting a new work session...\n")

pomodoro_timer()
