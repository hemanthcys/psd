class SparseMatrix:
    
    def __init__(self):
        self.matrix={}

    def set(self,row,col,value):
        if row not in self.matrix:
            self.matrix[row]={}
        self.matrix[row][col]=value

    def get(self,row,col):
        if row in self.matrix and col in self.matrix[row]:
            return self.matrix[row][col]
        else:
            return 0
         
    def recommend(self,vector):
        result=[]
        for r in self.matrix:
            r_result=0
            for c,v in self.matrix[r].items():
                r_result+=vector[c]*v
            result.append(r_result)
        return result

    def add_movie(self,matrix):
        for r in matrix.matrix:
            if r not in self.matrix:
                self.matrix[r]={}
            for c, v in matrix.matrix[r].items():
                if c not in self.matrix[r]:
                    self.matrix[r][c]=0
                self.matrix[r][c]+=v

    def to_dense(self):
        max_row=max(self.matrix.keys()) if self.matrix else 0
        max_col=max(max(self.matrix[r].keys()) for r in self.matrix) if self.matrix else 0
        dense_matrix=[[0 for _ in range(max_col+1)] for _ in range(max_row+1)]
        for r in self.matrix:
            for c,v in self.matrix[r].items():
                dense_matrix[r][c]=v
        return dense_matrix

sparse_matrix=SparseMatrix()
sparse_matrix.set(0, 0, 1)
sparse_matrix.set(0, 1, 2)
sparse_matrix.set(1, 1, 3)
value_00=sparse_matrix.get(0, 0)  
value_01=sparse_matrix.get(0, 1) 
value_11=sparse_matrix.get(1, 1)  
print(value_00,value_01,value_11)

sparse_matrix0=SparseMatrix()
sparse_matrix0.matrix={0: {0: 1, 1: 2}, 1: {0:0, 1: 3}}
vector=[2, 3]
recommendations=sparse_matrix0.recommend(vector)
print(recommendations)


sparse_matrix1=SparseMatrix()
sparse_matrix1.matrix={
        0: {0: 1, 1: 2, 2: 0},
        1: {0: 0, 1: 3, 2: 0},
        2: {0: 0, 1: 0, 2: 4}
    }
sparse_matrix2=SparseMatrix()
sparse_matrix2.matrix={
        0: {0: 0, 1: 4, 2: 0},
        1: {0: 0, 1: 0, 2: 5},
        2: {0: 6, 1: 0, 2: 0}
    }
sparse_matrix1.add_movie(sparse_matrix2)
print(sparse_matrix1.matrix)