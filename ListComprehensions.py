if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print[[i,j,k]for i in range(x+1) if(i+j+k != n)]
print[[i,j,k]for j in range(y+1) if(i+j+k != n)]
print[[i,j,k]for k in range(z+1) if(i+j+k != n)]
