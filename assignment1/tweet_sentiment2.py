import json
import sys

twitterfile=open('output.txt')
json_content=[]
json_dict={}
for line in twitterfile:
   # json_dict=json.loads(line)
   # if 'text' in json_dict:
       json_dict=json.loads(line)
       json_content.append(json_dict)
""" else:
json_content.append('')"""
for line in json_dict:
       tweet=json_dict['text']
       # return json_content
twitterfile.close()
print json_content.items()
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.
#print scores.items()
if __name__ == '__main__':
    main()
