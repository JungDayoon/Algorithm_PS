import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	public static int N;
	public static int Q;
	public static int[][] Map;
	public static int[] level;
	public static int mapSize;
	public static int[][] pos = {{-1,0}, {0,1}, {1,0}, {0,-1}};
	
	public static class Loc{
		int y, x;
		
		Loc(int y, int x)
		{
			this.y = y;
			this.x = x;
		}
	}
	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N= Integer.parseInt(st.nextToken());
		Q = Integer.parseInt(st.nextToken());
		
		mapSize = (int) (Math.pow(2, N));
		Map = new int[mapSize][mapSize];
		level = new int[Q];
		
		for(int i = 0; i<mapSize; i++)
		{
			st = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j<mapSize; j++)
			{
				Map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine(), " ");
		for(int i = 0; i<Q; i++)
		{
			level[i] = Integer.parseInt(st.nextToken());
		}
		
		
	}
	
	public static void rotateOne(int sy, int sx, int levelSize)
	{
		int[][] newMap = new int[levelSize][levelSize];
		
		for(int i = sy; i<sy+levelSize; i++)
		{
			for(int j = sx; j<sx+levelSize; j++)
			{
				newMap[i-sy][j-sx] = Map[i][j];
			}
		}
		
		int yIdx = sy;
		for(int j = 0; j<levelSize; j++)
		{
			int xIdx = sx;
			for(int i = levelSize-1; i>=0; i--)
			{
				Map[yIdx][xIdx++] = newMap[i][j];
			}
			yIdx++;
		}
	}
	
	public static void rotate(int Level)
	{
		int levelSize = (int) Math.pow(2, Level);
		for(int i = 0; i<mapSize; i+=levelSize)
		{
			for(int j = 0; j<mapSize; j+=levelSize)
			{
				rotateOne(i, j, levelSize);
			}
		}
	}
	
	public static boolean isIn(int y, int x)
	{
		if(y>=0 && y<mapSize && x>=0 && x<mapSize)
			return true;
		return false;
	}
	
	public static void meltIce()
	{
		ArrayList<Loc> meltLoc = new ArrayList<>();
		
		for(int i = 0; i<mapSize; i++)
		{
			for(int j = 0; j<mapSize; j++)
			{
				int iceCnt = 0;
				if(Map[i][j] == 0)
					continue;
				for(int p = 0; p<4; p++)
				{
					int ny = i + pos[p][0];
					int nx = j + pos[p][1];
					
					if(isIn(ny, nx) && Map[ny][nx] > 0)
						iceCnt += 1;
				}
				if(iceCnt <3)
				{
					meltLoc.add(new Loc(i, j));
				}
			}
		}
		
		for(Loc melt: meltLoc)
		{
			Map[melt.y][melt.x] -= 1;
		}
	}
	
	public static int bfs(int y, int x, boolean[][] visited)
	{
		int count = 0;
		Queue<Loc> Q = new LinkedList<>();
		
		Q.offer(new Loc(y, x));
		visited[y][x] = true;
		
		while(!Q.isEmpty())
		{
			Loc curr = Q.poll();
			count += 1;
			for(int i =0; i<4; i++)
			{
				int ny = curr.y + pos[i][0];
				int nx = curr.x + pos[i][1];
				
				if(isIn(ny, nx) && !visited[ny][nx] && Map[ny][nx] > 0)
				{
					Q.offer(new Loc(ny, nx));
					visited[ny][nx] = true;
				}
			}
		}
		
		return count;
	}
	
	public static void main(String[] args) throws Exception {
		input();
		
		for(int q = 0; q<Q; q++)
		{
			rotate(level[q]);
			meltIce();
		}
		
		boolean[][] visited = new boolean[mapSize][mapSize];
		int resCnt = 0;
		int maxCount = 0;
		for(int i = 0; i<mapSize; i++)
		{
			for(int j = 0; j<mapSize; j++)
			{
				resCnt += Map[i][j];
				if(Map[i][j] > 0 && !visited[i][j])
				{
					maxCount = Math.max(maxCount, bfs(i, j, visited));
				}
			}
		}
		
		System.out.println(resCnt);
		System.out.println(maxCount);
	}
		
}
