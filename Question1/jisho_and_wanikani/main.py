import pandas as pd
from Question1.jisho_and_wanikani.web.jisho import Jisho
from Question1.jisho_and_wanikani.web.wanikani import Wanikani
import time
from Question1.jisho_and_wanikani.func.func import write_csv


def run(web, path, list_length):
    cur = 1
    for cell in web.data:
        print(str(int(cur/list_length * 100)) + '%', cell["kanji"])
        write_csv(cell, path)
        cur += 1
    end = time.time()


if __name__ == '__main__':
    content = pd.read_csv("../kanji_list.csv")
    kanji_list = content["kanji"]
    jisho = Jisho(*kanji_list)
    wanikani = Wanikani(*kanji_list)
    start = time.time()
    wanikani_path = "../wanikani_result.csv"
    run(web=wanikani, path=wanikani_path, list_length=len(kanji_list))
    end = time.time()
    print("time_cost", end - start)





