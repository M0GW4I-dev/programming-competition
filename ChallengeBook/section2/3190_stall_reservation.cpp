#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

typedef int range_t;

struct Range {
    range_t from, to;
    int index;s
    Range() {};
    Range(range_t from, range_t, to, int index):from(from), to(to), index(index){};
};

bool cmpFrom(const Range& lhs, const Range&rhs) {
    return lhs.from < rhs.from;
}

struct CmpTo {
    bool operator() (const Range& lhs, const Range& rhs) {
        return lhs.to > rhs.to;
    }
};

const int MAX_N = 50000;

int N;

