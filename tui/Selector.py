import curses


class Selector:
    def __init__(self, stdscr, options):
        curses.curs_set(0)
        selected_option = 0

        while True:
            stdscr.clear()
            for index, option in enumerate(options):
                if index == selected_option:
                    stdscr.addstr(index, 0, option, curses.color_pair(1))
                else:
                    stdscr.addstr(index, 0, option)

            stdscr.refresh()
            key = stdscr.getch()
            if key == curses.KEY_UP:
                selected_option = max(0, selected_option - 1)
            elif key == curses.KEY_DOWN:
                selected_option = min(len(options) - 1, selected_option + 1)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self.selected_item_index = selected_option
                break
