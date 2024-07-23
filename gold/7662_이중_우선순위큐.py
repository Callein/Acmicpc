import sys
import heapq


def is_empty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True


t = int(sys.stdin.readline())

for i in range(t):
    min_heap = []
    max_heap = []
    nums = dict()
    k = int(sys.stdin.readline())

    for j in range(k):
        oprt, oprd = sys.stdin.readline().split()
        num = int(oprd)

        if oprt == 'I':
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)

        elif oprt == 'D':
            if not is_empty(nums.items()):
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in nums:
                            del (nums[temp])
                    nums[-max_heap[0]] -= 1
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del (nums[temp])
                    nums[min_heap[0]] -= 1

    if is_empty(nums.items()):
        print('EMPTY')
    else:
        # 허수 제거, min_heap 과 max_heap 의 pop 은 비동기적으로 일어나므로 min 에서 삭제 되었을 때 max 에 남아 있을 수 있다.
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])
