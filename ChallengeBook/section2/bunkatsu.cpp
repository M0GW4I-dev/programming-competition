#include <cstdio>
#include <algorithm>

using namespace std;
int n, m, M;
int dp[1001][1001]


int main() {
	dp[0][0] = 1;
	scanf("%d%d%d", &n, &m, &M);
	for (int i = 1; i <= m; i++) {
		for (int j = 0; j <= n; j++) {
			if (j - i >= 0) {
				dp[i][j] = (dp[i-1][j] + dp[i][j-i])%M;
			} else {
				dp[i][j] = dp[i-1][j];
			}
		}
	}
	printf("%d\n", dp[m][n]);
	return 0;
}

