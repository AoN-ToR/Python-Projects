import curses
from curses import wrapper
import time
import random


def intro_screen(stdscr):
	stdscr.clear()
	stdscr.addstr("Welcome to the Speed Typing Test!")
	stdscr.addstr("\nPress any key to begin!")
	stdscr.refresh()
	stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target)
	stdscr.addstr(1, 0, "WPM: %d" %wpm)

	# for each letter in the input of the user
	for i, char in enumerate(current):
		# see the expected text and color it green (correct)
		correct_char = target[i]
		color = curses.color_pair(1)
		# if the user input != expected text, then color the currently checked char red
		if char != correct_char:
			color = curses.color_pair(2)
		# print the users current char, with it's attributed color, on top of the target text
		stdscr.addstr(0, i, char, color)

def load_text():
	with open("text.txt", "r") as file:
		lines = file.readlines()
		# read one line of 'lines', choose which one at random
		return random.choice(lines).strip()

def wpm_test(stdscr):
	target_text = load_text()
	current_text = []
	wpm = 0
	time_start = time.time()
	stdscr.nodelay(True)

	while True:
		time_elapsed = max(time.time() - time_start, 1)
		# wpm = number of char / time in seconds / seconds in a minute / average word lengh
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

		stdscr.clear()
		display_text(stdscr, target_text, current_text, wpm)
		stdscr.refresh()

		if "".join(current_text) == target_text:
			stdscr.nodelay(False)
			break

		try:
			key = stdscr.getkey()
		except:
			continue

		# quit the program whenever the esc key is pressed.
		if ord(key) == 27:
			quit()

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)


def main(stdscr):

	# initialises the ids (here 1, 2, 3) and how they modify printed text color -> curses.init_pair(id, text color, background color)
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	intro_screen(stdscr)
	while True:
		wpm_test(stdscr)
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()
		
		# quit the program whenever the esc key is pressed.
		if ord(key) == 27:
			quit()

wrapper(main)
