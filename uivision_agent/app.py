import time
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError

def activate_app(app_name: str, wait: float = 1.0):
    """
    检测并激活指定软件窗口（基于窗口标题）

    Parameters
    ----------
    app_name : str
        软件名称关键字（如 "COMSOL", "MATLAB", "ANSYS"）
    wait : float
        激活后等待时间（秒）

    Returns
    -------
    win : pywinauto.application.WindowSpecification
        已激活的窗口对象

    Raises
    ------
    RuntimeError
        如果未找到对应软件窗口
    """
    try:
        app = Application(backend="uia").connect(title_re=f".*{app_name}.*")
        win = app.window(title_re=f".*{app_name}.*")
        win.set_focus()
        time.sleep(wait)
        return win
    except ElementNotFoundError:
        raise RuntimeError(f"❌ 未检测到已启动的软件窗口：{app_name}")