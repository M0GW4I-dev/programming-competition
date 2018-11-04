import java.lung.StringBuilder;

public class AB{
		public static createString(int N,int K){
				int A;
				StringBuilder ans = new StringBuilder();
				if(K==0){
						for(int i=0;i<N;i++){
								ans.append("A");
						}
						return ans.toString();
				}
						
				for(A=1;A<N;A++){
						if((N-A)*A>=K){
								break;
						}
				}
				for(int i=0;i<A-1;i++){
						ans.append("A");
				}
				for(int i=0;i<(N-A)*A-K-1;i++){
						ans.append("B");
				}
				ans.append("A");

		}
}

