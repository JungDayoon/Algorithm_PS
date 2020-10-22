import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static int N, M;
	public static ArrayList<Integer>[] computer;
	public static boolean[] visited;
	public static int count = 0;
	
	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine(), " ");
		M = Integer.parseInt(st.nextToken());
		
		computer = new ArrayList[N];
		visited = new boolean[N];
		
		for(int i = 0; i<N; i++)
		{
			computer[i] = new ArrayList<Integer>();
		}
		
		for(int i = 0; i<M; i++)
		{
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken())-1;
			int b = Integer.parseInt(st.nextToken())-1;
			computer[a].add(b);
			computer[b].add(a);	
		}
	}

	public static void dfs(int num)
	{
		visited[num] = true;
		
		for(int i = 0; i<computer[num].size(); i++)
		{
			if(!visited[computer[num].get(i)])
			{
				dfs(computer[num].get(i));
				count++;
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		input();
		
		dfs(0);
		
		System.out.println(count);
	}
}
