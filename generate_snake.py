# generate_snake.py

import datetime

def generate_snake():
    today = datetime.date.today()
    svg_content = f'<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="black" /><text x="10" y="50" font-family="Verdana" font-size="35" fill="white">{today}</text></svg>'
    return svg_content

if __name__ == "__main__":
    svg_content = generate_snake()
    with open('github-contribution-grid-snake.svg', 'w') as f:
        f.write(svg_content)
