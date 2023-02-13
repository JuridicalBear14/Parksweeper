#include <stdio.h>
#include <stdlib.h>
#include <ncurses.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

#define bg 1
#define set 2
#define cursor 3
#define navbar 4
#define flagged 5

// Opens a square
bool open_square(int y, int x, int** board) {

}

// Draw the navigation bar at the top of the screen
void draw_navbar(int LINES, int COLS, int color) {
    // Text to write
    char* conway = "Minesweeper";
    int conway_len = strlen(conway);

    // Change control text based on mode
    char* controls;
    controls =
    "([p]->[q]-quit) ([space]/[enter]-advance game) ([p]-pause)";
    int control_len = strlen(controls);

    // Draw colored line
    attron(COLOR_PAIR(color));
    mvhline(0, 0, ' ', COLS);

    // Draw strings
    mvaddstr(0, 0, conway);
    mvaddstr(0, COLS - control_len - 1, controls);

    attroff(COLOR_PAIR(color));
}

// Generate a board of mines with a given probability
void generate_board(int** board, int count) {
    
}

// Returns whether or not square is within valid bounds
bool isvalid(int y, int x) {
    return ((y > 1) && (y < LINES) && (x > 0) && (x < COLS));
}

// Gets the total value of neighbors of a certain square
int neighbor_count(int y, int x, int** board) {
    int count = (board[y][x])? -1 : 0;   // Total count, -1 to offset for self

    // Loop from just before to just after x
    for (int i = y - 1; i <= y + 1; i++) {
        for (int j = x - 1; j <= x + 1; j++) {
            if (isvalid(i, j) && board[i][j]) {
                count++;
            }
        }
    }

    return count;
}

int main(int argc, char** argv) {
    int count = (LINES * COLS) / 5;   // Default delay of 1

    // Set delay based on command line args
    if (argc == 2) {
        count = atoi(argv[1]);
    }

    // Set up gui stuff
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);
    start_color();

    // Set up color pairs
    init_pair(set, COLOR_BLACK, COLOR_WHITE);
    init_pair(bg, COLOR_BLUE, COLOR_CYAN);
    init_pair(cursor, COLOR_WHITE, COLOR_BLUE);
    init_pair(navbar, COLOR_BLUE, COLOR_BLACK);
    init_pair(flagged, COLOR_BLACK, COLOR_RED);

    // Draw navbar
    draw_navbar(LINES, COLS, navbar);

    // Draw background lines
    attron(COLOR_PAIR(bg));
    for (int i = 1; i < LINES; i++) {
        mvhline(i, 0, ' ', COLS);
    }
    attroff(COLOR_PAIR(bg));

    // Initialize board array
    int** board = (int**) calloc(LINES, sizeof(int*));
    for (int i = 0; i < LINES; i++) {
        board[i] = (int*) calloc(COLS, sizeof(int));
    }

    // Set up starting pos
    int x = COLS / 2;
    int y = LINES / 2;
    move(y, x);

    int ch;

    // Event loop
    while ((ch = getch()) != 'q') {
        switch(ch) {
            case KEY_UP:
                // >1 to account for navbar at top
                y -= (y > 1);   // Equals a bool to decide whether move 1 or 0
                break;
            case KEY_DOWN:
                y += (y < LINES - 1);
                break;
            case KEY_LEFT:
                x -= (x > 0);
                break;
            case KEY_RIGHT:
                x += (x < COLS - 1);
                break;

            case '\n':
            case ' ':
                // Select square
                open_square();
                break;

            default:
                continue;
         }
         move(y, x);
         refresh();
    }

    // Free board
    for (int i = 0; i < LINES; i++) {
        free(board[i]);
    }

    free(board);

    endwin();
    return 0;
}
