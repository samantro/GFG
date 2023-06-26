def nCr(n, r):
        if r>n:
            return 0
        else:
            num=1
            deno=1
            x=n
            y=r
            for i in range(r):
                num=num*x
                deno=deno*y
                x-=1
                y-=1
        return (num//deno)%((10**9)+7)