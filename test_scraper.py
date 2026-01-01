import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_run():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Cloudflare bypass karne ke liye fake user agent
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    
    try:
        print("🌐 Testing Mindbody URL...")
        # Direct URL for Jan 2nd
        test_url = "https://clients.mindbodyonline.com/classic/mainclass?studioid=780094&date=01/02/2026"
        driver.get(test_url)
        
        time.sleep(15) # Cloudflare challenge ke liye wait
        
        print(f"📄 Page Title: {driver.title}")
        
        # Check if we are still stuck on Cloudflare
        if "Just a moment" in driver.title or "Attention Required" in driver.title:
            print("❌ Still blocked by Cloudflare on GitHub.")
        else:
            print("✅ Successfully bypassed Cloudflare!")
            
            # Frame check
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            if iframes:
                driver.switch_to.frame(0)
                print("📥 Inside Data Frame.")

            rows = driver.find_elements(By.CLASS_NAME, "row")
            print(f"📊 Found {len(rows)} classes!")
            
            for row in rows[:3]: # Pehli 3 classes print karein
                print(f"👉 Data: {row.text.splitlines()[0] if row.text else 'No text'}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_run()
