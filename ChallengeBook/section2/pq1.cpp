#include <queue>
#include <cstdio>
#include <algorithm>
using namespace std;


int L, P, N;
int A[101], B[101];


void solve() {
	A[N] = L;
	B[N] = 0;
	priority_queue<int> que;
	int ans = 0, pos = 0, tank = P;
	for (int i = 0; i < N; i++) {
		int d = A[i]-pos;
		while (tank-d<0) {
			if (que.empty()) {
				puts("-1");
				return;
			}
			tank+=que.top();
			que.pop();
			ans++;
		}
		tank -= d;
		pos = A[i];
		que.push(B[i]);
	}
	printf("%d\n", ans);
}


int main() {
	scanf("%d %d %d", &N, &L, &P);
	for(int i = 0; i < N; i++) {
		scanf("%d%d", &A[i], &B[i]);
	}
	solve();
	return 0;
}
