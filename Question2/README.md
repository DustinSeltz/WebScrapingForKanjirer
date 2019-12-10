# README file of Question 2

## Question

A single kanji character could have various readings when formed into different words. Given a kanji, what words can it form, and what are the readings of this kanji in each of those words?

## Analysis

This question is more likely to be a query, or a function. That means, we send a single kanji as an input, find all words that uses this kanji, and find the meanings of those words. Notice that although it could be done using online approach (that means, do the web scraping/data wrangling after given the kanji), it takes some time if there are tens of words that uses a same kanji, which is frequently happen. However, our clients/users cannot wait that much time.

A better approach is to preprocessing, that making a data frame that saves all of the words in Japanese and related information, and what we need to do later is just locate them in the data frame. This is completely offline thus won't cause that much time. However, saving all of the Japanese words are not too much for our project. Our supervisor agreed that we could scrape only the most frequently used 20K words. (Wikipedia Page: [1-10K]('https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Japanese') [10001 - 20K](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Japanese10001-20000)) After we scraped the 20K words, we made queries to [Jisho](jisho.org) to get their meanings.

## Strategy

1. Scrape the most frequently used 20K word list. 
2. For each word, make one or more queries to [Jisho](jisho.org) to get their readings and meanings.
   1. If the word is not found, skip it.
   2. If the word have multiple readings, scrape all of them until the reply status is 404.
   3. If timed out, send a request again.
3. Write the words, readings and meanings together to a csv file.

## List of .py/.ipynb files and their order of running

1. Wikitionary_Wordlist.ipynb: Scraping the 20K word list. It also contains a demo for online word information scraping.
2. wikiwordlist_reading_scraping.ipynb/.py: The files to scrape the readings and meanings of those 20K words into a csv offline.
3. (Optional) wiki_word_viewer_final.ipynb: A file provided to see the word scraping results.

## Notes

Since the word csv file 'wikiword_table_new.csv' takes extremely long time to scrape, in case you ran the 2nd ipynb file and overwrite the csv file, we provided a copy.