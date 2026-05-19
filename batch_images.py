import os
import argparse
from PIL import Image

PLATFORM_SIZES = {
    "taobao_main": (800, 800),
    "taobao_detail": (750, 9999),
    "pdd_main": (750, 750),
    "douyin_main": (800, 800),
    "xiaohongshu": (1080, 1440),
}

def batch_resize(input_folder, width, height, output_folder=None):
    if output_folder is None:
        output_folder = os.path.join(input_folder, "resized")
    os.makedirs(output_folder, exist_ok=True)

    count = 0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            filepath = os.path.join(input_folder, filename)
            try:
                img = Image.open(filepath)
                img_resized = img.resize((width, height), Image.LANCZOS)
                save_path = os.path.join(output_folder, filename)
                img_resized.save(save_path)
                count += 1
                print(f"已处理: {filename}")
            except Exception as e:
                print(f"跳过 {filename}: {e}")

    print(f"\n完成! 共处理 {count} 张图片")
    print(f"保存位置: {output_folder}")

def batch_convert(input_folder, target_format, output_folder=None):
    if output_folder is None:
        output_folder = os.path.join(input_folder, "converted")
    os.makedirs(output_folder, exist_ok=True)

    count = 0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            filepath = os.path.join(input_folder, filename)
            try:
                img = Image.open(filepath)
                if img.mode == 'RGBA' and target_format.lower() in ('jpg', 'jpeg'):
                    img = img.convert('RGB')
                new_name = os.path.splitext(filename)[0] + '.' + target_format
                save_path = os.path.join(output_folder, new_name)
                img.save(save_path)
                count += 1
                print(f"已转换: {filename} -> {new_name}")
            except Exception as e:
                print(f"跳过 {filename}: {e}")

    print(f"\n完成! 共转换 {count} 张图片")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="批量图片处理工具")
    parser.add_argument("input", help="输入文件夹路径")
    parser.add_argument("--action", choices=["resize", "convert"], default="resize")
    parser.add_argument("--width", type=int, default=800, help="目标宽度")
    parser.add_argument("--height", type=int, default=800, help="目标高度")
    parser.add_argument("--format", default="png", help="目标格式")
    parser.add_argument("--platform", choices=list(PLATFORM_SIZES.keys()), help="电商平台尺寸")
    parser.add_argument("--output", help="输出文件夹路径")

    args = parser.parse_args()

    if args.platform:
        args.width, args.height = PLATFORM_SIZES[args.platform]

    if args.action == "resize":
        batch_resize(args.input, args.width, args.height, args.output)
    elif args.action == "convert":
        batch_convert(args.input, args.format, args.output)
