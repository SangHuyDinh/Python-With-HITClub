import def_multi_two_matrix
# def int_to_string(string):
#     return list(int(i) for i in (string.split()))
    
def input_matrix(number_rows):
    return list(list(map(int,input().split())) for i in range(number_rows))
if __name__=='__main__':
    n, m ,p = map(int,input().split())
    print(def_multi_two_matrix.multi(list(input_matrix(n)),list(input_matrix(m))))

