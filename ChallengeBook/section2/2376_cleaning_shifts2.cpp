#include <cstdio>
#include <algorithm>

using namespace std;

int e, n, T;
pair<int, int> interval[25000];

int main() {
	scanf("%d%d", &n, &T);
	for(int i = 0; i < n; i++) {
		scanf("%d%d", &interval[i].first, &interval[i].second);
	}
	int i = 0, ans = 0;
	e = 1;
	while(i < n && e <= T) {
		int tmp = 0;
		for(; interval[i].first <= e &&  i < n; i++) {
			if(interval[i].second > e && interval[i].second > tmp) {
				tmp = interval[i].second;
			}
		}
		e = tmp;
		ans++;
	}
	printf("%d\n", ans);
	return 0;
} 

