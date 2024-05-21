# from bs4 import BeautifulSoup
# import pandas as pd
# import requests
# import logging
# import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import atexit
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# import os
# import spacy
# import requests
# import pymysql
# import pytz
# import datetime
# from selenium.common.exceptions import StaleElementReferenceException

# from datetime import datetime, timedelta

# # Get today's date
# today_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

# # print(today_date)

# mydb = pymysql.connect(
 
#   host="localhost",
#   user=		"root",
#   password=	"Nadmin123$",
#   database=	"narvee_hr"
# )

# mycursor=mydb.cursor

# nlp = spacy.load('en_core_web_sm')
# from DataCleaning import extract_skills
# driver = webdriver.Chrome()

# #driver = webdriver.Chrome('https://www.simplyhired.com')
# # Function to release ChromeDriver
# def release_chromedriver():
#     try:
#         # Close the ChromeDriver session
        
#         driver.quit()
#         print("ChromeDriver released successfully.")
#     except Exception as e:
#         print(f"Error releasing ChromeDriver: {e}")

# # Define CST TimeZone

# # Define CST timezone
# cst_timezone = pytz.timezone('America/Chicago')

# now_cst = datetime.now().astimezone(cst_timezone)
# today_cst = now_cst.strftime('%Y-%m-%d %H:%M:%S')

# yesterday_cst = now_cst - timedelta(days=1)
# yesterday_cst = yesterday_cst.replace(hour=0, minute=0, second=0)
# yesterday_cst_str = yesterday_cst.strftime('%Y-%m-%d %H:%M:%S')



# # Function to check if job already exists
# def job_exists(vendor, job_title, job_location):
#     select_query = f"SELECT vendor, job_title, job_location FROM tbl_rec_requirement WHERE vendor = %s AND job_title = %s AND job_location = %s AND posted_on >= %s AND posted_on <= %s"
#     mycursor.execute(select_query, (vendor, job_title, job_location, yesterday_cst_str, today_cst))
#     if mycursor.fetchone():
#         return True
#     return False



# # driver= webdriver.Chrome()
# # driver.get("https://www.glassdoor.com")




# # from urllib3.exceptions import InsecureRequestWarning
# from Commonfields import Commonfields

# dirname=os.path.dirname(os.path.abspath(__file__))
# print("Directory Name - ", dirname)

# df=pd.read_excel(os.path.join(dirname,'/Users/admin/Documents/IT_skill_category_HOT_U.xlsx'))

# df1=pd.read_excel(os.path.join(dirname,'/Users/admin/Documents/JobSites_U.xlsx'))


# startno=0
# endno=len(df)
# # a = ['Python']

# def Glassdoor(commonfields,URL,startnum,endnum,Domain, result_all, job_titles_strings):
#     dic=commonfields
#     w2_contracts=[]
#     for i in job_titles_strings:
#         for j in range(1,2):
#             # skillname=df.loc[i, 'SkillName'] 
#             url=URL.format(a=i)
#             print("--------------------------")
            
#             print('url:', url)

            
#             driver.get(url)
#             time.sleep(18)

#             # try:
#             #     # Wait for the close button element to be clickable
#             #     close_button = WebDriverWait(driver, 10).until(
#             #         EC.element_to_be_clickable((By.CLASS_NAME, "CloseButton"))
#             #     )
#             #     # Click on the close button to close the sign-in page
#             #     close_button.click()
#             #     print("Sign-in page closed.")
#             # except Exception as e:
#             #     print("Error while closing sign-in page:", e)

#             # time.sleep(5)
            


#             # time.sleep(5)
#             # print(driver.page_source)
            
#             # html = requests.get(url, verify=True).text
#             # soup = BeautifulSoup(html,'html.parser')



#             # try:
#             #     job_elem = driver.find_element(By.CSS_SELECTOR, ".SearchResultsHeader_searchResultsHeader__uK15O h1.SearchResultsHeader_jobCount__eHngv").text
                
#             #     # Check if the text inside job_elem is '0'
#             #     if '0' in job_elem:
#             #         print("No results found")
#             #         # Print the text inside the h1 element if no job elements are found
#             #         error_message = driver.find_element(By.CSS_SELECTOR, ".ErrorPage_errorPage__5lJBV .ErrorPage_errorPageTitle__XtznY").text
#             #         print("Error Message:", error_message)
#             #     else:
#             #         job_elem = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardContainer___hKKI")
#             #         print("Job Elements:", len(job_elem))
#             # except:
#             #     print("No job elements found")


#             # try:           
#             #     job_elem = driver.find_element(By.CSS_SELECTOR, ".SearchResultsHeader_searchResultsHeader__uK15O h1.SearchResultsHeader_jobCount__eHngv").text
                
#             #     # Extract the text from the element
#             #         # job_count_text = job_elem.text
#             #         # print("Job Count:", job_count_text)
                    
#             #     if '0' not in job_elem:
#             #             job_elem = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardContainer___hKKI")
#             #             button_clicked = True

#             #             # Continue the loop until the button is no longer clickable
#             #             while button_clicked:
#             #                 try:
#             #                     # Locate the "Show more jobs" button
#             #                     show_more_button = WebDriverWait(driver, 10).until(
#             #                         EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="load-more"]'))
#             #                     )
#             #                     # Click the button to load more jobs
#             #                     show_more_button.click()
#             #                     print("Clicked 'Show more jobs' button.")
#             #                 except:
#             #                     # If the button is not clickable, set the variable to False to exit the loop
#             #                     button_clicked = False

#             #             print("Job Elements:", len(job_elem))
#             #     else:
#             #         print("No Job Elements..")
#             #         break
#             # except:
#             #     # error_message = driver.find_element(By.CLASS_NAME, "ErrorPage_errorPageContent__Pgl8_").text
#             #     print("No Results Found  ") 




