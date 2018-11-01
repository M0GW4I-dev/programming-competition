#include <cstdio>
#include <algorithm>
using namespace std;

#define MAX_N 20
int num[MAX_N];
int k,n;
bool solve(int sum, int i){
	if (i == n){
		if (sum == k){
			return true;
		}else{
			return false;
		}
	}
	if (solve(sum+num[i], i+1)) return true;
	if (solve(sum,i+1)) return true;
	return false;
}

int main(){
	scanf("%d %d", &n, &k);
	for (int i=0;i<n;i++){
		scanf("%d",&num[i]);
	}
	if(solve(0,0)){
		printf("Yes\n");
	}else{
		printf("No\n");
	}
	return 0;
}
