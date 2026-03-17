import os

# 定义词库：App名, 输入提示, 转换按钮, 美元标签, 日元标签, 欧元标签
TRANSLATIONS = {
    "values": ["Million Currency", "Enter CNY", "Convert", "USD: ", "JPY: ", "EUR: "],
    "values-zh-rCN": ["百万汇率", "输入人民币", "立即转换", "美元：", "日元：", "欧元："],
    "values-ja": ["ミリオン為替", "人民元を入力", "換算", "米ドル：", "円：", "ユーロ："]
}

KEYS = ["app_name", "hint_cny", "btn_convert", "res_usd", "res_jpy", "res_eur"]
BASE_PATH = "app/src/main/res"

def generate():
    for folder, values in TRANSLATIONS.items():
        target_dir = os.path.join(BASE_PATH, folder)
        os.makedirs(target_dir, exist_ok=True)
        content = '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n'
        for i in range(len(KEYS)):
            content += f'    <string name="{KEYS[i]}">{values[i]}</string>\n'
        content += '</resources>'
        with open(os.path.join(target_dir, "strings.xml"), "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    generate()