#             try:           
#                 job_elem = driver.find_element(By.CSS_SELECTOR, ".SearchResultsHeader_searchResultsHeader__uK15O h1.SearchResultsHeader_jobCount__eHngv").text
                
#                 # Extract the text from the element
#                     # job_count_text = job_elem.text
#                     # print("Job Count:", job_count_text)
                    
#                 if '0' not in job_elem:
#                         job_elem = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardContainer___hKKI")

#                         print("Job Elements:", len(job_elem))
#                 else:
#                     print("No Job Elements..")
#                     break

#                 # <div class="ErrorPage_errorPageContent__Pgl8_"><h1 class="ErrorPage_errorPageTitle__XtznY">No results found</h1>
#             except:
#                 # error_message = driver.find_element(By.CLASS_NAME, "ErrorPage_errorPageContent__Pgl8_").text
#                 print("No Results Found  ")



            
            
#             # break

#             # elif driver.find_element(By.CLASS_NAME, "ErrorPage_errorPageTitle__XtznY").text :
#             #     print("No Job elements..")
#             #     break
    

            


#             # job_elem= driver.find_elements(By.CLASS_NAME, "JobCard_jobCardWrapper__lyvNS")
#             # job_elem= driver.find_elements(By.CLASS_NAME, "jobCard ")
#             # job_elem= driver.find_elements(By.CLASS_NAME, "JobsList_jobListItem__wjTHv")
#             # job_elem= driver.find_elements(By.CLASS_NAME, "JobCard_jobTitle___7I6y") 
#             # job_elem= driver.find_elements(By.CLASS_NAME, "EmployerProfile_profileContainer__VjVBX EmployerProfile_compact__nP9vu")  #0
#             # driver.quit()
#             # print(list(job_elem))
#             # links=[]
#             time.sleep(2)

#             for e in job_elem:
#                     try :
#                 # try :
#                         driver.implicitly_wait(4)
#                         a_element = e.find_element(By.TAG_NAME, 'a')

#                         # Retrieve the href attribute
#                         link = a_element.get_attribute('href')
#                         print("link: ", link)
#                         # dic['job_source'].append(link)
#                         # dic['source'].append("Glassdoor")
#                         # print(type(jd_link))
#                         # print("Job Link:", link)
#                         # links.append(link)
            
#                         # Retrieve the text within the <a> tag
#                         role = a_element.text.strip()
#                         # print("Job Role:", role)
#                         link =str(link)
#                         if (link,) not in result_all:
#                             company_elem = e.find_element(By.CLASS_NAME, "EmployerProfile_compactEmployerName__LE242")
#                             company = company_elem.text
#                             print("Company:" , company) 
#                             # dic['vendor'].append(company)

#                             location = e.find_element(By.CLASS_NAME,"JobCard_location__rCz3x").text 
#                             print("Location:",location)
#                             # dic['job_location'].append(location)

#                             # wait = WebDriverWait(driver, 10)
#                                                 # time.sleep(5)
#                             try:
#                                 salary_element = e.find_element(By.CLASS_NAME, "JobCard_salaryEstimate__arV5J")
#                                 if salary_element:
#                                     job_salary = salary_element.text 
                                    
#                                     # Check if "Per Hour" is present in the salary text
#                                     if "Per hour" in job_salary:
#                                         print("Job Salary:", job_salary)
#                                         # dic['job_salary'].append(job_salary)
#                                     else:
#                                         # Proceed to the next job element if salary is not per hour
#                                         continue

#                                 else:
#                                     print("Salary Element Not Fetched")
#                             except:
#                                 print("No Salary Element")

#                             posted_on_element =e.find_element(By.CLASS_NAME, "JobCard_listingAge__Ny_nG")
#                             posted_on = posted_on_element.text
                                                        
#                             # Get the current date
#                             current_date = today_cst

#                             if posted_on == '24h':
#                                 # If posted_on is '24h', assign today's date
#                                 posted_on= current_date.strftime("%Y-%m-%d")
#                             # elif posted_on.endswith('d'):
#                             #     # If posted_on ends with 'd' (e.g., '1d', '2d', etc.), extract the number of days and subtract from today's date
#                             #     days_ago = int(posted_on[:-1])  # Extract the number of days
#                             #     posting_date = current_date - timedelta(days=days_ago)
#                             #     posted_on= posting_date.strftime("%Y-%m-%d")
#                             # else:
#                             #     # Handle other cases here (e.g., for '1w' - 1 week)
#                             #     # Add more conditions as needed
#                             #     return None  # Return None if the 'posted_on' value is not recognized
                            

#                                 # dic['posted_on'].append(posted_on)
#                             try:
#                                                 # Extract skills information
#                                 skills_element = e.find_element(By.CLASS_NAME, "JobCard_jobDescriptionSnippet__yWW8q")
#                                 skills_text = skills_element.text.strip()
#                                 skills = re.search(r'Skills:\s*(.*)', skills_text).group(1)
#                                 print("Skills:", skills)
#                                 dic['job_skills'].append(skills)
#                             except:
#                                 print("No Skills Found.")

#                             print("---------------------------")
#                             wait = WebDriverWait(driver, 10)
#                             headers = {
#                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
#                                     }
#                             # headers = {
#                             #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0"
#                             # }

#                             response = requests.get(link, headers=headers)
#                             # print(response.status_code)
#                             # break

#                             #     # Check if the request was successful
#                             if response.status_code == 200:
#                                 html_content = response.text
#                                 soup = BeautifulSoup(html_content, 'html.parser')
#                                 # print(soup.text)
#                                 # break
                                    
#                                 job_description_element = soup.find('div', class_='JobDetails_jobDescription__uW_fK')
                                                                
#                                 if job_description_element:
#                                         # Extract the text from the job description div
#                                         job_description = job_description_element.get_text(separator='\n', strip=True)
#                                         print("Job Description:", job_description)
#                                         #print(job_description)
#                                 else:
#                                         job_description = " "

