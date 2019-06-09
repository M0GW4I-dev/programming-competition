#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_N 100
#define MAX_W 10000

int n, W, dp[MAX_N+1][MAX_W+1], w[MAX_N], v[MAX_N];
void solve() {
	for (int i = 0; i < n;i++) {
		for ( int j = 0; j <=W; j++) {
			if (j < w[i]) {
				dp[i+1][j] = dp[i][j];
			} else {
				dp[i+1][j] = max(dp[i][j], dp[i+1][j-w[i]]+v[i]);
			}
		}
	}
	printf("%d\n", dp[n][W]);
}

int main(){
	scanf("%d %d", &n, &W);
	for(int i=0;i<n;i++){
		scanf("%d %d", &w[i], &v[i]);
	}
	solve();
	return 0;
}
