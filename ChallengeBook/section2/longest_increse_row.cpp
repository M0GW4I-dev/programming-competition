#include <cstdio>
#include <algorithm> 

using namespace std;

int n, a[1000];
int dp[1000];

int main() {
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	int res = 0;
	for (int i = 0; i < n; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (a[j] < a[i]) {
				dp[i] = max(dp[i], dp[j] + 1);
			}
		} 
		res = dp[i];
	}
	printf("%d\n", res);
	return 0;
}
				
	


	
