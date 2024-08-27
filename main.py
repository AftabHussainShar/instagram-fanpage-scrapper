import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# import undetected_chromedriver as uc
# from selenium.webdriver.common.proxy import Proxy, ProxyType
#import pyautogui


def login_to_Insta(username, password,login):
    with open('proxy.txt', 'r') as file:
        line = file.readline()
        line = line.split(':')

    proxy_ip = line[0]
    proxy_port = int(line[1])
    proxy_username = line[2]
    proxy_password = line[3]

    #chrome_driver_path = r"chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()


    chrome_options.add_argument('--no-sandbox')
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    chrome_options.add_argument(f"--user-agent={user_agent}")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    #chrome_options.add_argument(f"--proxy-server=http://{proxy_ip}:{proxy_port}")
    #driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    chrome_driver_dir = 'chromedriver.exe'  # Update this path

    # Set the PATH environment variable to include the ChromeDriver directory
    os.environ["PATH"] += os.pathsep + chrome_driver_dir

    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.maximize_window()
    driver.get('https://www.instagram.com/')
    sleep(3)
    # pyautogui.typewrite(proxy_username)
    # pyautogui.press('tab')
    # pyautogui.typewrite(proxy_password)
    # pyautogui.press('enter')
    # sleep(10)
    if login == 'yes':
        try:
            username_input = driver.find_element(By.XPATH, '//input[@aria-label="Phone number, username, or email"]')
            username_input.send_keys(Keys.CONTROL + 'a')
            username_input.send_keys(username)
            password_input = driver.find_element(By.XPATH, '//input[@aria-label="Password"]')
            password_input.send_keys(Keys.CONTROL + 'a')
            password_input.send_keys(password)
            sleep(1)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            sleep(10)
        except:
            print('You have Already login')
    return driver
# def login_to_Insta(username, password):
#     service = Service(ChromeDriverManager().install())
#     chrome_options = webdriver.ChromeOptions()
#     # chrome_options.binary_location = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
#     chrome_options.add_argument("--no-sandbox")
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
#     chrome_options.add_argument(f"--user-agent={user_agent}")
#     # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     chrome_options.add_argument("--disable-notifications")
#     # chrome_options.add_argument("--disable-geolocation")
#     chrome_options.add_argument("--disable-features=Geolocation")
#     # chrome_options.add_argument("--blink-settings=imagesEnabled=false")
#     # chrome_options.add_argument('--headless')
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver.maximize_window()
#     driver.get('https://www.instagram.com/')
#     sleep(10)
#     try:
#         username_input = driver.find_element(By.XPATH, '//input[@aria-label="Phone number, username, or email"]')
#         username_input.send_keys(Keys.CONTROL + 'a')
#         username_input.send_keys(username)
#         password_input = driver.find_element(By.XPATH, '//input[@aria-label="Password"]')
#         password_input.send_keys(Keys.CONTROL + 'a')
#         password_input.send_keys(password)
#         sleep(1)
#         driver.find_element(By.XPATH, '//button[@type="submit"]').click()
#         sleep(10)
#     except:
#         print('You have Already login')
#     # sleep(3)
#     input()
#
#     return driver


def search_for_profile(profile,driver):
    # Access Search bar
    search_icon = driver.find_element(By.XPATH,
                                      '//div[@class="x1xgvd2v x1o5hw5a xaeubzz x1cy8zhl xvbhtw8 x9f619 x78zum5 xdt5ytf x1gvbg2u x1y1aw1k xn6708d xx6bls6 x1ye3gou"]/div[2]/div[2]/span/div/a')
    search_icon.click()
    sleep(5)
    search_input = driver.find_element(By.XPATH, '//input[@aria-label="Search input"]')
    sleep(5)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search input"]')))

    # Search for Specific Profile
    search_input.send_keys(f"{profile}")  # << ENTER INSTAGRAM PROFILE HANDLE TO SCRAPE FOLLOWERS FROM
    sleep(5)
    profile_selection = driver.find_element(By.XPATH,
                                            f"//*[contains(text(), '{profile}')]")  # << ENTER IG PROFILE HANDLE AGAIN
    profile_selection.click()
    sleep(5)


def check(profile,driver):
    try:
        driver.get(f'{profile}')
        sleep(3)
        c = 0
        try:
            followers = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[1]/span')))
            followers_text = followers.text
        except:
            try:
                followers = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '//*[@id="mount_0_0_vg"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[2]/div/a/span/span')))
                followers_text = followers.text
            except:
                followers_text = ''
        print('No folllowers text found')

        if 'k' in followers_text.lower() or 'm' in followers_text.lower():
            c = 1
        elif ',' in followers_text:
            followers_text = followers_text.replace(',', '')
            ch = int(followers_text)
            if ch >= 3000:
                c = 1
        # if c == 1:
        #     link = ''
        #sleep(2)
        try:
            # link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[3]/a/span/span')))
            # link = link.text
            link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                        '//div[@class="x3nfvp2 x193iq5w"]//span[@class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft"]'))).text
            
        except:
            print('Link Not Found')
        
        print(link)
        if 'instagram' in link or 'youtube' in link or 'youtu.be' in link or 'tiktok' in link or 'wa.me' in link or 'twitter' in link or 'facebook' in link or 'wa.link' in link or 'whatsapp' in link or 'soundcloud' in link or 'walink' in link or '' == link or 'Facebook profile' in link:
            return None
        else:
            return link

        # else:
        #     return None
    except:
        return None


