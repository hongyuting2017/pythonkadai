#ユーザーに番号を尋ねます．番号が偶数か奇数かに応じて，適切なメッセージをユーザーに出力 します．
# また，数値が 4 の倍数の場合、別のメッセージを出力．

print("ユーザー番号教えてください。")
x=int(input())
if x%4==0:print("4の倍数です")
elif x%2==0:print("偶数です")
else:print("奇数です")
