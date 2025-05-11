import numpy as np
def mult_table(nrows, ncols):
 # คืนอาเรย์ที่มี shape เป็น (nrow, ncols) ภายในเก็บตารางสูตรคูณ (ดูตัวอย่างข ้างล่าง)
    x = np.arange(1,nrows+1)
    y = np.arange(1,ncols+1)
    y =np.reshape(y,(1,ncols))
    x =np.reshape(x,(nrows,1))
    a = np.dot(x,y)
    return a
exec(input().strip()) 