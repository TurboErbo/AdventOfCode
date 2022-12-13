source credentials.sh

DAY=$1
YEAR=$2
if [[ -z $DAY ]]; then
    DAY=`date +%-d`
fi

if [[ -z $YEAR ]]; then
    YEAR=`date +%-Y`
fi

DATADIR=$YEAR/data
mkdir -p $DATADIR

echo "Preparing files for AoC $YEAR day $DAY..."

touch $DATADIR/${DAY}.example.txt
curl -b $COOKIE https://adventofcode.com/$YEAR/day/${DAY}/input -o $DATADIR/${DAY}.txt
cp template.v2.py $YEAR/${DAY}.py

echo "Done!"