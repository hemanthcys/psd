import pytest
from sparse_recommender import SparseMatrix

def test_set_and_get():
    sparse_matrix=SparseMatrix()
    sparse_matrix.set(0, 0, 1)
    sparse_matrix.set(0, 1, 2)
    sparse_matrix.set(1, 1, 3)
    value_00=sparse_matrix.get(0, 0)
    value_01=sparse_matrix.get(0, 1)
    value_11=sparse_matrix.get(1, 1)
    assert value_00==1
    assert value_01==2
    assert value_11==3
    value_22=sparse_matrix.get(2, 2)  
    value_02=sparse_matrix.get(0, 2) 
    assert value_22==0
    assert value_02==0

def test_recommend():
    sparse_matrix=SparseMatrix()
    sparse_matrix.matrix={0: {0: 1, 1: 2}, 1: {1: 3}}
    vector=[2, 3]
    result=sparse_matrix.recommend(vector)
    assert result==[8, 9]

def test_add_movie_complex():
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
    expected_result={
        0: {0: 1, 1: 6, 2: 0},
        1: {0: 0, 1: 3, 2: 5},
        2: {0: 6, 1: 0, 2: 4}
    }
    assert sparse_matrix1.matrix==expected_result

def test_to_dense():
    sparse_matrix=SparseMatrix()
    sparse_matrix.matrix={0: {0: 1, 1: 2}, 1: {1: 3}}
    dense_matrix=sparse_matrix.to_dense()
    expected_result=[[1, 2], [0, 3]]
    assert dense_matrix==expected_result
