from selenium import webdriver
from urllib.parse import quote
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import chrome
import time
import re
import readandwrite
import webbrowser

def search_images_on_google(input_data, mode, language, s, SyntacticUnit, searchPhrase):
    if language == 'cro':
        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--force-dark-mode")
        chrome_options.add_argument("--lang=eng")  # Set the language to English

        # Provide the path to the ChromeDriver executable
        chrome_driver_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver"  # Replace with the actual path to ChromeDriver

        # Initialize the ChromeDriver service
        service = Service(chrome_driver_path)

        # Initialize the Chrome WebDriver with options and the service
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif language == 'chr':
        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--lang=de")  # Set the language to German

        # Provide the path to the ChromeDriver executable
        chrome_driver_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver"  # Replace with the actual path to ChromeDriver

        # Initialize the ChromeDriver service
        service = Service(chrome_driver_path)

        # Initialize the Chrome WebDriver with options and the service
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif language == 'chro':
        driver = webdriver.Chrome()
    elif language == 'edge':
        # Create the driver object
        driver = webdriver.Edge()

    if input_data.startswith("http"):
        # If the input data starts with "http" or "https", treat it as an HTML link
        html_link = input_data

        # Open the HTML page in the web driver
        driver.get(html_link)

        # Retrieve the text content from the web page
        body_element = driver.find_element("tag name", "body")
        text_content = body_element.text
    else:
        # Treat the input data as a text
        text_content = input_data

    # Split the text content into sentences
    sentences = text_content.split(".")
    sentences = text_content.split("!")
    sentences = text_content.split("?")

    # Split the text content into sentences using multiple delimiters
    sentences = re.split(r'[.!?]', text_content)
    sentences = re.split(r'[-•!?]', text_content)
    #sentences = re.split(r'[–→⇒•▪”.,;:()!?]', text_content)
    sentences = re.split(r'[-–—↔→⇒•▪”".,;:()!?]', text_content)
    #sentences = re.split(r'[().,:-]', text_content)

    # Remove leading/trailing whitespaces from each sentence
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # Initialize the current sentence index
    current_index = 0
    # Process each sentence
    while current_index < len(sentences):
        # Retrieve the current sentence based on current_index
        current_sentence = sentences[current_index]

        # Clean up the sentence by removing leading/trailing whitespaces
        current_sentence = current_sentence.strip()

        # Split the sentence into words or word phrases
        syntactic_units = current_sentence.split()
        if SyntacticUnit == "p":
            phrases = sentences
            syntactic_units = phrases
        count = 0
        # Search each word or word phrase on Google Images
        for syntactic_unit in syntactic_units:
            syntactic_unit = syntactic_unit.lower()
          #  if syntactic_unit == "is":
            #    syntactic_unit = "to be"
           # elif syntactic_unit == "be":
            #    syntactic_unit = "to be"
           # elif syntactic_unit == "was":
              #  syntactic_unit = "to be"

            word_length = len(syntactic_unit)

            files = readandwrite.readdir('englishtoclipart')

            clipart = False
            for filenpath in files:  # loop through files in the current directory
                lines = readandwrite.read(filenpath)
                for line in lines:
                    parts = [part.strip() for part in line.split(';')]
                    if syntactic_unit == parts[0]:
                        syntactic_unit = parts[1]
                        if len(parts) >= 3:
                            clipart = True
                    # print(line)


            if word_length < 3:
                delay_seconds = max(1, word_length / 5)*2*float(s)  # Adjust the factor as needed
            else:
                delay_seconds = max(1, word_length / 5)*float(s)  # Adjust the factor as needed


            t = 2
            encoded_syntactic_unit = quote(syntactic_unit)

            if mode == "go":
                search_query2 = f"https://www.google.com/search?q={encoded_syntactic_unit}"
            if mode == "walk":
                search_query = f"https://www.google.com/search?q={encoded_syntactic_unit} meaning in english"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit}"
            elif mode == "fromto":
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} clipart"
            elif mode == 'art':
                #imagetype = input("Add am image type like: art clipart gif anime movie: ")
                if clipart:
                    search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase}"
                else:
                    search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase} clipart "
                #search_query2 = f"https://www.google.it/search?q={encoded_syntactic_unit} clipart&cr=countryIT&sca_esv=07360a605685315c&as_st=y&udm=2&tbs=ctr:countryIT,itp:clipart&sxsrf=AHTn8zont7zNBUGn0s09qguWGoW8Wf5JWA:1742526226277&source=lnt&sa=X&ved=2ahUKEwjFpuqFmJqMAxXE1wIHHRDMLtMQpwV6BAgBECY&biw=1660&bih=845&dpr=1.12"
                #search_query2 = f"https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query={encoded_syntactic_unit} 클립 아트"
                #search_query2 = f""
            elif mode == 'photo':
                #search_query2 = f"https://www.bing.com/images/search?q={encoded_syntactic_unit}"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase}"
                #search_query2 = f"https://it.images.search.yahoo.com/search/images;_ylt=Awrij7fwvelnveEQdAYdDQx.;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDMjExNDcxOTAwNQRfcgMyBGZyA3NmcARmcjIDcDpzLHY6aSxtOnNiLXRvcARncHJpZANaLjBIMV9Vc1RPMkNNSzZWd1A4cEZBBG5fcnNsdAMwBG5fc3VnZwM2BG9yaWdpbgNpdC5pbWFnZXMuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNARxdWVyeQN0ZXN0BHRfc3RtcAMxNzQzMzcyMDYy?p={encoded_syntactic_unit}&fr=sfp&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&ei=UTF-8&x=wrt"
                #search_query2 = f"https://it.images.search.yahoo.com/search/images;_ylt=Awrij16XCuFnG7s78IsdDQx.?p={encoded_syntactic_unit}"
            elif mode == 'insta':
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} site:instagram.com"
                #search_query2 = f"https://www.instagram.com/{encoded_syntactic_unit}/"
            elif mode == "walk":
                search_query = f"https://www.google.com/search?q={encoded_syntactic_unit}"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} gif"
            elif mode == 'car':
                #in movies
                delay_seconds = 5*float(s)
                search_query2 = f"https://www.youtube.com/results?search_query={encoded_syntactic_unit} {searchPhrase}"
                #search_query2 = f"https://www.youtube.com/feed/history?query={encoded_syntactic_unit}"
            elif mode == 'train':
                delay_seconds = 5*float(s)
                search_query = f"https://earth.google.com/web/search/{encoded_syntactic_unit}"
                search_query2 = f"https://www.youtube.com/results?search_query={encoded_syntactic_unit} vlog"
            elif mode == 'homerun':
                delay_seconds = 5*float(s)
                search_query = f"https://earth.google.com/web/search/{encoded_syntactic_unit}"
                #travel vlogs

                search_query2 = f"https://www.youtube.com/results?search_query={encoded_syntactic_unit} vlog"
            elif mode == 'droneshooting':
                delay_seconds = 5*float(s)
                t = 5
                search_query = f"https://earth.google.com/web/search/{encoded_syntactic_unit}"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} drone"
            elif mode == 'drone':
                delay_seconds = 5*float(s)
                t = 5
                search_query = f"https://earth.google.com/web/search/{encoded_syntactic_unit}"
                search_query2 = f"https://www.youtube.com/results?search_query={encoded_syntactic_unit} drone"
            elif mode == 'van':
                t = float(s)
                search_query = f"https://earth.google.com/web/search/{encoded_syntactic_unit}"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit}"
            elif mode == 'spaceship':
                t = float(s)
                search_query2 = f"https://earth.google.com/web/search/{encoded_syntactic_unit}"
                search_queryN = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit}"
            elif mode == 'airplane':
                delay_seconds = 5*float(s)
                t = delay_seconds/4
                search_query = f"https://earth.google.com/web/search/{encoded_syntactic_unit}"
                search_query2 = f"https://www.youtube.com/results?search_query={encoded_syntactic_unit}"
            elif mode == 'lmaooo':
                delay_seconds = 5*float(s)
                t = delay_seconds/8
                search_query = f"https://earth.google.com/web/search/{encoded_syntactic_unit}"
                search_query2 = f"https://www.youtube.com/results?search_query={encoded_syntactic_unit} timelapse&sp=CAM%253D"
            elif mode == "url":
                search_query2 = f"https://{encoded_syntactic_unit}"

            #time.sleep(5)
            # Open a new tab with the search query URL

            # mode == "art" or
            if mode == "go" or mode == "art" or mode == "photo" or mode == "insta" or mode == "car" or mode == 'spaceship' or count % 2 == 1:
                pass
            else:
                driver.execute_script(f"window.open('{search_query}', '_blank')")
                #if mode == "art":
                #    pass
                #else:
                #time.sleep(t*2)
                time.sleep(delay_seconds)
            #webbrowser.open(search_query2)
            driver.execute_script(f"window.open('{search_query2}', '_blank')")

            time.sleep(delay_seconds)
            #count += 1
        time.sleep(3)
            # Calculate the delay based on the length of the word or phrase


        # Wait for the user input
        x = 0
        if x == 1:
            choice = input(
                f"Sentence:" + current_sentence + "\n"
                f"Enter 'n' to read the next sentence, 'p' to read the previous sentence, 's' to skip, "
                                                  f"or enter a number to jump to a specific sentence: ")

        elif x == 0:
            choice = 'n'

        # Process user input
        if choice == 'n':
            current_index += 1
            if SyntacticUnit == 'p':
                current_index = len(sentences)
        elif choice == 'p':
            current_index -= 1
            if current_index < 0:
                current_index = 0
        elif choice == 's':
            current_index += 2
        elif choice.isdigit():
            choice_index = int(choice)
            if 0 <= choice_index < len(sentences):
                current_index = choice_index
            else:
                print("Invalid sentence number. Skipping to the next sentence.")
        else:
            # Allow the user to enter text input in the same tab
            text_input = input("Enter text input: ")

            # Perform any necessary processing on the entered text input
            print("Entered text:", text_input)

            search_images_on_google(text_input, language)
            # Continue to the previous sentence
            current_index += 1

        # Close all the opened tabs except the original page
        original_handle = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != original_handle:
                driver.switch_to.window(handle)
                driver.close()
                #webbrowser.close()

        # Switch back to the original page
        driver.switch_to.window(original_handle)

    # Close the web driver
    driver.quit()


