#include <cstdio>
#include <algorithm>


using namespace std;

pair<int, int> p[25000];
int N, T;

int main() {
	scanf("%d%d", &N, &T);
	for(int i = 0; i < N; i++) {
		scanf("%d%d", &p[i].first, &p[i].second);
	}
	int e = 1, pos = 0, ans = 0;
	while (e < T) {
		int e2 = 0;
		while (pos < N && p[pos].first <= e) {
			e2 = max(e2, p[pos++].second);
		}
		ans++;
		if (pos == N) {
			if (e2 < T) ans = -1;
			break;
		}
		if (e2 == 0) {
			ans = -1;
			break;
		}
		e = e2;
	}
	printf("%d\n", ans);
	return 0;
}

