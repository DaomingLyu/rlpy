from Tools import *
from Representations import *
from Domains import *
import timeit
from scipy.sparse.linalg import *
from scipy.linalg import *

def randomSparse(M_size,Elems):
    o = random.rand(Elems)
    rows = random.random_integers(0,M_size-1,Elems)
    cols = random.random_integers(0,M_size-1,Elems)
    M = sp.csc_matrix((o,(rows,cols)),shape=(M_size,M_size))
    b = random.rand(M_size,1)
    return M,b

REGULARIZATION = .01
M_size = 1000
Sparsity = 92# Percentage of the matrix that is empty
Elems  = (M_size*M_size*(1-Sparsity/100.))/1
print 'Matrix size = %dx%d' % (M_size,M_size)
print 'Elements = %d' % (Elems)
Methods = ['spsolve(A,b, use_umfpack = True), 0',
           'spsolve(A,b, use_umfpack = False), 0', 
           'spsolve(A,b, permc_spec = 0), 0',
           'spsolve(A,b, permc_spec = 1), 0',
           'spsolve(A,b, permc_spec = 2), 0',
           'spsolve(A,b, permc_spec = 3), 0',
           'lsmr(A,b)',
         'lsmr(A,b,damp = REGULARIZATION, atol = 0, btol = 0, conlim = 0, maxiter = 10000)',
         'lsqr(A,b)',
         'lsqr(A,b,damp = REGULARIZATION, atol = 0, btol = 0, conlim = 0)',
         'lstsq(A.todense(),b)'
         ]
#Methods = ['spsolve(A,b, use_umfpack = True), 0',
#           'spsolve(A,b, use_umfpack = False), 0',
#           'spsolve(A,b, permc_spec = 0), 0',
#           'spsolve(A,b, permc_spec = 1), 0',
#           'spsolve(A,b, permc_spec = 2), 0',
#           'lsmr(A,b)',
#         'lsmr(A,b,damp = REGULARIZATION, atol = 0, btol = 0, conlim = 0, maxiter = 10000)',
#         'lsqr(A,b)',
#         'lsqr(A,b,damp = REGULARIZATION, atol = 0, btol = 0, conlim = 0)',
#         'bicg(A,b)',
#         'qmr(A,b)',
#         'lstsq(A.todense(),b)'
#         ]
for i,m in enumerate(Methods):
    print "==============\nMethod =", m
    statement = "A,b = randomSparse(M_size,Elems); x = %s; print 'Error = %%.2e' %% linalg.norm((A*x[0].reshape(-1,1) - b.reshape(-1,1))[0])" % m
    t = timeit.Timer(stmt=statement,setup="from __main__ import *; random.seed(999)")
    print t.timeit(number=1) 

