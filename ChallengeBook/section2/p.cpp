#include <cstdio>


using namespace std;


int main(){
	int *a,*b;
	a = (int *)0x4;
	b = (int *)0xc;
	printf("%ld\n", b-a);
	return 0;
}
