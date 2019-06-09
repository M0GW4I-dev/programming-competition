#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_A 500

int n, a[MAX_A][MAX_A], dp[MAX_A+1][MAX_A+1];

int solve(int n) {
	int ans = 0;
	dp[0][0] = a[0][0];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i+1; j++) {
			if (j-1>=0){
				dp[i+1][j] = max(dp[i][j-1], dp[i][j])+a[i+1][j];
			} else {
				dp[i+1][j] = dp[i][j]+a[i+1][j];
			}
			ans = max(ans, dp[i+1][j]);
		}
	}
	return ans;
}


int main() {
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		for(int j = 0; j <= i; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	printf("%d\n", solve(n));
	return 0;
}

