import sys
input = sys.stdin.readline

def main():
   up, down, stick=list(map(int, input().split()))
   cnt=0
   now=0
   #print(up,down,stick)

   day=up-down
   bf_stick=stick-up

   if(bf_stick%day==0):
       cnt=(bf_stick//day)+1
   else:
       cnt=(bf_stick//day)+2
   print(cnt)

if __name__ == "__main__":
    main()