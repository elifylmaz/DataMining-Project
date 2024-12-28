from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Firefox WebDriver için ayarlar
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument("--start-maximized")
options.set_preference("general.useragent.override", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# WebDriver'ı başlat
driver = webdriver.Firefox(options=options)

# Timeout süresini artır
driver.set_page_load_timeout(300)

# İlk sayfanın linkini girin
base_url = "https://letterboxd.com/film/parasite-2019/reviews/by/activity/"

# Tüm yorumları kaydetmek için bir liste oluştur
all_reviews = []

try:
    # İlk sayfayı aç
    driver.get(base_url)
    wait = WebDriverWait(driver, 30)

    while True:  # Next butonuna basılabildiği sürece devam et
        print(f"Sayfa açıldı, yorumlar çekiliyor...")

        # Dinamik içeriklerin yüklenmesini bekle
        review_elements = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.body-text"))
        )

        # "I can handle the truth" butonlarına tıklama
        try:
            spoiler_buttons = driver.find_elements(By.LINK_TEXT, "I can handle the truth.")
            for button in spoiler_buttons:
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", button)
                    button.click()  # Spoiler içeriğini açmak için tıkla
                    time.sleep(1)  # İçeriğin yüklenmesi için bekleme
                except Exception as e:
                    print(f"Bir hata oluştu: {e}")
        except Exception as e:
            print(f"Spoiler butonları bulunamadı: {e}")

        # "more" düğmelerine tıklama
        try:
            more_buttons = driver.find_elements(By.LINK_TEXT, "more")
            for button in more_buttons:
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", button)
                    button.click()  # Yorumun tamamını görmek için tıkla
                    time.sleep(1)  # İçeriğin yüklenmesi için bekleme
                except Exception as e:
                    print(f"'more' düğmesine tıklanırken bir hata oluştu: {e}")
        except Exception as e:
            print(f"'more' düğmeleri bulunamadı: {e}")

        # Yorumları al
        reviews = [review.text for review in review_elements]
        all_reviews.extend(reviews)  # Yorumları ana listeye ekle

        # "Next" butonuna tıklama
        try:
            next_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.next")))
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)  # Next butonunu görünür yap
            next_button.click()  # Sonraki sayfaya git
            time.sleep(5)  # Yeni sayfanın yüklenmesini bekle
        except Exception as e:
            print("Sonraki sayfa bulunamadı, işlem tamamlandı.")
            break  # Eğer "Next" butonu yoksa döngüden çık

    # Yorumları bir dosyaya kaydet
    print("Tüm yorumlar çekildi. Dosyaya kaydediliyor...")
    with open("all_reviews_3.txt", "w", encoding="utf-8") as file:
        for i, review in enumerate(all_reviews, 1):
            file.write(f"{i}. Yorum: {review}\n")

except Exception as e:
    print(f"Hata oluştu: {e}")

finally:
    # Tarayıcıyı kapat
    driver.quit()
