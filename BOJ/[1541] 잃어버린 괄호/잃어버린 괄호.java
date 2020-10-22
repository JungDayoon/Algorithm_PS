import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static String math;
	
	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		math = br.readLine();
	}

	
	
	public static void main(String[] args) throws Exception {
		input();
		
		ArrayList<Integer> num = new ArrayList<>();
		
		int result = 0;
		int tmpSum = 0;
		String now = "";
		for(int i = 0; i<math.length(); i++)
		{
			
			if(math.charAt(i) == '+')
			{
				tmpSum += Integer.parseInt(now);
				now = "";
			}
			else if(math.charAt(i) == '-')
			{
				tmpSum += Integer.parseInt(now);
				num.add(tmpSum);
				tmpSum = 0;
				now = "";
			}
			else
				now+= math.charAt(i);
		}
		tmpSum += Integer.parseInt(now);
		num.add(tmpSum);
		
		for(int i = 0; i<num.size(); i++)
		{
			if(i == 0) {
				result = num.get(i);
				continue;
			}
			
			result -= num.get(i);
		}
		
		System.out.println(result);
	}
}
