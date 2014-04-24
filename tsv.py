import csv
import tarfile

from tweet import Tweet
from collection import Collection


def process_tar(path):
    c = Collection()
    with tarfile.open(path, mode='r:gz') as tar:
        member = tar.getmembers()[0]  # assume single file tar
        f = tar.extractfile(member)
        tsv = csv.reader(f, delimiter='\t')
        for i, row in enumerate(tsv):
            if row[-1] != '\\N' or row[-2] != '\\N':
                print row
                raise Exception('Unexpected format.')

            tweet = Tweet(*row)
            c.add_tweet(tweet)
    print c.start_date, c.end_date

process_tar('C:/Users/Michael/Downloads/twitterdata_oklahomatornado-20130520_20130530_GMT.tsv.tar.gz')