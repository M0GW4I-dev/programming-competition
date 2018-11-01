#include <cstdio>
#define ll long\ long
int main(){
		int q,i,j,a,b;
		ll res,ans,left,right;
		scanf("%d",&q);
		for(i=0;i<q;i++){
				scanf("%d %d",&a,&b);
				for(j=a+1;j<=b;j++){
						left=a;
						right=b-1;
						mid=(a+b-1)/2;
						for(;;){
								if(mid*j>=a*b){
										right=mid;
										mid=(left+right)/2;
										
										continue;
								}else if(mid*j<a*b){
										left=mid;
										mid=(left+right)/2;
										if(mid==left){
												break;
										}
										continue;
								}








}
