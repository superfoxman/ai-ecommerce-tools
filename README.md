# AI 电商视觉工具集

## 项目简介

基于 Python + AI 的电商产品图自动化工具，
用于提升电商视觉素材的制作效率。

## 功能模块

### 1. 图片批处理
- 批量裁剪、缩放
- 格式转换（PNG/JPG/WebP）
- 适配电商平台尺寸

### 2. Prompt 模板库
- 覆盖服装、美妆、食品、3C数码等品类
- 产品场景图、模特图、主图等类型
- 50+ 验证过的高效 Prompt

### 3. AI 出图工作流
- Midjourney 商业图生成
- MiMo API 集成（开发中）
- 自动化后处理管线

## 技术栈

- Python 3.13
- Pillow（图片处理）
- OpenAI API（AI 调用）
- Midjourney（图像生成）
- MiMo API（小米大模型）

## 使用方法

```bash
pip install Pillow openai
python batch_images.py

