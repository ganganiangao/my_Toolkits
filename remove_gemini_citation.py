import re
import sys

def remove_citations(text):
    text = re.sub(r'\[cite_start\]|\[cite:\s*[\d,\s]+\]', '', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    return text.strip()

print("請貼上內容，輸入完成後")
print("(Mac/Linux) 按 Ctrl+D \n(Windows) 按 Ctrl+Z ：\n")
print("====== 原本輸入 ======")

# 讀取整個標準輸入
input_text = sys.stdin.read()

cleaned_text = remove_citations(input_text)

print("\n====== 清理後結果 ======\n")
print(cleaned_text)
