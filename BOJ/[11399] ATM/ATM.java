import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static int N;
	public static int[] time;
	
	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken());
		time = new int[N];
		
		st = new StringTokenizer(br.readLine(), " ");
		for(int i = 0; i<N; i++)
		{
			time[i] = Integer.parseInt(st.nextToken());
		}
	}

	
	
	public static void main(String[] args) throws Exception {
		input();
		int sum = 0;
		Arrays.sort(time);
		int cnt = N;
		for(int i = 0; i< N; i++)
		{
			sum += time[i]*cnt;
			cnt--;
		}
		
		System.out.println(sum);
	}
}
