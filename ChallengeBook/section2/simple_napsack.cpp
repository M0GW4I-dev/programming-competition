#include <cstdio>
#include <algorithm>

using namespace std;
#define INF 1000000

int n,W;
int dp[101][10001];
int w[100];
int v[100];

int main() {
	scanf("%d%d", &n,&W);
	for(int i = 0; i < n; i++){
		scanf("%d%d", &w[i],&v[i]);
	}
	fill(dp[0], dp[0] + 100 * 100 + 1, INF);
	int ans;
	dp[0][0] = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= 100 * 100; j++) {
			if(j < v[i]) {
				dp[i+1][j] = dp[i][j];
			}else{
				dp[i+1][j] = min(dp[i][j],  dp[i][j-v[i]]+w[i]);
			}
		}
	}
	for(int i = 0; i <= 100 * 100; i++) {
		if (dp[n][i] <= W) {
			ans = i;
		}
	}
	printf("%d\n", ans);
	return 0;
}


