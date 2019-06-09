#include <cstdio>
#include <algorithm>

using namespace std;

int n, W;
int w[100], v[100];


/* i 以上のものから, 重さが j 以下になるような最大の価値 */
int rec(int i, int j) {
	if (i == n) {
		return 0;
	}else if(j < w[i]) {
		return rec(i+1, j);
	}else{
		return max(rec(i+1, j-w[i]) + v[i], rec(i+1, j));
	}
	// non reach
	return 0;
}


int main(){
	scanf("%d%d", &n, &W);
	for(int i = 0; i < n; i++) {
		scanf("%d%d", &w[i], &v[i]);
	}
	printf("%d\n", rec(0, W));
	return 0;
}