#                             if 'Full-time' and 'year' and 'w2' not in job_description.lower() :
#                                 if "W2" not in role:
#                                     #print("----------:",  job_details.text)                   
#                                     dic['Employment_type'].append("Contract")
#                                     dic['category_skill'].append(str(i).replace("%20", " "))
#                                     dic['job_description'].append(job_description)
#                                     dic['job_title'].append(role)
#                                     dic['vendor'].append(company)
                                    
#                                     dic['job_location'].append(location)
#                                     dic['posted_on'].append(today_cst.strip())
#                                     dic['job_source'].append(link)
#                                     dic['source'].append("Glassdoor") 
#                             else:
#                                 w2_contracts.append({
#                                     'job_title': role,
#                                     'vendor': company,
#                                     'job_location': location,
#                                     'posted_on': today_cst.strip(),
#                                     'Employment_type': "Contract",
#                                     'job_source': link,
#                                     'source' :'Glassdoor',
#                                     'category_skill': str(i).replace("%20", " ")
#                                 }) 
#                         else:
#                             print("Job Already in Database...")
#                     except :
#                         continue

#     for r in range(len(dic['job_title'])):
#         dic['job_country'].append('United States')
    
            
        
#     glassdoor=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dic.items() ]))
#     print('no. of jobs in Glassdoor: %s', len(glassdoor)) 
#     logging.info('no. of jobs in Glassdoor: %s', len(glassdoor))
#     # Register the release function to be called on script exit
#     mydb.close()
#     # mycursor.close()
    
#     return(glassdoor, w2_contracts)

# atexit.register(release_chromedriver)
            


                
#                 # except :
#                 #     continue
                    
               
             
                
#     # for r in range(len(job['job_title'])):
#     #     job['job_country'].append('United States')
#         #job['job_source'].append('Judge')
                    
#     # print("len(job['job_title']),len(job['vendor']),len(job['job_location']),len(job['posted_on']),len(job['Employment_type']) len,(job['posted_on_element']),len(job['job_salary']),len(job['job_description'])")
    
#     glassdoor=pd.DataFrame(dict([(k,pd.Series(dic[k])) for k in dic])) 
    
#     #logging.info('no. of jobs in resumelibrary: %s', len(Careerjet))
    
#     return(glassdoor)


# glassdoor=Glassdoor(Commonfields(), df, df1.loc[45, 'ContractURL'], startno, endno,1,2)
# print(glassdoor)



# for link in glassdoor['job_source']:
#     # print([link])
#     driver.get(link)
#     time.sleep(3)
#                                 # Find the "See more" button
#     see_more_button = driver.find_element(By.XPATH, "//button[contains(@class, 'JobDetails_showMore___Le6L')]")

#     # Click the "See more" button
#     see_more_button.click()
#     time.sleep(2)


#     # Wait for the job description to expand
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'JobDetails_showMoreWrapper__ja2_y')))

#     # Find the <div> element with the job description
#     job_description_div = driver.find_element(By.CLASS_NAME, 'JobDetails_jobDescription__uW_fK')

#     # Extract the text content of the <div> element
#     job_description = job_description_div.text
#     if 'w2' and 'Full-Time' and 'year' not in job_description.lower():
#         print("Job Description:", job_description)
#         glassdoor.loc[glassdoor.index[-1], 'job_description'] = job_description
#     else:
#         print("It's a W2 position")
#     # print("Job Description:", job_description)
#     print("---------------------------")
#     time.sleep(3)
# # dataframe=glassdoor


# output_dir = '/Users/admin/Documents/'

# # Create the directory if it doesn't exist
# os.makedirs(output_dir, exist_ok=True)
# # import time
# # time = datetime.now().strftime('%H-%M-%S') 
# # Specify the path to the Excel file within the created directory
# excel_file_path = os.path.join(output_dir, f'data(glassdoor)-{today_date}.xlsx')

# # Write the DataFrame to an Excel file in the created directory
# glassdoor.to_excel(excel_file_path, index=False)

# print(f"Excel file saved at: {excel_file_path}")






# dataframes=[Glassdoor]
# # print(dataframes)

# data = pd.DataFrame(Commonfields())
# # print(data)

# for glassdoor in dataframes:
#     data = pd.concat([data, pd.DataFrame(glassdoor.__dict__)], ignore_index=True)
# data=data.drop_duplicates()
# print(data)




#____________________________________________________________________________________________________________________________________________________










# from bs4 import BeautifulSoup
# import pandas as pd
# import requests
# import logging
# import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import atexit
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# import os
# import spacy
# import requests
# import pymysql
# import pytz
# import datetime
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.keys import Keys
# from datetime import datetime, timedelta
# from Commonfields import Commonfields
# from proxy_servers_list import servers_list
# import random
# # Get today's date
# today_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

# # print(today_date)

# mydb = pymysql.connect(
 
#   host="localhost",
#   user=		"root",
#   password=	"Nadmin123$",
#   database=	"narvee_hr"
# )

# def release_chromedriver():
#     try:
#         # Close the ChromeDriver session
        
#         driver.quit()
#         print("ChromeDriver released successfully.")
#     except Exception as e:
#         print(f"Error releasing ChromeDriver: {e}")

# # Define CST TimeZone

# # Define CST timezone
# cst_timezone = pytz.timezone('America/Chicago')

# now_cst = datetime.now().astimezone(cst_timezone)
# today_cst = now_cst.strftime('%Y-%m-%d %H:%M:%S')

# yesterday_cst = now_cst - timedelta(days=1)
# yesterday_cst = yesterday_cst.replace(hour=0, minute=0, second=0)
# yesterday_cst_str = yesterday_cst.strftime('%Y-%m-%d %H:%M:%S')



