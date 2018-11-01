#include <cstdio>


void swap(int *a,int *b){
		int tmp = *a;
		*a=*b;
		*b=tmp;
}


int SameInteger(int a,int b,int c){
		int res=0;
		if (a==b && b==c){
				return 0;
		}
		res+=(a-b);
		if ((b-c)%2==0){
				res+=((b-c)/2);
		}else{
				res++;
				res+=((b-c)/2);
				res++;
		}
		return res;
}


int main(){
		int a,b,c,res=0;
		scanf("%d %d %d",&a,&b,&c);
		if(b-a>0){
				swap(&a,&b);
		}
		if(c-b>0){
				swap(&b,&c);
		}
		if(b-a>0){
				swap(&b,&a);
		}

		printf("%d\n",SameInteger(a,b,c));

		return 0;
}
