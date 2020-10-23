import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	public static char[] str1;
	public static char[] str2;
	public static int[][] LCS;
	
	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		str1 = (" "+ br.readLine()).toCharArray();
		str2 = (" "+ br.readLine()).toCharArray();
		
		LCS = new int[str1.length][str2.length];
	}
	

	public static void main(String[] args) throws Exception {
		input();
		
		for(int i = 1; i<str1.length; i++)
		{
			for(int j = 1; j<str2.length; j++)
			{
				if(str1[i] == str2[j])
				{
					LCS[i][j] = LCS[i-1][j-1] + 1;
				}
				else {
					LCS[i][j] = Math.max(LCS[i-1][j], LCS[i][j-1]);
				}
			}
		}
		
		int maxLCS = 0;
		for(int i = 1; i<str1.length; i++)
		{
			maxLCS = Math.max(maxLCS,Arrays.stream(LCS[i]).max().getAsInt());
		}
		
		System.out.println(maxLCS);
	}
		
}