def create_following_list(driver):
    followings = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()=" following"]')))
    # followings = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
    followings.click()
    sleep(5)
    try:
        try:
            sc = driver.find_element(By.XPATH, '//div[@class="_aano"]')
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", sc)
            ch = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                '//div[@class="_aano"]//span[@style="line-height: var(--base-line-clamp-line-height); --base-line-clamp-line-height: 20px;"]')))
            c = ch.text
            print(ch)
        except:
            c = ''
        if 'Suggested for you' in c:
            print(c)
            scroll_path = '//input[@aria-label="Search input"]/ancestor::div[3]/div[4]'
            scroll_box = driver.find_element(By.XPATH, scroll_path)
            print('SC 1')
        else:
            print('SC 2')
            scroll_path = '//input[@aria-label="Search input"]/ancestor::div[3]/div[4]'
            scroll_box = driver.find_element(By.XPATH, scroll_path)
    except:
        print('abc')

    chunk_size = 100
    last_ht, ht = 0, 1
    Followings_link = []
    while True:
        last_ht = ht
        sleep(1)
        ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroll_box)
        sleep(7)
        if last_ht == ht:
            break
        if not driver.execute_script("return arguments[0].parentNode", scroll_box):
            break
        links = scroll_box.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            count = Followings_link.count(href)
            if count == 0:
                Followings_link.append(href)
            elif count > 1:
                while Followings_link.count(href) > 1:
                    Followings_link.remove(href)

        if len(Followings_link) == chunk_size:
            break

    sleep(2)
    cross = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_abl-"]')))
    cross.click()
    # driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button').click()
    sleep(2)

    return Followings_link

def write_links_to_file(filename, links):
     with open(filename, 'w') as file:
        for link in links:
            file.write(link + "\n")

def Scrape(profile,driver):
    search_for_profile(profile,driver)
    followings_link = create_following_list(driver)
    print(len(followings_link))
    print(f'Following: {followings_link}')
    write_links_to_file('links.txt', followings_link)
    followings = []
    sleep(3)
    try:
        name = driver.find_element(By.XPATH,
                                   '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[1]/span').text
    except:
        name = ''
    try:
        about = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/h1').text
        about = about.replace('\n', ',')
    except:
        about = ''
    try:
        link = driver.find_element(By.XPATH,
                                   '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[3]/div/a/span/span').text
    except:
        link = ''

    #print(f'Followers: {followers}')
    print(f'Following: {followings}')
    print(f'Name: {name}')
    print(f'About: {about}')
    print(f'Link: {link}')

    with open(f'{profile}.csv', mode="a", newline="", encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Name", "About", "Link"])
        csv_writer.writerow([name, about, link])


    with open(f'{profile}.csv', mode="a", newline="", encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Followings", "Link"])

    #while True:
def read_txt_file(filepath):
    try:
        # Open the file in read mode ('r')
        with open(filepath, 'r') as file:
            # Read all data from the file
            data = file.read()
            if data is not None:
                return data
            else:
                return 0
    except FileNotFoundError:
        print(f"Error: File not found.")
        return None

def profile_scrapper(profile):
    data = read_txt_file('links.txt')
    data_list = data.split('\n')
    chk_value = 0
    with open('count.txt', 'r') as new1file:
        # Read all data from the file
        count = new1file.readline()
        if count:
            count = int(count.strip())
        else:
            count = 0

    while True:
        try:
            with open('state.txt', 'r') as newfile:
                # Read all data from the file
                data1 = newfile.read()
                if data1:
                    lines = data1.strip().split('\n')
                    last_index_str = lines[-1]
                    if last_index_str:
                        start_index = int(last_index_str)
                    else:
                        start_index = 0
                else:
                    # If file is empty, start with index 0
                    start_index = 0
            if len(data_list) - 1 == start_index:
                delete_file_contents('state.txt')
                delete_file_contents('links.txt')
                print('complete')
                break

            driver = login_to_Insta(username, password, 'yes')
            #input('press yes to continue')
            followings = []

            for following_link in data_list[start_index:]:
                try:
                    print(following_link)
                    index = data_list.index(following_link)
                    with open('state.txt', 'w') as readfile:
                        readfile.write(str(index))
                    ch = check(following_link, driver)
                    if ch is not None:
                        following = following_link.replace('https://www.instagram.com', '')
                        following = following.replace('/', '')
                        with open(f'{profile}.csv', mode="a", newline="", encoding='utf-8') as csv_file:
                            csv_writer = csv.writer(csv_file)
                            csv_writer.writerow([following, ch])
                        followings.append(following)
                except:
                    pass



                if chk_value ==  count:
                    driver.quit()
                    chk_value = 0  # Reset the counter
                    sleep(30)
                    break
                chk_value += 1
        except:
            break

def delete_file_contents(file_path):
    with open(file_path, 'w') as file:
        file.truncate(0)

with open('Instagram_cridentials.txt', 'r') as file:
    line = file.readline()
    line = line.split(',')
    username = line[0]
    password = line[1]
with open('permission.txt', 'r') as newfile:
    permission = newfile.readline()


us = input('Enter Username: ')
permission = permission.strip()
if permission == 'yes':
    driver = login_to_Insta(username, password, 'yes')
    sleep(10)
    Scrape(us, driver)
    driver.quit()


profile_scrapper(us)
