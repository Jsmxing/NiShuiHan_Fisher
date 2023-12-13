import pyautogui
import cv2
import mss
import time

def auto_start():
    # 截取屏幕截图
    with mss.mss() as sct:
        # 截取整个屏幕
        sct.shot(output='screenshot_start.png')

    # 加载待识别的图片
    screenshot = cv2.imread('screenshot_start.png')
    image = cv2.imread('start.png')

    # 在屏幕截图中查找目标图片
    result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # 根据匹配结果的阈值，判断是否找到目标图片：
    threshold = 0.8  # 阈值可以根据实际情况调整
    if max_val >= threshold:
        # 找到目标图片，进行点击操作
        target_width, target_height = image.shape[:-1]
        target_center_x = max_loc[0] + target_width // 2
        target_center_y = max_loc[1] + target_height // 2
        pyautogui.moveTo(target_center_x, target_center_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveRel(0, -100)

        # 找到以后进行下一步
        time.sleep(1)
        print("start end")
        auto_get()

    else:
        auto_start()

def auto_get():
    # 截取屏幕截图
    with mss.mss() as sct:
        # 截取整个屏幕
        sct.shot(output='screenshot_get.png')

    # 加载待识别的图片
    screenshot = cv2.imread('screenshot_get.png')
    image = cv2.imread('get.png')

    # 在屏幕截图中查找目标图片
    result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # 根据匹配结果的阈值，判断是否找到目标图片：
    threshold = 0.8  # 阈值可以根据实际情况调整
    if max_val >= threshold:
        # 找到目标图片，进行点击操作
        target_width, target_height = image.shape[:-1]
        target_center_x = max_loc[0] + target_width // 2
        target_center_y = max_loc[1] + target_height // 2
        pyautogui.moveTo(target_center_x, target_center_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveRel(0, -100)

        time.sleep(1)
        print("get end")
        auto_end()
    else:
        # 没有找到目标图片 重复执行
        auto_bug()

def auto_end():
    # 截取屏幕截图
    with mss.mss() as sct:
        # 截取整个屏幕
        sct.shot(output='screenshot_end.png')

    # 加载待识别的图片
    screenshot = cv2.imread('screenshot_end.png')
    image = cv2.imread('end.png')

    # 在屏幕截图中查找目标图片
    result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # 根据匹配结果的阈值，判断是否找到目标图片：
    threshold = 0.8  # 阈值可以根据实际情况调整
    if max_val >= threshold:
        # 找到目标图片，进行点击操作
        target_width, target_height = image.shape[:-1]
        target_center_x = max_loc[0] + target_width // 2
        target_center_y = max_loc[1] + target_height // 2
        pyautogui.moveTo(target_center_x, target_center_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveRel(0, -100)

        time.sleep(3)
        print("end end")
        auto_start()
    else:
        # 没有找到目标图片 重复执行
        time.sleep(1)
        auto_end()

def auto_bug():
    with mss.mss() as sct:
        # 截取整个屏幕
        sct.shot(output='screenshot_get.png')

    # 加载待识别的图片
    screenshot = cv2.imread('screenshot_get.png')
    image = cv2.imread('bug.png')

    # 在屏幕截图中查找目标图片
    result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # 根据匹配结果的阈值，判断是否找到目标图片：
    threshold = 0.8  # 阈值可以根据实际情况调整
    if max_val >= threshold:
        print("bug!")
        auto_start()
    else:
        # 没有找到目标图片 重复执行
        print("no bug")
        auto_get()

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    auto_start()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
