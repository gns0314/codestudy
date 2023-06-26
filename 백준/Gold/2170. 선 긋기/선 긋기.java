import java.io.*;
import java.util.*;

class Main {
    static class Line {
        int start;
        int end;

        public Line(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    public static void main(String[] args) throws IOException {
        int ans = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        List<Line> lines = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            String[] arr = s.split(" ");

            int start = Integer.parseInt(arr[0]);
            int end = Integer.parseInt(arr[1]);
            lines.add(new Line(start, end));
        }

        // 선분을 시작 좌표를 기준으로 정렬
        Collections.sort(lines, Comparator.comparingInt(l -> l.start));

        int x = lines.get(0).start;
        int y = lines.get(0).end;

        for (int i = 1; i < N; i++) {
            Line currLine = lines.get(i);
            if (y >= currLine.start) { // 겹치는 경우
                y = Math.max(y, currLine.end);
            } else {
                ans += y - x;
                x = currLine.start;
                y = currLine.end;
            }
        }

        ans += y - x;

        br.close();
        bw.write(Integer.toString(ans));
        bw.flush();
        bw.close();
    }
}