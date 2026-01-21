import cv2
import time
import pyautogui
import numpy as np


def commit_input_robust(
    offset_patterns=None,
    use_enter=True,
    final_refocus=False
):
    """
    通过多次近邻点击，确保 COMSOL 接收输入
    """

    if offset_patterns is None:
        # ⭐ 一组“安全”的近邻点（经验值）
        offset_patterns = [
            (40, 40),    # 下
        ]

    # 1️⃣ 多点失焦点击
    for dx, dy in offset_patterns:
        pyautogui.moveRel(dx, dy)
        pyautogui.click()
        time.sleep(0.05)

    # 2️⃣ 可选 Enter（作为补充，不是唯一）
    if use_enter:
        pyautogui.press("enter")
        time.sleep(0.1)

    # 3️⃣ 可选：再点回输入区，避免 UI 锁死
    if final_refocus:
        pyautogui.moveRel(-offset_patterns[0][0], 0)
        pyautogui.click()






def set_input_by_image(
    image_path: str,
    ga,
    text: str,
    offset_x: int = 0,
    offset_y: int = 0,
    threshold: float = 0.8,
    wait_after: float = 0.2,
    click_mode: str = "double",   
):
    """
    通过模板图片定位输入框，并输入指定内容

    click_mode:
        - "single": 单击进入编辑态（默认，推荐）
        - "double": 双击进入编辑态
    """

    # 1️⃣ 读取模板
    template = cv2.imread(image_path)
    if template is None:
        raise RuntimeError(f"❌ 模板图片读取失败: {image_path}")

    # 2️⃣ 模板匹配
    if not ga.detect(template, threshold):
        raise RuntimeError(f"❌ 未找到输入框模板: {image_path}")

    # 3️⃣ 定位到模板中心
    ga.click()
    time.sleep(0.05)

    # 4️⃣ 偏移到真正可编辑区域
    if offset_x != 0 or offset_y != 0:
        pyautogui.moveRel(offset_x, offset_y)
        time.sleep(0.02)

    # 5️⃣ 进入编辑态
    if click_mode == "single":
        # 单击即可编辑（什么都不做，已经点中了）
        pass

    elif click_mode == "double":
        pyautogui.doubleClick()
        time.sleep(wait_after)

    else:
        raise ValueError(f"❌ 不支持的 click_mode: {click_mode}")

    # 6️⃣ 输入内容
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.05)
    pyautogui.write(text, interval=0.02)

   # ⭐ 用鲁棒提交
    commit_input_robust(use_enter=True)

    print(f"✅ [{click_mode}] 已通过 {image_path} 设置输入为: {text}")