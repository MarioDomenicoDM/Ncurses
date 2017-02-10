import curses


#inizializza e memorizza un riferimento allo standard screen
stdscr = curses.initscr()

# spegne il cursore 

curses.curs_set(0)

#stampa

stdscr.addstr(3, 20, "X X X X X X X X X X X X X X X X")
#linea a sinistra
stdscr.addstr(4, 20, "X")
stdscr.addstr(5, 20, "X")
stdscr.addstr(6, 20, "X")
stdscr.addstr(7, 20, "X")
stdscr.addstr(8, 20, "X")
stdscr.addstr(9, 20, "X")
stdscr.addstr(10, 20, "X")
stdscr.addstr(11, 20, "X")
stdscr.addstr(12, 20, "X")
stdscr.addstr(13, 20, "X")
stdscr.addstr(14, 20, "X")
stdscr.addstr(15, 20, "X")
stdscr.addstr(16, 20, "X")
stdscr.addstr(17, 20, "X")
stdscr.addstr(18, 20, "X")
stdscr.addstr(19, 20, "X")
#sinistra
stdscr.addstr(4, 50, "X")
stdscr.addstr(5, 50, "X")
stdscr.addstr(6, 50, "X")
stdscr.addstr(7, 50, "X")
stdscr.addstr(8, 50, "X")
stdscr.addstr(9, 50, "X")
stdscr.addstr(10, 50, "X")
stdscr.addstr(11, 50, "X")
stdscr.addstr(12, 50, "X")
stdscr.addstr(13, 50, "X")
stdscr.addstr(14, 50, "X")
stdscr.addstr(15, 50, "X")
stdscr.addstr(16, 50, "X")
stdscr.addstr(17, 50, "X")
stdscr.addstr(18, 50, "X")
stdscr.addstr(19, 50, "X")

#linea sotto 

stdscr.addstr(20, 20, "X X X X X X X X X X X X X X X X")
#faccina
#occhio sinistra
stdscr.addstr(8, 25, "XXXX")
stdscr.addstr(9, 25, "XXXX")
stdscr.addstr(10, 25, "XXXX")
stdscr.addstr(11, 25, "XXXX")
#occhio destra 

stdscr.addstr(8, 42, "XXXX")
stdscr.addstr(9, 42, "XXXX")
stdscr.addstr(10, 42, "XXXX")
stdscr.addstr(11, 42, "XXXX")

#bocca

stdscr.addstr(16, 25, "XXXXXXXXXXXXXXXXXXXXX")
stdscr.addstr(17, 25, "XXXXXXXXXXXXXXXXXXXXX")



stdscr.getch()

curses.endwin()
