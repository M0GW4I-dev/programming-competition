/* dp[i+1][j]:=i番目までの品物から重さの総和がj以下となるように選んだ時の、価値の総和の最大値 */
#include <cstdio>
/* dp[0][j]=0 -1番目までの品物までの価値の最大値は0にしておく。
 * dp[i+1][j]=max(dp[i][j-k*w[i]]+k*v[i]|0<=k) */

using namespace std;


int dp[MAX_N+1][MAX_W+1];

void solve() {
	for(int i = 0;i < n; i++) {
		for(int j = 0; j < W; j++) {
			for(int k = 0; k*w[i] <= j;k++){
			       dp[i+1][j] = max(dp[i+1][j],dp[i][j-k*w[i]]+k*v[i]);
			}
		}
	}
	printf("%d\n", dp[n][w]);
}

