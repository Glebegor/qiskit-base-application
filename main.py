# Qiskit import
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QiskitError, transpile
from qiskit_ibm_provider import IBMProvider
from qiskit.visualization import circuit_drawer

# Load environment variables
from dotenv import load_dotenv
import os

load_dotenv()
imageFolder = "images/"

# Load IBM Quantum Experience provider
provider = IBMProvider(token=os.getenv("IBMQ_API_KEY"))
print(provider.backends())

# Helper functions
def saveQuantumCircuit(qc: QuantumCircuit, name: str):
    qc.draw(output='mpl', filename=imageFolder + name + '.png')
    return name + '.png'
def getBackend():
    return provider.get_backend("ibm_kyoto")

# Quantum Applications
def quantumHelloWorld():
    # Create a Quantum Circuit acting on the 2 register
    qc = QuantumCircuit(4)

    # Add a H gate on qubit 0
    qc.h(0)

    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1
    qc.cx(0, 1)

    saveQuantumCircuit(qc, 'quantum_hello_world')
    return qc
def testApp():
    # Create a Quantum Circuit acting on the 2 register
    qc = QuantumCircuit(4)

    qc.h(0)
    qc.cx(3, 0)
    qc.h(2)
    qc.cx(0, 1)

    saveQuantumCircuit(qc, 'testApp')
    return qc

def main():
    currBackend  = getBackend()
    transpiled_qc = transpile(testApp(), currBackend)
    job = currBackend.run(transpiled_qc)
    print(f"Job ID: {job.job_id()}")
    result = job.result()
    print(result.get_counts(transpiled_qc))

if __name__=="__main__":
    main()
