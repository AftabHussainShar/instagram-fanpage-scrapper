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

# word = 'hawa'
# foll = 20000
with open('Instagram_rules.txt', 'r') as file:
    line = file.readline()
    line = line.split(',')
    word = line[0]
    foll = line[1]


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
    
def convert_to_int(number_str):
    multiplier = 1
    if number_str[-1] == 'K':
        multiplier = 1000
        number_str = number_str[:-1]
    elif number_str[-1] == 'M':
        multiplier = 1000000
        number_str = number_str[:-1]
    else:
        # int number_str
        number_str = number_str.replace(',', '')
        if '.' in number_str:
            number_str = number_str.replace('.', '')
        if number_str == '':
            return None
    try:
        return int(float(number_str) * multiplier)
    except ValueError:
        return None

def check(profile,driver):
    try:
        driver.get(f'{profile}')
        sleep(3)
         # bio 
        try:
            bio = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[4]/div'))
                    )
            bio = bio.text
        except:
            bio = "Not found"
                    
                # followers count 
        try:
            followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span')
            followers = followers.text
        except:
            try:
                followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span')
                followers = followers.text
            except:
                followers = "Not found"

        # following count
        try:
            following = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span')
            following = following.text
        except:
            try:
                following = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span')
                following = following.text
            except:
                following = "Not found"
                
        following=convert_to_int(following)
        followers=convert_to_int(followers)
        print(f"Bio: {bio}")
        print(f"Followers: {followers}")
        print(f"Following: {following}")
        profile_ = profile.replace('https://www.instagram.com', '')
        username = profile_.replace('/', '')
        # Check conditions and return result
        if word in bio.lower() and followers > foll:
            return [profile, username]
        else:
            return False
       
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


    with open(f'{profile}_following.csv', mode="a", newline="", encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Profile", "Username"])

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
    try:
        # Read profile links from file
        with open('links.txt', 'r') as file:
            data = file.read()
        data_list = data.split('\n')

        # Read count value from count.txt
        with open('count.txt', 'r') as file:
            count = file.readline().strip()
            count = int(count) if count else 0

        # Read last processed index from state.txt
        try:
            with open('state.txt', 'r') as file:
                data1 = file.read().strip()
                start_index = int(data1) if data1 else 0
        except FileNotFoundError:
            start_index = 0

        # Check if all links have been processed
        if start_index >= len(data_list):
            print('All profiles have been processed.')
            return

        # Initialize driver
        driver = login_to_Insta(username, password, 'yes')

        # Process each profile link
        followings = []
        chk_value = 0
        while start_index < len(data_list):
            following_link = data_list[start_index].strip()
            if not following_link:
                start_index += 1
                continue

            try:
                print(f"Processing: {following_link}")
                with open('state.txt', 'w') as file:
                    file.write(str(start_index))

                data = check(following_link, driver)

                if data is not None:
                    with open(f'{profile}_following.csv', mode="a", newline="", encoding='utf-8') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(data)

                chk_value += 1
                if chk_value >= count:
                    driver.quit()
                    sleep(30)
                    driver = login_to_Insta(username, password, 'yes')  # Reinitialize driver
                    chk_value = 0  # Reset counter

            except Exception as e:
                print(f"Error processing {following_link}: {e}")

            start_index += 1

        # Clean up and finalize
        driver.quit()
        delete_file_contents('state.txt')
        delete_file_contents('links.txt')
        print('Processing complete. All data written to CSV.')

    except Exception as e:
        print(f"An error occurred: {e}")

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
# us = 'just_talk009'

profile_scrapper(us)
