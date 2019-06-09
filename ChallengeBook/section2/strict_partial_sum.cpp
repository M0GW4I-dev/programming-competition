#include <cstdio>
#include <algorithm>

using namespace std;

int n, K, a[100], m[100];
bool dp[101][100001];

int main() {
	scanf("%d%d", &n, &K);
	for (int i = 0; i < n; i++) {
		scanf("%d%d", &a[i], &m[i]);
	}
	dp[0][0] = true;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j <= K; j++) {
			for(int k = 0; k <= m[i] && k*a[i] <= j; k++) {
				dp[i+1][j] |= dp[i][j-k*a[i]];
			}
		}
	}
	printf(dp[n][K]? "Yes\n": "No\n");
	return 0;
}
