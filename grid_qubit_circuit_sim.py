import cirq
import matplotlib.pyplot as plt

#function to create and simulate a quantum circuit that is simulated 100 times
def simulate_quantum_circuit(repetitions=100):
    #pick grid qubit
    qubit = cirq.GridQubit(0, 0)

    #create a circuit
    circuit = cirq.Circuit(
        cirq.X(qubit)**0.5,  #square root of NOT.
        cirq.measure(qubit, key='m')  #measurement.
    )

    #simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=repetitions)

    #return the circuit and the measurement results
    return circuit, result

#function that uses matplotlib to plot the measurement results
def plot_results(circuit, result):
    #print the circuit
    print("Circuit:")
    print(circuit)

    #get measurement results
    data = result.data['m']

    #count the frequency of each measurement outcome
    counts = data.value_counts().sort_index()

    #plot should show ~50% 0s and ~50% 1s
    plt.bar(counts.index, counts.values, tick_label=counts.index)
    plt.xlabel('Measurement Outcome')
    plt.ylabel('Frequency')
    plt.title('Measurement Outcomes of the Quantum Circuit')
    plt.show()

#main function definition
def main():
    circuit, result = simulate_quantum_circuit(repetitions=100)
    plot_results(circuit, result)

#run main function
if __name__ == '__main__':
    main()
