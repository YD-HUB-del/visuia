import cv2
import time
import pyautogui

def click_by_image(
    image_path: str,
    ga,
    threshold: float = 0.8,
    wait_before: float = 2.0,
    click_type: str = "single"
):
    """
    通过模板图片点击 GUI 元素（安全版）

    click_type:
        - "single": 单击
        - "double": 系统级双击
    """

    time.sleep(wait_before)

    template = cv2.imread(image_path)
    if template is None:
        raise RuntimeError(f"❌ 模板图片读取失败: {image_path}")

    # ⭐ 关键 1：清空旧 spot，防止误点
    ga.spot = None

    ga.detect(template, threshold)

    # ⭐ 关键 2：严格判断是否真的找到
    if ga.spot is None:
        raise RuntimeError(f"❌ 未找到界面元素: {image_path}")

    # 获取当前 spot 中心坐标
    x, y = ga.spot.center()

    # ⭐ 关键 3：使用 OS 级鼠标事件
    if click_type == "single":
        pyautogui.click(x, y)
        action = "单击"

    elif click_type == "double":
        pyautogui.doubleClick(x, y)
        action = "双击"

    else:
        raise ValueError(f"❌ 不支持的 click_type: {click_type}")

    print(f"✅ 已{action}: {image_path}")

