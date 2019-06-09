#include <cstdio>
#include <algorithm>


using namespace std;


pair<int, int> p[100];
bool dp[100000];
int n,m;

int main() {
	while(true) {
		scanf("%d%d", &n, &m);
		if(n == 0 && m == 0) {
			break;
		}
		for(int i = 0; i < n; i++) {
			scanf("%d", &p[i].first);
		}
		for(int i = 0; i < n; i++) {
			scanf("%d", &p[i].second);
		}
		sort(p,p+n);
		dp[0] = true;
		int ans = 0;
		for (int i = p[0].first; i <= m; i++) {
			for (int j = n-1; j >= 0; j--) {
				int c = p[j].first;
				if(p[j].second > 0) {
					dp[i] = dp[i-c];
					if(dp[i]) {
						printf("%dを使用\n", p[j].second);
						p[j].second--;
						ans += 1;
						break;
					}
				}
			}
		}
		printf("%d\n", ans);
	}
}

