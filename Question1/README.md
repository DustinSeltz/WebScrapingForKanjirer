# README file of Question 1

## Question

What are the most common characters, and information about them such as: frequency of use, meanings, readings, number of strokes, radicals, and difficulty level.

## Strategy

1. Scrape the frequently used Kanjis (from Wikipedia, which source is a file released by the Cultural Agency of Japanese Government, so that is reliable)
2. For each frequently-used Kanji, make a query to [Jisho](jisho.org), an online English-Japanese dictionary. Scrape the related information (number of strokes, readings, meanings, etc.) in the website.
3. For each frequently-used Kanji, make a query to [WaniKani](wanikani.com), an online Japanese learning website for English speakers. Wanikani assigned individual levels, from 1 (easiest) to 60 (most difficult), to lots of Kanjis. We want to know these levels and combine with the information from Step 2.
4. (Dustin's scraping on that github webpage)
5. (Xudong's scraping on Genki)
6. Combine and clean up the data frames from the previous steps into one csv file.

## List of .py/.ipynb files and their order of running

1. get_kanji_list.ipynb (by Jimmy Wang): Step1: *Scraping the frequently used kanjis*  
2. ...
3. ...
4. ...
5. ...

## Other notes

An notebook *Individual_Kanji_Info_Viewer.ipynb* is provided, written by Jimmy Wang, that can display the comprehensive information of a single kanji in human-read-friendly format.