#input_data = "I think this maintenance diet is successful because it’s hard to overeat when you have only one significant meal a day. If my weight creeps upward a few pounds—which sometimes happens—I eliminate the bread and dessert until my weight returns to normal."


input_data = input("Enter an HTML link or a text: ")
SyntacticUnit = input("p for Phase : ")
s = input("Enter how long you want to see it: ")

mode = input("how do you want to travel? \nphotograph, walk, art, car, drone, 'homerun', airplane, train, spaceship, lmaooo: ")
searchPhrase = input("what do you want to add? ")

# Call the function with the input data input html link or text
while(True):
    if input_data == "m":
        mode = input("how do you want to travel? \nphotograph, walk, art, car, drone, 'homerun', airplane, train, spaceship, lmaooo: ")
        input_data = input("Enter an HTML link or a text: ")
    elif input_data == "t":
        s = input("Enter how long you want to see it: ")
        input_data = input("Enter an HTML link or a text: ")
    elif input_data == "p":
        SyntacticUnit = input("p for Phase : ")
        input_data = input("Enter an HTML link or a text: ")
    elif input_data == "w":
        searchPhrase = input("what do you want to add? ")
        input_data = input("Enter an HTML link or a text: ")
    else:
        search_images_on_google(input_data, mode, 'chro', s, SyntacticUnit, searchPhrase)
        input_data = input("Enter an HTML link or a text: ")
