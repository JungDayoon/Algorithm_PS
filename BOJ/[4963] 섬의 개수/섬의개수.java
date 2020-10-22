import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static int w, h;
	public static int[][] Map;
	public static boolean[][] visited;
	public static int count = 0;
	public static int[][] pos = {{-1,0}, {1,0}, {0,1}, {0,-1}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};
	public static boolean input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		count = 0;
		
		w = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());
		
		if(w == 0 && h == 0)
			return false;
		
		Map = new int[h][w];
		visited = new boolean[h][w];
		
		for(int i = 0; i<h; i++)
		{
			st = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j<w; j++)
			{
				Map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		return true;
	}

	public static boolean isIn(int y, int x)
	{
		if(y>=0 && y<h && x>=0 && x<w)
			return true;
		return false;
	}
	
	public static void dfs(int y, int x)
	{
		visited[y][x] = true;
		
		for(int i = 0; i<8; i++)
		{
			int ny = y + pos[i][0];
			int nx = x + pos[i][1];
			
			if(isIn(ny, nx) && !visited[ny][nx] && Map[ny][nx] == 1)
			{
				visited[ny][nx] = true;
				dfs(ny, nx);
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		while(true)
		{
			if(!input())
				break;
			
			for(int i = 0; i<h; i++)
			{
				for(int j = 0; j<w; j++)
				{
					if(Map[i][j] == 1 && !visited[i][j])
					{
						dfs(i, j);
						count += 1;
					}
				}
			}
			System.out.println(count);
		}
		
		
	}
}
