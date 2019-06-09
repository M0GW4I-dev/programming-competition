/*
 * dp[i+1][j]:=i番目まででjが作れるか
 */


int n, K, a[MAX_N], m[MAX_N];

bool dp[MAX_N+1][MAX_K+1];

void solve() {
	dp[0][0] = true;
	for (int i=0;i<n;i++) {
		for (int j=0;j<=K; j++) {
			for (int k=0;k<=m[i] && k*a[i]<=j k++) {
				dp[i+1][j] |= dp[i][j-k*a[i]];
			}
		}
	}
	if (dp[n][K]) printf("Yes\n");
	else printf("No\n");
}
