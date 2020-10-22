import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class Main {
	static int N, M, K;
	static ArrayList<Fireball> fireballList = new ArrayList<>();
	static int[][] pos = {{-1, 0}, {-1, 1}, {0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1}};
	static int[] odd = {1,3,5,7};
	static int[] even = {0,2,4,6};
	
	static class Fireball{
		int y, x, m, s, d;
		Fireball(int y, int x, int m, int s, int d){
			this.y = y;
			this.x = x;
			this.m = m;
			this.s = s;
			this.d = d;
		}
		
		int getCount()
		{
			return this.m;
		}
	}
	
	public static void moveFireBall()
	{
		ArrayList<int[]>[][] fireballMap = new ArrayList[N][N];
		for(int i = 0; i<N; i++)
		{
			for(int j = 0; j<N; j++)
			{
				fireballMap[i][j] = new ArrayList<>();
			}
		}
		
		while(!fireballList.isEmpty())
		{
			Fireball fb = fireballList.get(0);
			fireballList.remove(0);
			
			int ny = (fb.y + N + pos[fb.d][0] * (fb.s  % N)) % N;
			int nx = (fb.x + N + pos[fb.d][1] * (fb.s  % N)) % N;
			
			int[] newFB = {fb.m, fb.s, fb.d};
			
			fireballMap[ny][nx].add(newFB);
		}
		
		for(int i = 0; i<N; i++)
		{
			for(int j = 0; j<N; j++)
			{
				if(fireballMap[i][j].size() == 1)
				{
					fireballList.add(new Fireball(i, j, fireballMap[i][j].get(0)[0], fireballMap[i][j].get(0)[1], fireballMap[i][j].get(0)[2]));
				}
				else if(fireballMap[i][j].size() > 1)
				{
					int sSum = 0;
					int mSum = 0;
					boolean evenFlag = false;
					boolean oddFlag = false;
					
					for(int[] fb: fireballMap[i][j])
					{
						mSum += fb[0];
						sSum += fb[1];
						if(fb[2] % 2 == 0)
						{
							evenFlag = true;
						}
						else {
							oddFlag = true;
						}
					}
					int newM = mSum / 5;
					if(newM == 0)
						continue;
					int newS = sSum / fireballMap[i][j].size();
					if(evenFlag && oddFlag)
					{
						for(int newD : odd)
						{
							fireballList.add(new Fireball(i, j, newM, newS, newD));
						}
			
					}
					else {
						for(int newD: even)
						{
							fireballList.add(new Fireball(i, j, newM, newS, newD));
						}
					}
				}
			}
		}
	}
	public static void input() throws IOException {
	      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	      StringTokenizer st = new StringTokenizer(br.readLine(), " ");
	      
	      N = Integer.parseInt(st.nextToken());
	      M = Integer.parseInt(st.nextToken());
	      K = Integer.parseInt(st.nextToken());
	      
	      for(int i = 0; i < M; i++) {
	    	 st = new StringTokenizer(br.readLine(), " ");
	         fireballList.add(new Fireball(Integer.parseInt(st.nextToken())-1, Integer.parseInt(st.nextToken())-1, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
	      }
	 }
	
	public static void main(String[] args) throws Exception
	{
		input();
		
		for(int k = 0; k<K; k++)
		{
			moveFireBall();
		}
		
		int count = 0;
		for(Fireball fb: fireballList)
		{
			count += fb.getCount();
		}
		
		System.out.println(count);
	}
}