# # Function to check if job already exists
# def job_exists(vendor, job_title, job_location):
#     select_query = f"SELECT vendor, job_title, job_location FROM tbl_rec_requirement WHERE vendor = %s AND job_title = %s AND job_location = %s AND posted_on >= %s AND posted_on <= %s"
#     mycursor.execute(select_query, (vendor, job_title, job_location, yesterday_cst_str, today_cst))
#     if mycursor.fetchone():
#         return True
#     return False

# # mycursor=mydb.cursor
# mycursor = mydb.cursor()
# nlp = spacy.load('en_core_web_sm')

# from DataCleaning import extract_skills

# driver = webdriver.Chrome()
# # Maximize the browser window
# driver.maximize_window()

# driver.get("https://www.glassdoor.co.in/Community/index.htm")
# time.sleep(5)
# # Find the email input field by ID and enter your email address
# # email_input = driver.find_element_by_id("inlineUserEmail")
# email_input = driver.find_element(By.ID, "inlineUserEmail")  # Corrected line
# email = "rumina4122@gmail.com"
# email_input.send_keys(email)
# time.sleep(2)
# #Wait for the "Continue with email" button to be clickable
# continue_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[@data-test='email-form-button']"))
# )

# # Click the "Continue with email" button
# continue_button.click()


# # Wait for the page to load completely
# # WebDriverWait(driver, 10).until(EC.title_contains("Glassdoor"))
# time.sleep(5)

# # Find the "Jobs" link and click it
# jobs_link = driver.find_element(By.XPATH, "//a[@href='/Job/index.htm']")
# jobs_link.click()

# time.sleep(4)


# time.sleep(2)

# location_input = driver.find_element(By.ID, "searchBar-location")
# # Clear any existing text in the location input field
# location_input.clear()
# time.sleep(2)



# # Enter the location "United States"
# location_input.send_keys("United States")
# location_input.send_keys(Keys.RETURN)
# time.sleep(6)
#  # Find and click the button to open the filter menu


# # job_titles_strings = ['Python%20Developer', 'Java%20Developer', 'Angular%20Developer', ".Net%20Developer"]
# def Glassdoor(commonfields,result_all, job_titles_strings): # job_titles_strings):
#     dic=commonfields
#     w2_contracts=[]
#     with requests.Session() as session:
#      for i in job_titles_strings:
#       for j in range(1,2):
#     # try:
#         # Find the search input field by ID
#         search_input = driver.find_element(By.ID, "searchBar-jobTitle")

#         # Use JavaScript to clear the value of the search field
#         driver.execute_script("arguments[0].value = '';", search_input)
#         # search_input.clear()
#                 # Find the search input field by class name
#         # search_input = driver.find_element(By.CLASS_NAME, "Autocomplete_autocompleteInput__Ngcdi")

#         # Clear the search input field
#         search_input.clear()

#         # search_input.send_keys(Keys.RETURN)
        


#         # Update the placeholder attribute to change the displayed text
#         # driver.execute_script("arguments[0].setAttribute('placeholder', 'Find your perfect job and search for job postings')", search_input)
#         # time.sleep(2)
#         # Clear the search input field
#         time.sleep(2)
#         search_input = driver.find_element(By.ID, "searchBar-jobTitle")


#         # Enter the search string
#         search_input.send_keys(i.replace("%20", " "))
#         search_input.send_keys(Keys.RETURN)
#         time.sleep(5)

                        
        

#         # Wait for the page to load completely (optional)
#         # 
#         # Add a suitable wait here if needed to ensure the page is fully loaded

        
#         # Find and click the button to open the filter menu
#         try:
#             filter_button = driver.find_element(By.XPATH, "//button[@data-test='expand-filters']")
#             filter_button.click()

#             time.sleep(5)
#                     # Find the toggle switch by data-test attribute
#             toggle_switch = driver.find_element(By.CSS_SELECTOR, '[data-test="remoteWorkType"]')

#             # Click on the toggle switch
#             toggle_switch.click()
#             time.sleep(2)

#             # Wait for the filter menu to expand (optional)
#             # Add a suitable wait here if needed to ensure the filter menu is fully expanded

#             # Find and click on the button for date posted
#             date_posted_button = driver.find_element(By.XPATH, "//button[@data-test='fromAge']")
#             date_posted_button.click()
#             time.sleep(2)

#             # Wait for the options to appear in the dropdown (optional)
#             # Add a suitable wait here if needed to ensure the options are fully loaded

#             # Locate and select the "Last day" option from the dropdown
#             last_day_option = driver.find_element(By.XPATH, "//li/button[contains(., 'Last day')]")
#             last_day_option.click()
#             time.sleep(2)

#             # Find and click the button to expand the job types filter
#             button = driver.find_element(By.CLASS_NAME, "SearchFiltersBar_pillRight__2aWS4")

#             # Click the button
#             button.click()
#             # job_types_button = driver.find_element(By.XPATH, "//button[@data-test='jobTypeIndeed']")
#             # job_types_button.click()

#             # Wait for the job types filter options to appear (optional)
#             # Add a suitable wait here if needed to ensure the options are fully loaded
#             time.sleep(2)

#             # Locate and click the "Contract" option
#             contract_option = driver.find_element(By.XPATH, "//li/button[contains(., 'Contract')]")
#             contract_option.click()
#             # Find and click the "Apply Filters" button
#             time.sleep(2)

#             apply_filters_button = driver.find_element(By.XPATH, "//button[@data-test='apply-search-filters']")
#             apply_filters_button.click()
#             time.sleep(5)
#         except:
#             print("No filter Options")

#         # print("Current URL  link:", driver.current_url)
#         time.sleep(4)
#         url=driver.current_url
#         print("URL",url)
#         print("---------------------------")


#         try:
#             job_elem = driver.find_element(By.CSS_SELECTOR, ".SearchResultsHeader_searchResultsHeader__uK15O h1.SearchResultsHeader_jobCount__eHngv").text
            
