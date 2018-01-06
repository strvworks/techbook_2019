void initEditor() {
  E.cx = 0;
  E.cy = 0;
  E.rx = 0;
  E.rowoff = 0;
  E.coloff = 0;
  E.numrows = 0;
  E.row = NULL;
  E.dirty = 0;
  E.filename = NULL;
  E.statusmsg[0] = '\0';
  E.statusmsg_time = 0;
  E.syntax = NULL;

  if (getWindowSize(STDIN_FILENO, STDOUT_FILENO, &E.screenrows, &E.screencols) == -1) {
    perror("Unable to query the screen for size (columns / rows)");
    exit(1);
  }
  E.screenrows -= 2;
}
