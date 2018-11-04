#include <cstdio>
using namespace std;

int main(){
		int n;
		scanf("%d",&n);
		if(n/10==9){
				printf("Yes\n");
		}else if(n-n/10*10==9){
				printf("Yes\n");
		}else{
				printf("No\n");
		}
		return 0;
}
