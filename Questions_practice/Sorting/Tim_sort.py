''' Tim Sort : 
    We divide the Array into blocks known as Run. ( merge sort )
    We sort those runs using insertion sort one by one and then merge those runs
    using the combine function used in merge sort. 
    If the size of the Array is less than run, then Array gets sorted just by using 
    Insertion Sort. 
    The size of the run may vary from 32 to 64 depending upon the size of the array. 
    Note that the merge function performs well when size subarrays are powers of 2. 
    The idea is based on the fact that insertion sort performs well for small arrays.
'''
