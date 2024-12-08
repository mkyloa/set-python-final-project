import sys
from modules.weather import main as weather_main
from modules.ascii import main as ascii_main
from modules.cowsay import main as cowsay


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python useless_tool.py <weather|ascii> [image_path]")
        sys.exit(1)

    tool = sys.argv[1]

    if tool == "weather":
        weather_main()

    elif tool == "ascii" and len(sys.argv) == 3:
        image_path = sys.argv[2]
        ascii_main(image_path)

    elif tool == "cowsay" and len(sys.argv) == 3:
        message = sys.argv[2]
        cowsay(message)
        
    else:
        print("Invalid usage. For weather: python useless_tool.py weather")
        print("For ASCII: python useless_tool.py ascii <image_path>")
        print("For cowsay: python useless_tool.py cowsay <message>")