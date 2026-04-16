import sys

# sys.argv is a list of everything you typed after 'python'
args = sys.argv[1:] 

if not args:
    print("Usage: python blackbull.py [greet | status | info]")
    sys.exit()

command = args[0].lower()

if command == "greet":
    name = args[1] if len(args) > 1 else "Agent"
    print(f"Welcome back, {name}. BlackBull systems are standing by.")

elif command == "status":
    print("--- SYSTEM CHECK ---")
    print("Database: Secure\nNetwork: Encrypted\nUptime: 100%")

elif command == "info":
    print("BlackBull v1.0 - Built for mobile engineering.")

else:
    print(f"Unknown command: '{command}'. Try 'greet' or 'status'.")
