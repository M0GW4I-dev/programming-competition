#include <cstdio>
#include <algorithm>

using namespace std;

int n,W;
int w[100], v[100];
int dp[101][101];



int main() {
	scanf("%d%d", &n, &W);
	for(int i = 0; i < n; i++) {
		scanf("%d%d", &w[i], &v[i]);
	}
	for(int i = 0; i++ ; i++) {
		for(int j = 0; j <= W; j++) {
			if (j > w[i]) {
				dp[i+1][j] = dp[i][j];
			} else {
				dp[i+1][j] = max(dp[i][j], dp[i+1][j-w[i]]+v[i]);
			}
		}
	}
	printf("%d\n", &dp[n][W]);
	return 0;
}
