#include <cstdio>
#include <algorithm>

using namespace std;

int N, R;
pair<int, int> X[1000];

int solve() {
	sort(X,X+N);
	int i = 0, ans = 0;
	while (i < N) {
		if (X[i].second > R) return -1;
		int x = X[i].first; 
		while (i < N && (X[i].first-x)*(X[i].first-x)+X[i].second*X[i].second <= R*R) x++;
		x--;
		i++;
		while (i < N && (X[i].first-x)*(X[i].first-x)+X[i].second*X[i].second <= R*R) i++;
		if (X[i].second > R) return -1;
		ans++;
	}
	return ans;
}


int main() {
	while(true) {
		int k = 1;
		scanf("%d%d", &N, &R);
		if(N==0 && R==0) break;
		for(int i = 0; i < N; i++) {
			scanf("%d%d", &X[i].first, &X[i].second);
		}
		printf("Case %d: %d\n", k, solve());
		k++;
	}
	printf("\n");
	return 0;
}

