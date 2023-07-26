from PIL import Image, ImageDraw
import random
import hashlib

def generate_avatar(username, size=200):
    # Create a unique pattern based on the user's input (username)
    seed = hashlib.md5(username.encode()).hexdigest()
    random.seed(seed)

    # Generate random colors for the background and foreground
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    fg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Create a blank image with a specified size
    avatar = Image.new('RGB', (size, size), bg_color)

    # Draw a pattern on the image using random shapes
    draw = ImageDraw.Draw(avatar)
    for _ in range(100):
        x0 = random.randint(0, size)
        y0 = random.randint(0, size)
        x1 = random.randint(0, size)
        y1 = random.randint(0, size)
        draw.line((x0, y0, x1, y1), fill=fg_color, width=3)

    return avatar

if __name__ == "__main__":
    username = input("Enter your username: ")
    avatar = generate_avatar(username)
    avatar.show()
    avatar.save(f"{username}_avatar.png")
