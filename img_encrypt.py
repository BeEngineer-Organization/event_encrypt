from PIL import Image
import random

def scramble_image(input_img_path, output_img_path, key, decrypt=False):
    img = Image.open(input_img_path)
    img = img.convert("RGB")
    width, height = img.size
    
    # 全ピクセルの座標リストを作成 [(0,0), (1,0), ..., (w-1, h-1)]
    coordinates = [(x, y) for y in range(height) for x in range(width)]
    
    # 鍵（パスワード）を元に乱数の「種」を固定する
    # これにより、同じ鍵なら毎回同じシャッフル結果になる
    random.seed(key)
    
    # シャッフルされた座標リストを作成
    shuffled_coordinates = coordinates[:] # コピーを作成
    random.shuffle(shuffled_coordinates)
    
    # 新しい画像を作成
    new_img = Image.new("RGB", (width, height))
    
    # 元の画像のピクセルを取得
    original_pixels = img.load()
    new_pixels = new_img.load()
    
    total_pixels = width * height
    
    if decrypt:
        # 【復号モード】: ぐちゃぐちゃの座標から元の座標に戻す
        # shuffled の位置にあるピクセルを、元の coordinates の位置に戻す
        for i in range(total_pixels):
            orig_x, orig_y = coordinates[i]      # 本来あるべき場所
            shuf_x, shuf_y = shuffled_coordinates[i] # 今ある場所（暗号画像上の位置）
            
            # 暗号画像の色を取得して、正しい位置に置く
            new_pixels[orig_x, orig_y] = original_pixels[shuf_x, shuf_y]
    else:
        # 【暗号化モード】: 元の座標からぐちゃぐちゃの座標へ移動
        for i in range(total_pixels):
            orig_x, orig_y = coordinates[i]      # 元の画像の場所
            shuf_x, shuf_y = shuffled_coordinates[i] # 移動先の場所
            
            # 元の画像の色を取得して、シャッフル位置に置く
            new_pixels[shuf_x, shuf_y] = original_pixels[orig_x, orig_y]

    new_img.save(output_img_path)
    print(f"処理完了: {output_img_path}")

# --- 実行部分 ---
key = 2025 # これが鍵になります

# 暗号化
scramble_image("kyoto-university.jpg", "scrambled.png", key, decrypt=False)

# 復号
input("復号します...")
scramble_image("scrambled.png", "restored.png", key, decrypt=True)