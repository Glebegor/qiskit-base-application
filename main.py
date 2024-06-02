from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QiskitError
from qiskit_ibm_provider import IBMProvider

from dotenv import load_dotenv
import os

load_dotenv()
# IBMProvider.save_account(token=os.getenv("IBMQ_API_KEY"))
provider = IBMProvider(token=os.getenv("IBMQ_API_KEY"))
# provider = IBMProvider()
# service = QiskitRuntimeService(channel="ibm_quantum", token=)