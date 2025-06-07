import time

def countdown(t:int) -> None :
    """
    Counts down from 't' seconds, displaying the time in HH:MM:SS or MM:SS format.
    """
    print("Countdown starting...")
    while t >= 0:
        # Calculate minutes and seconds
        # divmod(t, 60) returns a tuple (quotient, remainder)
        # For example, divmod(125, 60) returns (2, 5) meaning 2 minutes and 5 seconds
        minutes, seconds = divmod(t, 60)
        
        # If the total time is over an hour, display hours as well
        if minutes >= 60:
            hours, minutes = divmod(minutes, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        else:
            timer = '{:02d}:{:02d}'.format(minutes, seconds)
        
        # print(timer, end="\r")
        # The `end="\r"` carriage return character moves the cursor to the beginning
        # of the current line, overwriting the previous output.
        # This creates the effect of a ticking clock on a single line.
        print(timer, end="\r")
        
        time.sleep(1) # Pause for 1 second
        t -= 1        # Decrement the time by 1 second

    print("\nTime's up! Countdown complete!")

def countdown_app():
    print("Welcome to the Countdown Timer!")
    
    while True:
        try:
            total_seconds_str = input("Enter the time to countdown from in seconds: ")
            total_seconds = int(total_seconds_str)
            
            if total_seconds < 0:
                print("Please enter a non-negative number of seconds.")
                continue
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    countdown(total_seconds)

if __name__ == "__main__":
    countdown_app()