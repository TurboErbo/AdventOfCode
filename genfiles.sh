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
touch $DATADIR/${DAY}.solution.txt
curl -b $COOKIE https://adventofcode.com/$YEAR/day/${DAY}/input -o $DATADIR/${DAY}.txt

PYFILE=$YEAR/${DAY}.py
cp -n templates/python/template.v2.py $PYFILE

CPPDIR=$YEAR/cpp/$DAY
cp -n templates/cpp/solution.hpp.template $CPPDIR
cp -n templates/cpp/test.cpp.template $CPPDIR/test.cpp
cp -n templates/cpp/utilities.hpp.template $CPPDIR/utilities.hpp

echo "Done!"