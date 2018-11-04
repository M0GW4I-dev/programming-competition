#include <cstdio>
using namespace std;

int main(){
		int ans=0,n=0;
		int a,b;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
				scanf("%d %d",&a,&b);
				ans+=(b-a+1);
		}
		printf("%d\n",ans);
		return 0;
}
