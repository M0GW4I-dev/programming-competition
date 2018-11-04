import java.lang.StringBuilder;
public class AB {
		public static String createString(int N,int K){
				StringBuilder ans = new StringBuilder();
				if(K==0){
						for(int i=0;i<N;i++){
								ans.append("A");
						}
						return ans.toString();
				}
						
				for(int x=1;x<N;x++){
						if(K%x==0){
								int y=K/x;
								if(x+y<=N){
										for(int i=0;i<x;i++){
												ans.append("A");
										}
										for(int i=0;i<y;i++){
												ans.append("B");
										}
										for(int i=0;i<N-(x+y);i++){
												ans.append("A");
										}
										break;
								}
						}
				}
				return ans.toString();
		}
		public static void main(String[] args){
				System.out.println(createString(3,2));
		}


}
