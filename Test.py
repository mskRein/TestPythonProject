import tkinter as tk
from tkinter import messagebox

# メインウィンドウを作成
root = tk.Tk()
root.title("テストアプリ")
root.geometry("300x200")  # ウィンドウサイズを設定

# ラベルを追加
label = tk.Label(root, text="こんにちは！")
label.pack(pady=20)

# ボタンを追加
button1 = tk.Button(root, text="クリックしてね！", command=lambda: messagebox.showinfo("メッセージ", "やるじゃん！"))
button1.pack(pady=10)

button2 = tk.Button(root, text="クリックしないでね！", command=lambda: messagebox.showinfo("メッセージ", "しないでって言ったのに！"))
button2.pack(pady=10)

# メインループを開始
root.mainloop()
