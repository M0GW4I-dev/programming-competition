#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
	int n,a,b,A=0,B=0;
	scanf("%d", &n);
	bool flag = true;
	for(int i=0;i<n;i++){
			scanf("%d %d", &a,&b);
			if(a!=b){
					flag=false;
			}
			if(a>b){
					B=min(B,b);
			}
			A+=a;
	}
	if (flag){
			puts("0");
	}else{
			printf("%d\n",A-B);
	}
}