#             # Check if the text inside job_elem is '0'
#             if '0' not in job_elem:
#                 job_elem = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardContainer___hKKI")
#                 print("Job Elements:", len(job_elem))
#                 # Print the text inside the h1 element if no job elements are found
#                 # error_message = driver.find_element(By.CSS_SELECTOR, ".ErrorPage_errorPage__5lJBV .ErrorPage_errorPageTitle__XtznY").text
#                 # print("Error Message:", error_message)
#             else:
#                 print("No results found")
#                 continue

#                 # job_elem = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardContainer___hKKI")
#                 # print("Job Elements:", len(job_elem))
#         except:
#             print("No job elements found")
#             continue
            

#         time.sleep(4)
#         # job_elem

#     # except :
#         # print("Search input field not found")
#         for e in job_elem:
#                     # try :
#                 # try :
#                     # driver.implicitly_wait(4)
#                     a_element = e.find_element(By.TAG_NAME, 'a')
#                     print("---------------------------")


#                     # Retrieve the href attribute
#                     link = a_element.get_attribute('href')
#                     print("link: ", link)
#                     # dic['job_source'].append(link)
#                     # dic['source'].append("Glassdoor")
#                     # print(type(jd_link))
#                     # print("Job Link:", link)
#                     # links.append(link)
        
#                     # Retrieve the text within the <a> tag
#                     role = a_element.text.strip()
#                     # print("Job Role:", role)
#                     link =str(link)
#                     if (link,) not in result_all:
#                         company_elem = e.find_element(By.CLASS_NAME, "EmployerProfile_compactEmployerName__LE242")
#                         company = company_elem.text
#                         print("Company:" , company) 
#                         # dic['vendor'].append(company)

#                         location = e.find_element(By.CLASS_NAME,"JobCard_location__rCz3x").text 
#                         print("Location:",location)
#                         # dic['job_location'].append(location)

#                         # wait = WebDriverWait(driver, 10)
#                                             # time.sleep(5)
#                         # try:
#                         try:
#                             salary_element = e.find_element(By.CLASS_NAME, "JobCard_salaryEstimate__arV5J")

#                             if salary_element:
#                                 job_salary = salary_element.text 
                                
#                                 # Check if "Per Hour" is present in the salary text
#                                 if "Per hour" in job_salary:
#                                     print("Job Salary:", job_salary)
#                                     # dic['job_salary'].append(job_salary)
#                                 else:
#                                     # Proceed to the next job element if salary is not per hour
#                                     print("Salary Not in Hours")
#                                     continue
#                         except:
#                             print("No salary Element")

                            
#                         # except:
#                         #     print("No Salary Element")

#                         posted_on_element =e.find_element(By.CLASS_NAME, "JobCard_listingAge__Ny_nG")
#                         posted_on = posted_on_element.text
                                                    
#                         # Get the current date
#                         today_cst_datetime = datetime.strptime(today_cst, '%Y-%m-%d %H:%M:%S')

#                         if posted_on == '24h':
#                             # If posted_on is '24h', assign today's date
#                             posted_on= today_cst_datetime
#                             print("Posted On ", posted_on)
#                         else:
#                             continue
#                         # elif posted_on.endswith('d'):
#                         #     # If posted_on ends with 'd' (e.g., '1d', '2d', etc.), extract the number of days and subtract from today's date
#                         #     days_ago = int(posted_on[:-1])  # Extract the number of days
#                         #     posting_date = current_date - timedelta(days=days_ago)
#                         #     posted_on= posting_date.strftime("%Y-%m-%d")
#                         # else:
#                         #     # Handle other cases here (e.g., for '1w' - 1 week)
#                         #     # Add more conditions as needed
#                         #     return None  # Return None if the 'posted_on' value is not recognized
                        

#                             # dic['posted_on'].append(posted_on)
#                         try:
#                                             # Extract skills information
#                             skills_element = e.find_element(By.CLASS_NAME, "JobCard_jobDescriptionSnippet__yWW8q")
#                             skills_text = skills_element.text.strip()
#                             skills = re.search(r'Skills:\s*(.*)', skills_text).group(1)
#                             print("Skills:", skills)
#                             dic['job_skills'].append(skills)
#                         except:
#                             print("No Skills Found.")

#                         time.sleep(5)

                        

#                         driver.get(link)
#                         print("JobDescription URL:", driver.current_url)
#                         time.sleep(10)
#                         # driver.get(link)
#                         # time.sleep(3)
#                                                     # Find the "See more" button
#                         see_more_button = driver.find_element(By.XPATH, "//button[contains(@class, 'JobDetails_showMore___Le6L')]")

#                         # Click the "See more" button
#                         see_more_button.click()
#                         time.sleep(2)


#                         # Wait for the job description to expand
#                         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'JobDetails_showMoreWrapper__ja2_y')))

#                         # Find the <div> element with the job description
#                         job_description_div = driver.find_element(By.CLASS_NAME, 'JobDetails_jobDescription__uW_fK')

#                         # Extract the text content of the <div> element
#                         job_description = job_description_div.text
#                         # print("Job Description:",job_description)
#                         #  Define the regular expression pattern to match monetary values
#                         monetary_pattern = '[1-9]{2,3},000'

#                         # Search for monetary values in the job description
#                         matches = re.findall(monetary_pattern, job_description) #list
#                         if matches:
#                             a=len(matches[0])
#                         else:
#                             a=0


#                         # Print the extracted monetary values
                        
#                         print("Salary values found:", matches)
#                         print(a)

#                         print("---------------------------")

#                                                     # break


#                         if 'full-time' not in job_description.lower() and 'per year' not in job_description.lower() and 'annual salary' not in job_description.lower() and 'w2' not in job_description.lower():
#     # Your code here

