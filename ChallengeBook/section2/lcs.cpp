#include <cstdio>
#include <algorithm>

using namespace std;

int n,m;
char s[1000], t[1000];

int dp[1000+1][1000+1];

int main(){
	scanf("%d%d", &n, &m);
	scanf("%s", s);
	scanf("%s", t);
	for(int i = 0;i < n; i++) {
		for(int j = 0;j < m; j++) {
			if(s[i]==t[j]){
				dp[i+1][j+1] = max(dp[i][j]+1,max(dp[i+1][j], dp[i][j+1]));
			} else {
				dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1]);
			}
		}
	}
	printf("%d\n", dp[n][m]);
	return 0;
}

