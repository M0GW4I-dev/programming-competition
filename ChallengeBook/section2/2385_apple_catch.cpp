#include <cstdio>
#include <algorithm>
#define MAX_N 1000
#define MAX_M 30

using namespace std;

int dp[MAX_N+1][MAX_M+1];
int a[MAX_N+1];
int n, m;


int solve(int n, int m){
	for(int i = 1; i <= n; i++) {
		dp[i][0] = dp[i-1][0] + (a[i]==1);
		for(int j = 1; j <=  m; j++) {
			dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+(a[i]==j%2+1);
		}
	}
	return dp[n][m];
}

int main() {
	scanf("%d %d", &n, &m);
	for(int i = 1; i <= n; i++) {
		scanf("%d", &a[i]);
	}
	printf("%d\n", solve(n, m));
	return 0;
}