#                         # if "w2" not in role.lower() and len(matches[0]) <= 3:
#                             if "w2" not in role.lower() and (a<=3):
#                                 #print("----------:",  job_details.text)                   
#                                 dic['Employment_type'].append("Contract")
#                                 dic['category_skill'].append(str(i).replace("%20", " "))
#                                 dic['job_description'].append(job_description)
#                                 dic['job_title'].append(role)
#                                 dic['vendor'].append(company)
                                
#                                 dic['job_location'].append(location)
#                                 dic['posted_on'].append(today_cst.strip())
#                                 dic['job_source'].append(link)
#                                 dic['source'].append("Glassdoor") 
#                             else:
#                                 w2_contracts.append({
#                                 'job_title': role,
#                                 'vendor': company,
#                                 'job_location': location,
#                                 'posted_on': today_cst.strip(),
#                                 'Employment_type': "Contract",
#                                 'job_source': link,
#                                 'source' :'Glassdoor',
#                                 'category_skill': str(i).replace("%20", " ")
#                                 }) 

                       
#                     else:
#                         print("Job Already in Database...")
#                 # except :
#                     #     continue

#     for r in range(len(dic['job_title'])):
#         dic['job_country'].append('United States')
     
#     glassdoor=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dic.items() ]))
#     print('no. of jobs in Glassdoor: %s', len(glassdoor)) 
#     logging.info('no. of jobs in Glassdoor: %s', len(glassdoor))
#     # Register the release function to be called on script exit
#     mydb.close()
#     mycursor.close()

#     return(glassdoor, w2_contracts)

# atexit.register(release_chromedriver) 







# ---------------------------------------------------------




# # glassdoor=pd.DataFrame()

# # logging.info("Glassdoor Started..")
# glassdoor=Glassdoor(Commonfields(), job_titles_strings)
# print(glassdoor)
# atexit.register(release_chromedriver)








# # Retrieve the current URL after clicking the link
# current_url = driver.current_url

# # Print or use the URL as needed
# print("Current URL after clicking Java Developer jobs link:", current_url)

# print(jobs_link)

# # Wait for the page to load completely
# WebDriverWait(driver, 10).until(EC.title_contains("Job Search"))

# # Find the search input field by ID
# search_input = driver.find_element_by_id("searchBar-jobTitle")

# # Clear any existing text in the search input field
# search_input.clear()

# # Enter your desired search string
# search_string = "java developer"
# search_input.send_keys(search_string)

# # Press Enter to submit the search
# search_input.send_keys(Keys.RETURN)

# # Print the URL after the search
# print("Current URL after search:", driver.current_url)






#=======================================================================================================






from bs4 import BeautifulSoup
import pandas as pd
import requests
import logging
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import atexit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import os
import spacy
import requests
import pymysql
import pytz
import datetime
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from Commonfields import Commonfields
from proxy_servers_list import servers_list
import random
from selenium.webdriver.chrome.options import Options

# Get today's date
today_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

# print(today_date)

mydb = pymysql.connect(
 
  host="localhost",
  user=		"root",
  password=	"Nadmin123$",
  database=	"narvee_hr"
)

def release_chromedriver():
    try:
        # Close the ChromeDriver session
        
        driver.quit()
        print("ChromeDriver released successfully.")
    except Exception as e:
        print(f"Error releasing ChromeDriver: {e}")

# Define CST TimeZone

# Define CST timezone
cst_timezone = pytz.timezone('America/Chicago')

now_cst = datetime.now().astimezone(cst_timezone)
today_cst = now_cst.strftime('%Y-%m-%d %H:%M:%S')

yesterday_cst = now_cst - timedelta(days=1)
yesterday_cst = yesterday_cst.replace(hour=0, minute=0, second=0)
yesterday_cst_str = yesterday_cst.strftime('%Y-%m-%d %H:%M:%S')



#dirname = os.path.dirname('__file__')
dirname = os.path.dirname(os.path.abspath(__file__))

# mycursor=mydb.cursor
mycursor = mydb.cursor()
nlp = spacy.load('en_core_web_sm')

from DataCleaning import extract_skills
# chrome_options = Options()
# chrome_options.add_argument('--incognito')  # Enable incognito mode
# Initialize the WebDriver with these options
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()

driver.get("https://www.glassdoor.co.in/Community/index.htm")
time.sleep(5)
# Find the email input field by ID and enter your email address
# email_input = driver.find_element_by_id("inlineUserEmail")
email_input = driver.find_element(By.ID, "inlineUserEmail")  # Corrected line
email = "rumina4122@gmail.com"
email_input.send_keys(email)
time.sleep(2)
#Wait for the "Continue with email" button to be clickable
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-test='email-form-button']"))
)

# Click the "Continue with email" button
continue_button.click()


# Wait for the page to load completely
# WebDriverWait(driver, 10).until(EC.title_contains("Glassdoor"))
time.sleep(5)

# Find the "Jobs" link and click it
jobs_link = driver.find_element(By.XPATH, "//a[@href='/Job/index.htm']")
jobs_link.click()

time.sleep(4)


location_input = driver.find_element(By.ID, "searchBar-location")
# Clear any existing text in the location input field
location_input.clear()
time.sleep(2)



# Enter the location "United States"
location_input.send_keys("United States")
location_input.send_keys(Keys.RETURN)
time.sleep(6)
# url="https://www.glassdoor.co.in/Job/united-states-python-developer-jobs-SRCH_IL.0,13_IN1_KO14,30.htm?jobTypeIndeed=NJXCK&fromAge=1&remoteWorkType=1"
# driver.get(url)
# time.sleep(4)

## Job Sites Excel
df1= pd.read_excel(os.path.join(dirname,'/Users/admin/Documents/JobSites1.xlsx'))

# job_titles_strings=['Python%20Developer','Angular%20Developer', "Java%20Developer"]

