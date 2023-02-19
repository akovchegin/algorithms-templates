def merge(arr, lf, mid, rg):
	i = lf
	j = mid
	k = 0
	merged_arr = [None]*(rg-lf)
	while i < mid and j < rg:
		if arr[i] <= arr[j]:
			merged_arr[k] = arr[i]
			i += 1
		else:
			merged_arr[k] = arr[j]
			j += 1
		k += 1
	while i < mid:
		merged_arr[k] = arr[i]
		i += 1
		k +=1
	while j < rg:
		merged_arr[k] = arr[j]
		j += 1
		k +=1
	arr[lf:rg] = merged_arr
	return merged_arr


def merge_sort(arr, lf, rg):
	if rg-lf == 1:
		return arr
	mid = (rg + lf) // 2
	merge_sort(arr, lf, mid)
	merge_sort(arr, mid, rg)
	merge(arr, lf, mid, rg)
	

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

if __name__ == '__main__':
    test()