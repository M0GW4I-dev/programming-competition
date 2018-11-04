#include <iostream>


bool dfs(int i,int sum,int k){
		if(n==i) return sum == k;
		if(dfs(i+1,sum+a[i],k)) return true;
		if(dfs(i+1,sum,k)) return true;
		//return false;
}
int main(void){
		int MAX_N;
		cin > MAX_N;
		int a[MAX_N];
		for(int i = 0;i < MAX_N;i++){
				cin > a[i];
		}
}
