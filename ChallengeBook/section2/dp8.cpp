#include <cstdio>
#include <algorithm>

#define MAX_N 1000
int n;
int a[MAX_N];
int dp[MAX_N];

void solve() {
	int res = 0;
	for (int i = 0; i < n; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (a[j] < a[i]) {
				dp[i] = max(dp[i], dp[j]+1);
			}
		}
		res = max(res, dp[i]);
	}
	printf("%d\n", res);
}

