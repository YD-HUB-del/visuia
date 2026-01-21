import cv2
from gui_automation import GuiAuto
import time
import pyautogui
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
import numpy as np


def detect_once(template, threshold=0.8):
    """
    基于当前屏幕截图，判断模板是否存在（无缓存、无状态）

    Parameters
    ----------
    template : np.ndarray
        OpenCV 读取的模板图像
    threshold : float
        匹配阈值

    Returns
    -------
    bool
        当前屏幕是否检测到模板
    """
    # 1️⃣ 截屏
    screenshot = pyautogui.screenshot()

    # 2️⃣ PIL -> OpenCV
    screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 3️⃣ 模板匹配
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

    # 4️⃣ 判断最大相似度
    max_val = res.max()

    return max_val >= threshold



def wait_for_compute_done_cv(
    computing_image: str,
    threshold: float = 0.8,
    timeout: float = 600,
    check_interval: float = 1.0,
    confirm_miss: int = 3
):
    """
    使用 OpenCV + 截屏判断 COMSOL 计算完成（进度条消失）

    Parameters
    ----------
    computing_image : str
        计算中进度条模板路径
    threshold : float
        模板匹配阈值
    timeout : float
        最大等待时间（秒）
    check_interval : float
        检测间隔（秒）
    confirm_miss : int
        连续 miss 次数，确认消失

    Raises
    ------
    TimeoutError
        超时仍未完成
    """
    template = cv2.imread(computing_image)
    if template is None:
        raise RuntimeError(f"❌ 进度条模板读取失败: {computing_image}")

    start = time.time()
    miss_count = 0

    print("⏳ 等待计算完成...")

    while True:
        found = detect_once(template, threshold)

        if found:
            miss_count = 0
            print("🔄 仍在计算中...")
        else:
            miss_count += 1
            print(f"🔍 未检测到进度条 ({miss_count}/{confirm_miss})")

        if miss_count >= confirm_miss:
            print("✅ 计算完成（进度条消失）")
            break

        if time.time() - start > timeout:
            raise TimeoutError("❌ 等待计算完成超时")

        time.sleep(check_interval)
