from .init_pygame import *
from .draw_text import draw_text

def menu():
    draw_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit", FONT, WHITE, 200, 540)
    draw_text("Duis ultricies molestie metus, feugiat placerat odio tincidunt id. Sed facilisis lorem quis diam hendrerit,", FONT, WHITE, 200, 580)
    draw_text("sit amet pharetra tortor ornare. Vivamus varius accumsan eleifend. Morbi auctor tincidunt sagittis. Integer viverra magna ut efficitur auctor. Maecenas vitae lorem nisi.", FONT, WHITE, 200, 620)
    draw_text("Integer in odio a elit tincidunt efficitur. In in diam sed arcu vestibulum convallis. \nEtiam bibendum est ut augue porta ultrices. Donec sit amet augue ut velit rhoncus cursus id eget metus.", FONT, WHITE, 200, 660)