def Glassdoor(commonfields, result_all, job_titles_strings):
    job = commonfields
    w2_contracts = []
  
    #unique_job_ids = set()
    for i in job_titles_strings:#range(startnum, endnum) job_titles_strings
        for j in range(1, 2):
            
                # Find the search input field by ID
                search_input = driver.find_element(By.ID, "searchBar-jobTitle")

                # Use JavaScript to clear the value of the search field
                driver.execute_script("arguments[0].value = '';", search_input)
                # Clear the search input field
                search_input.clear()
                # Clear the search input field
                time.sleep(2)
                search_input = driver.find_element(By.ID, "searchBar-jobTitle")
                # Enter the search string
                if ".Net" not in i:
                    search_input.send_keys(i.replace("%20", " "))
                    search_input.send_keys(Keys.RETURN)
                    time.sleep(5)
                
                    # Find and click the button to open the filter menu
                    try:
                        filter_button = driver.find_element(By.XPATH, "//button[@data-test='expand-filters']")
                        filter_button.click()

                        # time.sleep(5)
                                # Find the toggle switch by data-test attribute
                        # toggle_switch = driver.find_element(By.CSS_SELECTOR, '[data-test="remoteWorkType"]')

                        # Click on the toggle switch
                        # toggle_switch.click()
                        time.sleep(2)

                        # Wait for the filter menu to expand (optional)
                        # Add a suitable wait here if needed to ensure the filter menu is fully expanded

                        # Find and click on the button for date posted
                        date_posted_button = driver.find_element(By.XPATH, "//button[@data-test='fromAge']")
                        date_posted_button.click()
                        time.sleep(2)

                        # Wait for the options to appear in the dropdown (optional)
                        # Add a suitable wait here if needed to ensure the options are fully loaded

                        # Locate and select the "Last day" option from the dropdown
                        last_day_option = driver.find_element(By.XPATH, "//li/button[contains(., 'Last day')]")

                        #Last 3 Days
                        # last_day_option = driver.find_element(By.XPATH, "//li/button[contains(., 'Last 3 days')]")

                        last_day_option.click()
                        time.sleep(2)

                        # Find and click the button to expand the job types filter
                        button = driver.find_element(By.CLASS_NAME, "SearchFiltersBar_pillRight__2aWS4")

                        # Click the button
                        button.click()
                        # job_types_button = driver.find_element(By.XPATH, "//button[@data-test='jobTypeIndeed']")
                        # job_types_button.click()

                        # Wait for the job types filter options to appear (optional)
                        # Add a suitable wait here if needed to ensure the options are fully loaded
                        time.sleep(2)

                        # Locate and click the "Contract" option
                        contract_option = driver.find_element(By.XPATH, "//li/button[contains(., 'Contract')]")
                        contract_option.click()
                        # Find and click the "Apply Filters" button
                        time.sleep(2)

                        apply_filters_button = driver.find_element(By.XPATH, "//button[@data-test='apply-search-filters']")
                        apply_filters_button.click()
                        time.sleep(5)
            
                    except:
                         print("No filter Options")

                    # print("Current URL  link:", driver.current_url)
                    # time.sleep(4)
                    url=driver.current_url
                    # print("---------------------------")

                

                    print('Glassdoor url-----:' ,driver.current_url)
                    

                    
                    driver.get(url)
                    time.sleep(5)

                    html_content = driver.page_source
                    soup = BeautifulSoup(html_content, 'html.parser')
                    time.sleep(5)
                    # print(soup)
                    # try:
                    no_of_jobs=soup.find('h1', class_="SearchResultsHeader_jobCount__eHngv")
                    print("Type of No_of_jobs...", type(no_of_jobs))
                    time.sleep(5)
                    if no_of_jobs is not None and '0' not in no_of_jobs.text:
                        time.sleep(2)
                        job_elem = soup.find('div', class_="JobsList_wrapper__EyUF6")
                        job_elems=job_elem.find_all('div', class_="JobCard_jobCardContainer___hKKI")
                        print("No of Job Elements:========================", len(job_elems))
                        print("---------------------------")
                        time.sleep(2)



                        for e in job_elems:
                            time.sleep(4)

                                # Fetch title and href attributes
                            role = e.find('a', class_="JobCard_jobTitle___7I6y").text
                            link = e.find('a', class_="JobCard_jobTitle___7I6y")['href']
                            
                            # Print title and href attributes
                            print("Job Role:----", role)
                            time.sleep(4)
                            
                            print("link---: ", link)
                            location=e.find('div', class_="JobCard_location__rCz3x").text.strip()
                            # print("Location:----", location)

                            company_elem = e.find('span', class_="EmployerProfile_compactEmployerName__LE242")
                            company = company_elem.text.strip()
                            print("Company:" , company) 
                            # salary_element=e.find('div', class_='JobCard_salaryEstimate__arV5J')
                                        # Fetch salary information
                            
                            # try:
                            #     salary_elem = e.find('div', class_="JobCard_salaryEstimate__arV5J").text.strip()
                            #     # Check if "Per Hour" is present in the salary text
                            #     if "Per hour" in salary_elem:
                            #         print("Job Salary:", salary_elem)
                            #         # dic['job_salary'].append(job_salary)
                            #     else:
                            #         # Proceed to the next job element if salary is not per hour
                            #         print("Salary not in Hours")
                            #         continue
                                    
                            # except:
                            #         print("No Salary Element")

                            posted_on_element = e.find('div', class_="JobCard_listingAge__Ny_nG")
                            posted_on = posted_on_element.text.strip()
                            if posted_on == '24h':
                                print("Posted On:---", now_cst.strftime('%Y-%m-%d %H:%M:%S'))
                            elif posted_on.endswith('d'):
                                days_ago = int(posted_on[:-1])
                                posted_date = now_cst - timedelta(days=days_ago)
                                print("Posted On:", posted_date.strftime('%Y-%m-%d %H:%M:%S'))
                    

                           


                            # try:
                            #             # Extract skills information
                            #     skills_element = e.find('div', class_="JobCard_jobDescriptionSnippet__yWW8q")
                            #     skills_text = skills_element.text.strip()
                            #     skills = re.search(r'Skills:\s*(.*)', skills_text).group(1)
                            #     print("Skills:", skills)
                                
                            # except:
                            #     print("No Skills Found.")

                            if (link, ) not in result_all:
                                # print("Job Not in Our Database.....", link)

                                driver.get(link)
                                print("JobDescription URL:", driver.current_url)
                                time.sleep(5)
                                # driver.get(link)
                                # time.sleep(3)
                                
                                #                             # Find the "See more" button
                                # see_more_button = driver.find_element(By.XPATH, "//button[contains(@class, 'JobDetails_showMore___Le6L')]")

                                # # Click the "See more" button
                                # see_more_button.click()
                                time.sleep(5)


                                # Wait for the job description to expand
                                # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'JobDetails_showMoreWrapper__ja2_y')))
                                time.sleep(3)

                                # Find the <div> element with the job description
                                try:
                                    job_description_div = driver.find_element(By.CLASS_NAME, 'JobDetails_jobDescription__uW_fK')
                            
                                    time.sleep(2)
                                    # Extract the text content of the <div> element
                                    job_description = job_description_div.text
                                    time.sleep(2)

                                except:
                                    job_description_div= driver.find_element(By.CLASS_NAME, 'JobDetails_jobDetailsSection__y_xa6')
                                    time.sleep(2)
                                    # Extract the text content of the <div> element
                                    job_description = job_description_div.text
                                    time.sleep(2)
 
                                # print("Job Description:",job_description)
                                # Define the regular expression pattern to match monetary values
                                try:
                                    monetary_pattern = '[1-9]{2,3},000'

                                    # Search for monetary values in the job description
                                    matches = re.findall(monetary_pattern, job_description) #list
                                    if matches:
                                        a=len(matches[0])
                                    else:
                                        a=0
                                    # Print the extracted monetary values 
                                    # print("Salary values found:", matches)
                                    print(a)
                                except:
                                    print("No Monetary Pattern")

                                print("---------------------------")


                                if 'full-time' not in job_description.lower() and 'per year' not in job_description.lower() and 'annual salary' not in job_description.lower() and 'w2' not in job_description.lower():
                                    if "w2" not in role.lower()and (a<=3):
                                        #print("----------:",  job_details.text)                   
                                        job['Employment_type'].append("Contract")
                                        job['category_skill'].append(str(i).replace("%20", " "))
                                        job['job_description'].append(job_description)
                                        job['job_title'].append(role)
                                        job['vendor'].append(company)
                                        
                                        job['job_location'].append(location)
                                        job['posted_on'].append(today_cst.strip())
                                        job['job_source'].append(link)
                                        job['source'].append("Glassdoor")
                                        # print("Job Added in Our Database.........") 
                                    else:
                                        w2_contracts.append({
                                        'job_title': role,
                                        'vendor': company,
                                        'job_location': location,
                                        'posted_on': today_cst.strip(),
                                        'Employment_type': "Contract",
                                        'job_source': link,
                                        'source' :'Glassdoor',
                                        'category_skill': str(i).replace("%20", " ")
                                        }) 

                            
                            else:
                                print("Job Already in Database...")



                                    # headers = {
                                    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
                                    # }
                                    # # response = requests.get(link, headers=headers)
                                    # # Use the session object to send requests
                                    #                         # Use the session object to send requests
                                    # response = session.get(url, headers=headers)
                                    # print("Response status code:", response.status_code)

                                    # #     # Check if the request was successful
                                    # if response.status_code == 200:
                                    #     html_content1 = response.text
                                    #     soup1 = BeautifulSoup(html_content1, 'html.parser')
                                    #     # print(soup.text)
                                    #     # break
                                            
                                    #     job_description_element = soup1.find('div', class_='JobDetails_jobDescription__uW_fK')
                                                                        
                                    #     if job_description_element:
                                    #             # Extract the text from the job description div
                                    #             job_description = job_description_element.get_text(separator='\n', strip=True)
                                    #             print("Job Description:", job_description)
                                    #             #print(job_description)
                                    #     else:
                                    #             job_description = " "
                                print("===========================")
                    else:
                        print("No Job Elements Found.....")


                else:
                   print("No skill ")

    for r in range(len(job['job_title'])):
        job['job_country'].append('United States')
     
    glassdoor=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in job.items() ]))
    print('no. of jobs in Glassdoor: %s', len(glassdoor)) 
    logging.info('no. of jobs in Glassdoor: %s', len(glassdoor))
    # Register the release function to be called on script exit
    mydb.close()
    mycursor.close()

    return(glassdoor, w2_contracts)

atexit.register(release_chromedriver) 

    # glassdoor=pd.DataFrame(dict([(k,pd.Series(job[k])) for k in job])) 
    
    # return glassdoor
    # print(dice)


# glassdoor=Glassdoor(Commonfields(), job_titles_strings)
# print(glassdoor)



# dataframes=[glassdoor]

# data = pd.DataFrame(Commonfields())

# for dice in dataframes:
#     data = pd.concat([data, pd.DataFrame(dice.__dict__)], ignore_index=True)
# data=data.drop_duplicates()





# output_dir = '/Users/admin/Documents/'

# # Create the directory if it doesn't exist
# os.makedirs(output_dir, exist_ok=True)
# # import time
# time = datetime.now().strftime('%H-%M-%S') 
# # Specify the path to the Excel file within the created directory
# excel_file_path = os.path.join(output_dir, f'data(dice)-{today_cst}.xlsx')

# # Write the DataFrame to an Excel file in the created directory
# glassdoor.to_excel(excel_file_path, index=False)

# print(f"Excel file saved at: {excel_file_path}")






# Glassdoor(Commonfields(),  job_titles_strings)
    
   

            
    





















