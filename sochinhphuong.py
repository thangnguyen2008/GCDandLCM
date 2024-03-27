def find_square_number(n):
    #flag = 1 => số chính phương
    #flag = 0 => không phải số chính phương

    flag = 0;
    #Tìm số bất kỳ nhỏ hơn hoặc bằng n mà bình phương bằng n
    if any(i**2 == n for i in range(n+1)):
        flag = 1
    return flag
n = int(input())
if flag == 1:
  print("True")
else:
  print("False")
