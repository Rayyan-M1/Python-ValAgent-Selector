from graphics import *
import random
import time

def main():
    # 1. Setup the Window
    win = GraphWin("VALORANT Agent Roulette", 400, 300)
    win.setBackground("#0f1923") # Valorant Dark Blue/Black

    # 2. Define the Agent List (Current for 2026)
    agents = [
        "Astra", "Breach", "Brimstone", "Chamber", "Clove", "Cypher", 
        "Deadlock", "Fade", "Gekko", "Harbor", "Iso", "Jett", "KAY/O", 
        "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", 
        "Skye", "Sova", "Tejo", "Veto", "Viper", "Vyse", "Waylay", "Yoru"
    ]

    # 3. Create UI Elements
    title = Text(Point(200, 50), "AGENT SELECTION")
    title.setFace("arial")
    title.setSize(12)
    title.setTextColor("#ece8e1")
    title.draw(win)

    display_text = Text(Point(200, 150), "CLICK TO ROLL")
    display_text.setFace("courier") # Clean, monospaced look
    display_text.setSize(28)
    display_text.setStyle("bold")
    display_text.setTextColor("#ff4655") # Valorant Red
    display_text.draw(win)

    instruction = Text(Point(200, 250), "Click window to start...")
    instruction.setSize(10)
    instruction.setTextColor("gray")
    instruction.draw(win)

    while True:
        # Wait for user click to start the roll
        win.getMouse()
        
        instruction.setText("Rolling...")
        display_text.setTextColor("#ece8e1") # Change to white during roll
        
        # 4. The Roulette Animation
        # We start with a fast flicker and gradually increase the sleep time
        current_delay = 1.02
        for i in range(40):
            selected = random.choice(agents)
            display_text.setText(selected.upper())
            
            # Gradually slow down the animation
            if i > 25:
                current_delay += 0.02
            
            time.sleep(current_delay)
            update() # Force graphics.py to refresh the window

        # 5. The Final Choice
        final_agent = random.choice(agents)
        display_text.setText(final_agent.upper())
        display_text.setTextColor("#ff4655") # Final highlight in Red
        instruction.setText("Click to roll again!")
        
        # Flash effect for the final pick
        for _ in range(3):
            display_text.undraw()
            time.sleep(0.1)
            display_text.draw(win)
            time.sleep(0.1)

if __name__ == "__main__":
    main()
