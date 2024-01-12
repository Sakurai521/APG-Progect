pythonに必要なモジュール
インストールに少し時間がかかるかもしれない

pip install firebase-admin
pip install google-cloud-firestore

データベースへの接続
https://gakogako.com/python_firestore/
データの取得
https://firebase.google.com/docs/database/admin/retrieve-data?hl=ja#python

12/10追加
PowerManager.py追加しました
中には以下の関数が入っています

def askLevel(player: bool, wait: float, time: str = "now")-> int
    AIのレベルを決定する関数。
    変数Playerはプレイヤー情報であり、TrueがP1でFalseがP2である。
    変数waitは過去何秒のデータを参照するかである。
    レベルを1~5でintで返すが変更可能。エラーがある場合必ず真ん中のレベルが返される。
    変数timeはUTS時間で'%Y-%m-%d %H:%M:%S'で入力すると時間を指定可能。

なのでDebagの際は第3因数を文字列で"2023-12-10 11:23:00"のように年月日の間をハイフン、半角スペース、時分秒の間にコロンを入れてください。
関数実行時、あればエラーや注意内容とLevelの変更結果が出ます。

JSONPASSが変更がある場合は6行目で変更

FireBaseの参照ファイルは42行目

    docs = db.collection('click_count_debug').get() 

'この中'を適宜変更してください

別ファイルとしてでも同じファイルにコピーしてもいいですが、上記のpipのインストールとコピーの場合は全部の関数のコピーとimportを忘れないようにしてください
