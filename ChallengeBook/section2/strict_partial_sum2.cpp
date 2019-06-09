#include <cstdio>
#include <algorithm>


using namespace std;


int n, K, a[100], m[100];
int dp[1000001];


int main() {
	scanf("%d%d", &n, &K);
	for (int i = 0; i < n; i++) {
		scanf("%d%d", &a[i], &m[i]);
	}
	memset(dp, -1, sizeof(dp));
	dp[0] = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= K; j++) {
			if (dp[j] >= 0){
				dp[j] = m[i];
			} else if (j < a[i] || dp[j - a[i]] <= 0) {
				dp[j] = -1;
			} else {
				dp[j] = dp[j - a[i]] - 1;
			}
		}
	}
	if (dp[K] >= 0) printf("Yes\n"); else printf("No2\n");
	return 0;
}

