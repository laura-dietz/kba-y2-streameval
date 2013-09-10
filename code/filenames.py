import os.path


COLLAPSED_JUDGMENT_FILE = os.path.expanduser('~/kba-evaluation/taia-stream-eval/data/collapsed-onlypos-trec-kba-ccr-2013-judgments-2013-07-08.filter-run.txt') # year 2
ORIG_JUDGMENT_FILE ='~/kba-evaluation/kba-scorer-y2/data/trec-kba-ccr-judgments-2013-07-08.before-and-after-cutoff.filter-run.txt'  # year 2
#COLLAPSED_JUDGMENT_FILE ='~/kba-evaluation/taia/data/collapsed-onlypos-trec-kba-ccr-2012-judgments-2012JUN22-final.filter-run.txt'  # year 1
#ORIG_JUDGMENT_FILE ='~/kba-evaluation/taia/data/trec-kba-ccr-2012-judgments-2012JUN22-final.filter-run.txt'  # year 1

#evalTR = 1325376000 # year 1
#evalTRend = 1338508800  # year 1
evalTR = 1330559999000  # year 2
evalTRend = 1360368000  # year 2