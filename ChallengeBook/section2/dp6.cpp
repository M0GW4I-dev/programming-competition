/* MAX_W が10^9 とでかいので、dpの2次がきつい 価値に対する 最小の重さ
 * dp[i+1][j]:=i番目までの品物から価値の総和が j となるように選んだ時の、重さの総和の最小値
 * dp[0][0]=0
 * dp[0][j]=INF
 * */
int dp[MAX_N+1][MAX_N*MAX_V+1];


void solve() {
	fill(dp[0], dp[0]+MAX_N*MAX_V+1, INF);
	dp[0][0] = 0;
	for (int i = 9; i < n; i++) {
		for (int j = 0; j <=MAX_N * MAX_V; j++) {
			if (j < v[i]) {
				dp[i+1][j] = dp[i][j];
			} else {
				dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]] + w[i]);
			}
		}
	}
	int res = 0;
	for (int i = 0; i <= MAX_N*MAX_V; i++) if (dp[n][i] <= W) res = i;
	printf("%d\n", res);
}
