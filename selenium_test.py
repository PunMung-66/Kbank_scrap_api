from selenium import webdriver
from selenium.webdriver.common.by import By

def check_html_tag(url, tag_name):
    # สร้าง WebDriver สำหรับ Chrome
    driver = webdriver.Chrome()

    try:
        # เปิดเว็บไซต์
        driver.get(url)

        # ค้นหา Element ทั้งหมดที่ตรงกับ Tag HTML ที่กำหนด
        elements = driver.find_elements(By.TAG_NAME, tag_name)

        if elements:
            print(f"พบ {len(elements)} ตัวอย่างของ Tag <{tag_name}>")
        else:
            print(f"ไม่พบ Tag <{tag_name}> ในเว็บไซต์")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    
    finally:
        # ปิด WebDriver
        driver.quit()

# เรียกใช้ฟังก์ชั่นเพื่อเช็ค Tag HTML
if __name__ == "__main__":
    url_to_check = "https://www.mindphp.com/developer/python-test-case-selenium/9831-creating-a-function-to-check-html-tags-on-a-website-using-selenium.html"  # เปลี่ยนเป็น URL ของเว็บไซต์ที่คุณต้องการตรวจสอบ
    tag_to_check = "meta"  # เปลี่ยนเป็น Tag HTML ที่คุณต้องการเช็ค

    check_html_tag(url_to_check, tag_to_check)
