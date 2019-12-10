# README file of Question 1

## Question

What are the most common characters, and information about them such as: frequency of use, meanings, readings, number of strokes, radicals, and difficulty level.

## Strategy

1. Scrape the frequently used Kanjis (from Wikipedia, which source is a file released by the Cultural Agency of Japanese Government, so that is reliable)
2. For each frequently-used Kanji, make a query to [Jisho](jisho.org), an online English-Japanese dictionary. Scrape the related information (number of strokes, readings, meanings, etc.) in the website.
3. For each frequently-used Kanji, make a query to [WaniKani](wanikani.com), an online Japanese learning website for English speakers. Wanikani assigned individual levels, from 1 (easiest) to 60 (most difficult), to lots of Kanjis. We want to know these levels and combine with the information from Step 2.
4. Students in our school are using a book called *Genki* to learn Japanese. Scraping the Genki levels and combine with info from Step 3.
5. Another github source shows some frequency data on *Aozora Bunko* (online library), newspapers, Twitter, etc. scrape them and combine with Step 4.
6. Combine and clean up the data frames from the previous steps into one csv file.

## List of .py/.ipynb files and their order of running

1. get_kanji_list.ipynb (by Jimmy Wang): Step1: Scraping the frequently used kanjis
2. jisho_and_wanikani/main.py (by Mengdi Wei): Step2: Scrape the dictionary information about each kanji on Jisho; Step3: Scrape Wanikani levels from wanikani
3. Genki.ipynb (by Xudong Guo): Step4: Scrape Genki levels
4. Combine.ipynb (by Xudong Guo): Combine Step2~4 information
5. Scraping Kanji Frequency.ipynb (by Dustin Seltz): Step5: Scrape the github webpage for frequency data
6. CombineFrequencyData.ipynb (by Dustin Seltz): Combine frequency data from Step5 to Xudong's combined data
7. cleanlinks.ipynb (by Xudong Guo): Step6: Clean up the web links in the data, and do some data wrangling
8. (Optional) Individual_Kanji_Info_Viewer.ipynb (by Jimmy Wang): csv data viewer, see notes.

## Other notes

An notebook *Individual_Kanji_Info_Viewer.ipynb* is provided, written by Jimmy Wang, that can display the comprehensive information of a single kanji in human-read-friendly format.
