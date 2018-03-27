int main(int argc, char **argv) {
    // takdit <ファイル名> という引数のみ実行
    if (argc != 2) {
        fprintf(stderr, "Usage: takdit <filename>\n");
        exit(1);
    }

    initEditor();                         // エディタの初期化
    editorSelectSyntaxHighlight(argv[1]); // シンタックスハイライトの適用
    editorOpen(argv[1]);                  // ファイルを開く
    enableRawMode(STDIN_FILENO);          // Rawモードの有効化
    editorSetStatusMessage(
            "HELP: Ctrl-S = save | Ctrl-Q = quit | Ctrl-F = find");
    while (1) {
        editorRefreshScreen();                // 変更の反映
        editorProcessKeypress(STDIN_FILENO);  // キー入力待ち
    }
    return 0;
}