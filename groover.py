from qiskit import QuantumCircuit
from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate
import math

from qiskit import QuantumCircuit
def grover_algo(n,t):
 
 n_controls = n-1
 N = 2 ** n
 num_iter=math.floor((math.pi / 4) * math.sqrt(N ))
 total_qubits = n_controls + 1


 oracle = QuantumCircuit(total_qubits, name='oracle')
 for i in range(len(t)):
  if t[i]=="0":
   oracle.x(i)
 cz = ZGate().control(n_controls)
 
 oracle.append(cz, list(range(total_qubits)))
 for i in range(len(t)):
  if t[i]=="0":
   oracle.x(i)

 oracle_df = QuantumCircuit(total_qubits, name='oracle_df')
 oracle_df.h(range(n))

    # Step 2: Apply X to all qubits
 oracle_df.x(range(n))
 cz = ZGate().control(n_controls)
 oracle_df.append(cz, list(range(total_qubits)))
    # Step 4: Apply X to all qubits
 oracle_df.x(range(n))
 oracle_df.h(range(n))

 



 grover_circ = QuantumCircuit(n,n)
 for i in range(n):
  grover_circ.h(i)
 for i in range(num_iter): 
  grover_circ.compose(oracle, inplace=True)
  grover_circ.compose(oracle_df, inplace=True)

 grover_circ.measure(range(n), reversed(range(n)))
 return grover_circ
grover_cc=grover_algo(7,"0001000")
grover_cc.draw("mpl")

from qiskit_aer import Aer
from qiskit import transpile
from qiskit.visualization import plot_histogram
from qiskit.visualization import plot_distribution

backend = Aer.get_backend('aer_simulator')
grover_circ = transpile(grover_cc, backend)
result = backend.run(grover_circ, shots=1024).result()
counts = result.get_counts()
plot_distribution(counts)
