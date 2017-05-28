#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import csv
from collections import Counter

def run_quickstart():
    # [START language_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import language

    # Instantiates a client
    language_client = language.Client()

    f = open('data/170528_Comments.csv','r')
    csvReader = csv.reader(f)
    new_rows_list = []

    for row in csvReader:

        # print('Text: {}'.format(text))
        # print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


        if "_" not in row[0]:
            if len(row[1].split()) <4 :
                continue
        #if row[0]=='comment: ':
            text = row[1]
            try:
                document = language_client.document_from_text(text)
                # Detects the sentiment of the text
                sentiment = document.analyze_sentiment().sentiment
                new_row = [row[0], row[1], sentiment.score, sentiment.magnitude]
            except Exception:
                print ('error')
            # print (text)
            # print (new_row)
        else:
            try:
                new_row = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]]
            except Exception:
                pass
        new_rows_list.append(new_row)
    f.close()

    f2 = open('data/result_0528.csv','w', newline='')
    writer = csv.writer(f2)
    writer.writerows(new_rows_list)
    # output = csv.DictWriter(f2, delimiter=',', lineterminator='\n')
    # output.writerows(new_rows_list)
    f2.close()

if __name__ == '__main__':
    run_quickstart()
