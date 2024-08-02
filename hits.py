from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# WebDriver'ı başlat (Firefox için GeckoDriver kullanacağız)
driver = webdriver.Firefox()

try:
    # Kullanıcıdan website ismini al
    website = input("Lütfen gitmek istediğiniz websitesinin URL'sini girin: ")

    while True:
        # Web sitesini aç
        driver.get(website)

        # Sayfanın tamamen yüklenmesi için bekle
        time.sleep(5)

        # Sayfayı aşağı yukarı kaydırma
        for _ in range(5):  # 5 kere aşağı yukarı kaydırma işlemi yapılacak
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
            time.sleep(2)

        # 10 saniye bekle ve sayfayı yeniden yükle
        time.sleep(10)
        # (Sonsuz döngü devam ettiği için while True döngüsü sayfayı baştan açar)

finally:
    # WebDriver'ı kapat
    driver.quit()
