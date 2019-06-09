#include <cstdio>

using namespace std;
#define MAX_N 1000000

int dp[MAX_N+1];


int solve(int n) {
	dp[1]=1;
	for(int i=2;i<=n; i++) {
		if (i%2==0) {
			dp[i] = (dp[i/2]+dp[i-1])%1000000000;
		} else {
			dp[i] = dp[i-1]%1000000000;
		}
	}
	return dp[n];
}

int main(){
	int n;
	scanf("%d", &n);
	printf("%d\n", solve(n));
}
