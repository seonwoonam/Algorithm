
import java.util.Arrays;

/*
 * 연속된 구간의 데이터 합을 가장 빠르고 간단하게 구할 수 있는 트리
 * 합을 구할 때 시간복잡도는 O(logN)을 가진다.
 * 
 * 상황 : 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구해야한다. 
 * 
 * 배열의 크기 N일때 완전 이진 트리 높이
 * h-1 < log2(N) <= h
 * N =5 이면, h=3 이다.
 * 2**0 + 2**1 + 2**2 + 2**3 = 15
 * 2**(h+1)-1
 * 
 * 루트 노드의 인덱스를 1로 한다면
 * 세그먼트 트리의 treeSize = 2^(h+1)
 * 
 * ============================================================
 * 기본적으로 보통 재귀형태로 구현
 * 
 * 1. 생성자
 *  - 세그먼트 트리의 배열 사이즈 정해주기
 * 2. init(arr, tree_idx, start, end)
 *  - 현재의 배열 상태에 맞게 트리 구성하기
 *  - 재귀 형태로 진행
 * 3. update
 *  - 특정 원소값(리프 노드의 값)을 수정하는 함수 
 *  - 재귀적으로 진행 가능
 *  - 변경된 차이만큼 더해주고 자식노드들을 확인하러 간다.
 * 4. 구간합 구하기
 *  - 현재 배열이 찾고자하는 것의 범위에서 벗어나면 0 반환
 *  - 재귀 
 */

public class segment_tree {
    int[] tree; // 원소가 담길 트리
    int treeSize; 

    public segment_tree(int arrSize){
        this.treeSize = arrSize * 4;
        tree = new int[this.treeSize];
    }

    // tree_idx : 현재노드
    // start, end : 현재노드가 커버하는 범위
    public int init(int[] arr, int tree_idx, int start, int end){
        if(start == end){
            // 리프 노드를 의미
            tree[tree_idx] = arr[start];
            return tree[tree_idx]; 
        }

        tree[tree_idx] = init(arr, tree_idx * 2, start, (start+end)/2) + init(arr, tree_idx*2+1,(start+end)/2+1,end);
        return tree[tree_idx];
    }

    // 특정 원소값을 수정하는 함수
    // tree_idx : 현재노드
    // start, end : 현재노드가 커버하는 범위
    // arr_idx : 변경된 데이터의 arr 상의 idx
    // diff : 원래 데이터 값과 변경 데이터 값의 차이
    public void update(int tree_idx, int start, int end, int arr_idx, int diff){
        if (arr_idx < start || arr_idx > end) return;
        tree[tree_idx] += diff;
        if(start != end){
            update(tree_idx * 2, start, (start+end)/2, arr_idx,diff);
            update(tree_idx * 2 + 1, (start+end)/2 + 1, end, arr_idx, diff);
        }
    }

    // 구간합 가져오기
    // left : 원하는 누적합의 시작
    // right : 원하는 누적합의 끝
    public int get_sum(int tree_idx, int start, int end, int left, int right){
        // 아예 벗어날때
        if(left > end || right < start){
            return 0;
        }
        
        // 아예 들어올 떄
        if(left<=start && end <= right){
            return tree[tree_idx];
        }

        // 걸쳐 있을 때(그 외의 경우)
        return get_sum(tree_idx*2, start, (start+end)/2, left, right) + get_sum(tree_idx * 2 + 1, (start+end)/2 + 1, end, left, right);
    }
}
