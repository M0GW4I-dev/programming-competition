#include <cstdio>
#include <algorithm>

using namespace std;

int n,W;
int dp[101][10001];
int w[100];
int v[100];

int main() {
	scanf("%d%d", &n,&W);
	for(int i = 0; i < n; i++){
		scanf("%d%d", &w[i],&v[i]);
	}

	for(int i = 0; i < n; i++) {
		for(int j = 0; j <=W; j++) {
			for(int k = 0; k*w[i] <= j; k++) {
				dp[i+1][j] = max(dp[i+1][j], dp[i][j-k*w[i]]+k*v[i]);
			}
		}
	}
	printf("%d\n", dp[n][W]);
}

