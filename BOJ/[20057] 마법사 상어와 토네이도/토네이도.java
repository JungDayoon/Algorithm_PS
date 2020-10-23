import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	public static int N;
	public static int[][] Map;
	public static int[][] pos = {{0,-1}, {1,0}, {0,1}, {-1,0}};
	public static int[][][] sandPos = 
		{{{-1,-1}, {1,-1}, {-1,0}, {1,0}, {0,-2}, {-2,0}, {2,0}, {-1,1}, {1,1}, {0,-1}},
			{{1,-1}, {1,1}, {0,-1}, {0,1}, {2,0}, {0,-2}, {0,2}, {-1,-1}, {-1,1}, {1,0}},
			{{-1,1}, {1,1}, {-1,0}, {1,0}, {0,2}, {-2,0}, {2,0}, {-1,-1}, {1,-1}, {0,1}},
			{{-1,-1}, {-1,1}, {0,-1}, {0,1}, {-2,0},{0,-2}, {0,2}, {1,-1}, {1,1}, {-1,0}}};
	
	public static double[] sandPercent = {0.1, 0.1, 0.07, 0.07, 0.05, 0.02, 0.02, 0.01, 0.01};
	
	public static int sandCnt;
	
	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N= Integer.parseInt(st.nextToken());
		Map = new int[N][N];
		
		for(int i = 0; i<N; i++)
		{
			st = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j<N; j++)
			{
				Map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
	}

	public static void spreadSand(int posNum, int y, int x)
	{
		int origSand = Map[y][x];
		int sandSum = 0;
		Map[y][x] = 0;
		for(int i = 0; i<sandPos[posNum].length; i++)
		{
			int ny = y + sandPos[posNum][i][0];
			int nx = x + sandPos[posNum][i][1];
			
			int sandPart;
			if(i == sandPos[posNum].length -1)
			{
				sandPart = origSand - sandSum;
			}
			else {
				sandPart = (int) (origSand * sandPercent[i]);
				sandSum += sandPart;
			}
			if(0<=ny && ny <N && nx >=0 && nx<N)
			{
				Map[ny][nx] += sandPart;
			}
			else {
				sandCnt += sandPart;
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		input();
		
		int cnt = 0;
		int posNum = 0;
		int y = N/2;
		int x = N/2;
		
		loop:
		while(true)
		{
			if(posNum % 2 == 0)
			{
				cnt++;
			}
			for(int nowCnt = 0; nowCnt < cnt; nowCnt++)
			{
				y = y + pos[posNum][0];
				x = x + pos[posNum][1];
				
				spreadSand(posNum, y, x);
				if(y == 0 && x == 0)
					break loop;
			}
			posNum = (posNum + 1) % 4;
		}
		
		System.out.println(sandCnt);
	}
}
