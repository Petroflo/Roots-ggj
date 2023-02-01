Colors = [
    {"name": "black", "value": (0, 0, 0)},
    {"name": "white", "value": (255, 255, 255)},
    {"name": "red", "value": (255, 0, 0)},
    {"name": "green", "value": (0, 255, 0)},
    {"name": "blue", "value": (0, 0, 255)}
]

def get_colors(color) -> tuple:
    for c in Colors:
        if c["name"] == color:
            return c["value"]