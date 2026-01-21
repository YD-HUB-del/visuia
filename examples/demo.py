"""
Minimal demo for uivision-agent

This demo shows how to:
1. Activate a running application window
2. Locate UI elements by vision
3. Click buttons
4. Input text into fields
5. Wait for a visual state to disappear
"""

from gui_automation import GuiAuto

from uivision_agent import (
    activate_app,
    click_by_image,
    set_input_by_image,
    wait_for_compute_done_cv,
)
from pathlib import Path
import time


# ===============================
# Configuration
# ===============================

APP_NAME = "COMSOL"         # window title keyword
BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / "templates"
out_dir =r"G:\TEST\001"
# ===============================
# Demo workflow
# ===============================

def main():
    
    # 打开参数表
    ga = GuiAuto()
    click_by_image(TEMPLATE_DIR/"canshu.png", ga)
    click_by_image(TEMPLATE_DIR/"dakaicanshuwenjian.png", ga)

    set_input_by_image(
        TEMPLATE_DIR/"canshulujing.png",
        ga,
        text=out_dir,
        click_mode="single",
        
    )

    set_input_by_image(
        TEMPLATE_DIR/"wenjianming.png",
        ga,
        text="canshu",
        offset_x=50
    )

    click_by_image(TEMPLATE_DIR/"dakai.png", ga, click_type="double")
    click_by_image(TEMPLATE_DIR/"fugai.png", ga)

    

    # 设置边界条件
    click_by_image(TEMPLATE_DIR/"jiasudu.png", ga)
    
    # 等待建模完成
    time.sleep(20)  # 前 20 秒必算
    wait_for_compute_done_cv(
        computing_image=TEMPLATE_DIR/"computing.png",
        threshold=0.8,
        timeout=600,
        check_interval=2.0,
        confirm_miss=3
    )
    
    set_input_by_image(
        TEMPLATE_DIR/"af_input.png",
        ga,
        text="acceleration*g_const",
        offset_x=0,
        offset_y=20
    )
    set_input_by_image(
        TEMPLATE_DIR/"afy_0.png",
        ga,
        text="0",
        offset_x=-50
    )

    print("🎉 COMSOL 参数设置完成")

    # 计算
    click_by_image(TEMPLATE_DIR/"yanjiu.png", ga)
    click_by_image(TEMPLATE_DIR/"jisuan.png", ga)

    time.sleep(30)  # 前 30 秒必算
    wait_for_compute_done_cv(
        computing_image=TEMPLATE_DIR/"computing.png",
        threshold=0.8,
        timeout=600,
        check_interval=1.0,
        confirm_miss=3
    )

    print("🎉 Demo finished successfully")


if __name__ == "__main__":
    main()
