/*
SWEA - 6808 규영이와 인영이의 카드게임

# 1. 테스트 케이스 입력을 받는다.  T / 규영이의 카드들
# 2. 인영이의 카드는 1 ~ 18 번 카드 중에 규영이가 가져간 카드를 제외한 카드들.
# 3. 인영이 카드의 순열을 DFS로 생성하며 라운드를 진행한다.
    # 3-1. depth번째 라운드에 아직 안 낸 인영이 카드를 하나씩 선택
    # 3-2. 규영이의 depth번째 카드와 비교하여 점수 누적
    # 3-3. 총점은 항상 171이므로 한쪽이 86 이상이면 승패 확정 -> 남은 순열 수(remain!)만큼 한 번에 카운트 (가지치기)
# 4. 9라운드 끝나면 규영이 점수 > 85 이면 win, 아니면 lose
# 5. 출력한다.
*/
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static final int HALF = 85;              // 171 / 2, 86점 이상이면 승리 확정
    static final int[] FACT = new int[10];   // FACT[n] = n!

    static int[] kyuyoung = new int[9];
    static int[] inyoung = new int[9];
    static boolean[] used = new boolean[9];
    static int win, lose;

    // 3. 인영이 카드의 순열을 DFS로 생성하며 라운드를 진행한다.
    static void dfs(int depth, int kPoint, int iPoint) {
        // 3-3. 한쪽이 86 이상이면 승패 확정 -> 남은 카드 순열 수만큼 한 번에 카운트
        if (kPoint > HALF) { win += FACT[9 - depth]; return; }
        if (iPoint > HALF) { lose += FACT[9 - depth]; return; }

        // 4. 9라운드 끝나면 규영이 점수 > 85 이면 win, 아니면 lose (무승부 없음)
        if (depth == 9) {
            if (kPoint > iPoint) win++; else lose++;
            return;
        }

        // 3-1. depth번째 라운드에 아직 안 낸 인영이 카드를 하나씩 선택
        for (int i = 0; i < 9; i++) {
            if (used[i]) continue;
            used[i] = true;

            // 3-2. 규영이의 depth번째 카드와 비교하여 점수 누적
            int sum = kyuyoung[depth] + inyoung[i];
            if (kyuyoung[depth] > inyoung[i]) dfs(depth + 1, kPoint + sum, iPoint);
            else dfs(depth + 1, kPoint, iPoint + sum);

            used[i] = false;
        }
    }

    public static void main(String[] args) throws Exception {
        FACT[0] = 1;
        for (int n = 1; n <= 9; n++) FACT[n] = FACT[n - 1] * n;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 1. 테스트 케이스 입력을 받는다.  T / 규영이의 카드들
        int T = Integer.parseInt(br.readLine().trim());
        for (int tc = 1; tc <= T; tc++) {
            boolean[] taken = new boolean[19];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 9; i++) {
                kyuyoung[i] = Integer.parseInt(st.nextToken());
                taken[kyuyoung[i]] = true;
            }

            // 2. 인영이의 카드는 1 ~ 18 번 카드 중에 규영이가 가져간 카드를 제외한 카드들.
            int idx = 0;
            for (int c = 1; c <= 18; c++)
                if (!taken[c]) inyoung[idx++] = c;

            win = 0; lose = 0;
            dfs(0, 0, 0);

            // 5. 출력한다.
            sb.append('#').append(tc).append(' ').append(win).append(' ').append(lose).append('\n');
        }
        System.out.print(sb);
    }
}