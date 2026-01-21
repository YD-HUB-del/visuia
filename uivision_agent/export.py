from .click import click_by_image
import time
from .input import set_input_by_image



def export_result(tab_png, filename):
        click_by_image(tab_png, ga)
        click_by_image("qingkong.png", ga)
        click_by_image("jisuan^Cx.png", ga)
        time.sleep(10)
        click_by_image("daochu.png", ga)

        set_input_by_image(
            "baocunlujing.png",
            ga,
            text=out_dir,
            click_mode="single",
            
        )

        set_input_by_image(
            "wenjianming.png",
            ga,
            text=filename,
            offset_x=50
        )

        click_by_image("baocun.png", ga, click_type="double")