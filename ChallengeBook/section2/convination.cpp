#include <cstdio>
#include <algorithm>

using namespace std;

int n, m, M, a[100];
int dp[1001][1001];

int main() {
	scanf("%d%d%d", &n, &m, &M);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	for (int i = 0; i <= n; i++) {
		dp[i][0] = 1;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= m; j++) {
			if (j-1-a[i] >= 0) {
				dp[i+1][j] = (dp[i+1][j-1]+dp[i][j]-dp[i][j-1-a[i]]+M)%M;
			} else {
				dp[i+1][j] = (dp[i+1][j-1]+dp[i][j])%M;
			}
		}
	}
	printf("%d\n", dp[n][m]);
}
