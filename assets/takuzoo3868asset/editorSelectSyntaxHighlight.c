void editorSelectSyntaxHighlight(char *filename) {
  for (unsigned int j = 0; j < HLDB_ENTRIES; j++) {
    struct editorSyntax *s = HLDB + j;
    unsigned int i = 0;
    while (s->filematch[i]) {
      char *p;
      int patlen = strlen(s->filematch[i]);
      if ((p = strstr(filename, s->filematch[i])) != NULL) {
        if (s->filematch[i][0] != '.' || p[patlen] == '\0') {
          E.syntax = s;
          return;
        }
      }
      i++;
    }
  }
}
