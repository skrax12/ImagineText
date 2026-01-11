from selenium import webdriver
from urllib.parse import quote
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import re
import readandwrite
import helperfunctions
from pyswip import Prolog


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
    time.sleep(3)

    # Split the text content into sentences
    sentences = text_content.split(".")
    sentences = text_content.split("!")
    sentences = text_content.split("?")

    # Split the text content into sentences using multiple delimiters
    #sentences = re.split(r'[.!?]', text_content)
    #sentences = re.split(r'[-•!?]', text_content)
    #sentences = re.split(r'[–→⇒•▪”.,;:()!?]', text_content)
    #sentences = re.split(r'[-—↔→⇒•▪”“".;:{()}/|!?%]', text_content)
    #sentences = re.split(r'[().,:-]', text_content)

    if SyntacticUnit == '':
        sentences = re.split(r'[—↔→⇒•▪”“".,;:\[{()}\]/|!?%]', text_content)
        if mode == 'art':
            sentences = re.split(r'[—↔→⇒•▪.;:\[{()}\]/|!?]', text_content)
    if SyntacticUnit == 'xp':
        if mode == 'art':
            sentences = re.split(r'[-—↔→⇒•▪”“".;:\[{()}\]/|!?%]', text_content)
    if SyntacticUnit == 'p':
        sentences = re.split(r'[-—↔→⇒•▪”“".;:\[{()}\]/|!?%]', text_content)
        if mode == 'art':
            sentences = re.split(r'[-—↔→⇒•▪”“";:\[{()}\]/|!?%]', text_content)

    # Remove leading/trailing whitespaces from each sentence
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # Initialize the current sentence index
    current_index = 0
    # Process each sentence
    while current_index < len(sentences):
        # Retrieve the current sentence based on current_index
        current_sentence = sentences[current_index]

        current_sentence = current_sentence.replace(',', '')
        current_sentence = current_sentence.replace('\'', '')


        # Clean up the sentence by removing leading/trailing whitespaces
        current_sentence = current_sentence.strip()

        # Split the sentence into words or word phrases
        syntactic_units = current_sentence.split()
        if SyntacticUnit == "p":
            phrases = sentences
            syntactic_units = phrases
        count = 0
        # Search each word or word phrase on Google Images
        for i in range(len(syntactic_units)):
            syntactic_units[i] = syntactic_units[i].lower()
          #  if syntactic_units[i] == "is":
            #    syntactic_units[i] = "to be"
           # elif syntactic_units[i] == "be":
            #    syntactic_units[i] = "to be"
           # elif syntactic_units[i] == "was":
              #  syntactic_units[i] = "to be"

            word_length = len(syntactic_units[i])

            syntactic_units[i] = str(helperfunctions.process_text_numbers(syntactic_units[i]))

            files = readandwrite.readdir('englishtoclipart')

            clipart = False
            url = False
            for filenpath in files:  # loop through files in the current directory
                lines = readandwrite.read(filenpath)
                for line in lines:
                    parts = [part.strip() for part in line.split(';')]

                    if "," in parts[0]:
                        subparts = [subpart.strip() for subpart in parts[0].split(',')]
                        if 0 <= i+1 < len(syntactic_units):
                            syntactic_units[i+1] = syntactic_units[i+1].lower()
                            if syntactic_units[i] == subparts[0] and syntactic_units[i+1] == subparts[1]:
                                syntactic_units[i+1] = parts[1]
                                if len(parts) >= 3:
                                    clipart = True
                            if syntactic_units[i+1] == subparts[0] and syntactic_units[i] == subparts[1]:
                                syntactic_units[i] = parts[1]
                                if len(parts) >= 3:
                                    clipart = True
                    if syntactic_units[i] == parts[0]:
                        syntactic_units[i] = parts[1]
                        if len(parts) >= 3:
                            clipart = True
                        if len(parts) >= 3:
                            if parts[2]== 'va':
                                syntactic_units[i] = syntactic_units[i] + ' vector art'
                            elif parts[2]== 'ca':
                                syntactic_units[i] = syntactic_units[i] + ' clipart'
                            elif parts[2]== 'url':
                                url = True
                    # print(line)

            if word_length < 3:
                delay_seconds = max(1, word_length / 5)*2*float(s)  # Adjust the factor as needed
            else:
                delay_seconds = max(1, word_length / 5)*float(s)  # Adjust the factor as needed


            t = 2
            encoded_syntactic_unit = quote(syntactic_units[i])

            if mode == "go":
                search_query2 = f"https://www.google.com/search?q={encoded_syntactic_unit}"
            if mode == "walk":
                search_query = f"https://www.google.com/search?q={encoded_syntactic_unit} meaning in english"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit}"
            elif mode == "fromto":
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} clipart"
            elif mode == 'art':
                #imagetype = input("Add am image type like: art clipart gif anime movie: ")
                if url:
                    search_query2 = encoded_syntactic_unit
                elif clipart:
                    search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase}"
                    #search_query2 = f"https://www.google.com/search?q={encoded_syntactic_unit} {searchPhrase}&sca_esv=2e41414a5e61d415&udm=2&sxsrf=AE3TifOVesOB0m4SY64R3-YwD9V7TDzFkg:1763890740824&source=lnt&tbs=itp:clipart"
                else:
                    search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase} clipart "
                    #search_query2 = f"https://www.google.com/search?q={encoded_syntactic_unit} {searchPhrase}&sca_esv=2e41414a5e61d415&udm=2&sxsrf=AE3TifOVesOB0m4SY64R3-YwD9V7TDzFkg:1763890740824&source=lnt&tbs=itp:clipart"
                #search_query2 = f"https://duckduckgo.com/?t=h_&q={encoded_syntactic_unit} {searchPhrase} clipart&ia=images&iax=images&iaf=type%3Aclipart"
                #search_query2 = f"https://www.bing.com/images/search?q={encoded_syntactic_unit} {searchPhrase}%20clipart&qs=n&form=QBIR&qft=%20filterui%3Aphoto-clipart&sp=-1&lq=0&pq=test%20clipart&sc=10-12&cvid=F4801A9876794564B46D755487DB5827&ajf=10&first=1"
                #search_query2 = f"https://www.ecosia.org/images?q={encoded_syntactic_unit} {searchPhrase} clipart&imageType=clipart"
                #search_query2 = f"https://www.google.it/search?q={encoded_syntactic_unit} clipart&cr=countryIT&sca_esv=07360a605685315c&as_st=y&udm=2&tbs=ctr:countryIT,itp:clipart&sxsrf=AHTn8zont7zNBUGn0s09qguWGoW8Wf5JWA:1742526226277&source=lnt&sa=X&ved=2ahUKEwjFpuqFmJqMAxXE1wIHHRDMLtMQpwV6BAgBECY&biw=1660&bih=845&dpr=1.12"
                #search_query2 = f"https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query={encoded_syntactic_unit} 클립 아트"
                #search_query2 = f""
            elif mode == 'vart':
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase} vector art"
            elif mode == 'try':
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase}"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase} icon"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase} clipart"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase} vector art"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase} illustration"
                search_query2 = f"https://www.google.com/search?tbm=isch&q={encoded_syntactic_unit} {searchPhrase} art"
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
            elif mode == 'starship':
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
                search_query2 = f"https://www.youtube.com/feed/history?query={encoded_syntactic_unit}"

            #time.sleep(5)
            # Open a new tab with the search query URL
            # mode == "art" or
            if mode == "go" or mode == "art" or mode == "vart" or mode == "photo" or mode == "insta" or mode == "car" or mode == 'spaceship' or count % 2 == 1:
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

        if SyntacticUnit ==  'p':
            time.sleep(2)
        else:
            # Calculate the delay based on the length of the word or phrase
            sp = len(syntactic_units) * 2.2  # sentence pause
            time.sleep(sp)

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

if input_data == "prolog":
    prolog = Prolog()
    prolog.consult("Prolog/usasearch")
    #prolog.consult("Prolog/Prolog_PeopleAndPlaces.pl")
    while (True):
        input_data = input('Prolog command: ')

        output_data = list(prolog.query(input_data))
        predicate = str(input_data).split('(')[0]

        output_data = input_data + str(output_data)

        output_data = output_data.replace('\'', '')
        output_data = output_data.replace(':', '')
        output_data = output_data.replace(']', '')
        output_data = output_data.replace('[', '')
        output_data = output_data.replace(',', '')
        # output_data = output_data.replace('\'','')

        search_images_on_google(output_data, mode, 'chro', s, SyntacticUnit, searchPhrase)
    readandwrite.read('Prolog/usasearch')
    #readandwrite.read('Prolog/Prolog_PeopleAndPlaces.pl')

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
