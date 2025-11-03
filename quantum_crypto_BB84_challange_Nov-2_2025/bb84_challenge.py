"""
# Protocole BB84 de Distribution Quantique de Clés 

## Objectif :  
Alice et Bob souhaitent établir une clé secrète partagée en utilisant la mécanique quantique.  
Un espion (Eve) ne peut pas obtenir la clé sans introduire des perturbations détectables.  

## Étapes du protocole :  

### Procédure d'Alice :  
1) Préparation des bits du message :  
   - Générer une chaîne de bits aléatoire (ou en choisir une). Cette chaîne représente les bits à encoder.  

2) Choix des bases d'encodage :  
   - Générer une chaîne de bits aléatoire pour déterminer la base de chaque qubit.  
   - Base '0' : Base computationnelle standard { |0⟩, |1⟩ }.  
   - Base '1' : Base diagonale { |+⟩, |−⟩ }.  

3) Encodage des qubits :
   - Pour chaque bit :  
       • Si la base choisie est '0' : encoder le bit dans la base standard ('0' → |0⟩ et '1' → |1⟩).  
       • Si la base choisie est '1' : encoder le bit dans la base diagonale ('0' → |+⟩ et '1' → |−⟩).  

4) Transmission des qubits :  
   - Envoyer les qubits encodés à Bob.  

### Procédure de Bob :  
5) Choix des bases de mesure :  
   - Pour chaque qubit reçu, choisir une base aléatoire ('0' pour standard, '1' pour diagonale).  

6) Mesure des qubits :  
   - Pour la base '0' : mesurer directement dans la base standard.  
   - Pour la base '1' : mesurer dans la base diagonale.  
   - Enregistrer les résultats des mesures.  

### Comparaison des bases (Phase de tamisage ) :  
7) Réconciliation publique des bases :  
   - Alice et Bob partagent publiquement les bases qu'ils ont utilisées (sans révéler les valeurs des bits).  

8) Tamisage de la clé : 
   - Ils ne conservent que les bits où leurs bases correspondent. Cela forme la clé brute.  

### Chiffrement/Déchiffrement :  
- La clé finale est utilisée avec des schémas de chiffrement classique pour sécuriser les messages échangés.  


## II) Pourquoi cela fonctionne-t-il ?  

Si Alice et Bob utilisent la même base :  
- **Base standard (0)** : Une mesure directe donne le bit correct.  
- **Base diagonale (1)** : La porte Hadamard (H) convertit |+⟩ en |0⟩ et |−⟩ en |1⟩.  

Si les bases sont différentes :  
- Le résultat est aléatoire (50/50) et ces bits seront éliminés.  


## **III) Exemples de scénarios :**  

### **Cas 1 (Même base - Standard) :**  
- Alice envoie |0⟩ ; Bob mesure dans la base standard → Il obtient 0 (100%).  
- Alice envoie |1⟩ ; Bob mesure dans la base standard → Il obtient 1 (100%).  

### **Cas 2 (Même base - Diagonale) :**  
- Alice envoie |+⟩ ; Bob mesure dans la base diagonal → |0⟩ → Il mesure 0 (100%).  
- Alice envoie |-⟩ ; Bob mesure dans la base diagonal → |1⟩ → Il mesure 1 (100%).  

### **Cas 3 (Bases différentes) :**  
- Alice envoie |0⟩ ; Bob mesure dans la base diagonal → Résultat aléatoire 0/1 (50/50) → Ce bit est éliminé.  
- Alice envoie |1⟩ ; Bob mesure dans la base diagonal → Résultat aléatoire 0/1 (50/50) → Ce bit est éliminé.  
- Alice envoie |+⟩ ; Bob mesure dans la base standard → Résultat aléatoire 0/1 (50/50) → Ce bit est éliminé.  
- Alice envoie |-⟩ ; Bob mesure dans la base standard → Résultat aléatoire 0/1 (50/50) → Ce bit est éliminé.  

"""


import random
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

import encryption_algorithms as enc # contains the encryption and decryption algorithms

random.seed(84) # do not change this seed, otherwise you will get a different key

# Helper function:---------------------------------------
def run_circuit(circ: QuantumCircuit) -> dict:
    """
    Run a quantum circuit on the AerSimulator and return the counts
    @param circ: QuantumCircuit to run
    @return: dictionary of measurement results and their counts
    """
    simulator = AerSimulator()
    circ = transpile(circ, simulator)
    result = simulator.run(circ, shots=1001).result() # 1001 shots to get the most frequent result, so 1001 unpair number so + or - state will have at least +1 diffrent counts (so the method most_frequent work fin)
    return result.get_counts(circ)


def generate_random_binary_string(length: int=100) -> str:
    """
    Generate a random binary string of specified length
    @param length: The desired length of the binary string
    @return: String of random bits ('0' and '1')
    """
    return ''.join(random.choices(['0', '1'], k=length))

# --------------------------------------------------------
# part 1: BB84 protocol without eavesdropping (no Eve)

def alice_prepare_qubits(alice_bits:str, alice_bases:str)->list[QuantumCircuit]:
    """
    Alice prepares a list of qubits based on her bits and bases
    @param alice_bits: string of bits
    @param alice_bases: string of bases
    @return: list of QuantumCircuit objects, each representing a single qubit

    rule:
    - base choice 0: encode in standard basis |0> or |1>
    - base choice 1: encode in diagonal basis |+> or |->

    note: the length of alice_bits and alice_bases must be the same
    """
    
    qubits = [None] * len(alice_bits)



    
    #TODO: implement the qubits preparation

    return qubits



def bob_measure_qubits(qubits_from_alice:list[QuantumCircuit], bob_bases:str)->str:
    """
    Bob measures the qubits he received from Alice
    @param qubits: list of QuantumCircuit objects, each representing a single qubit
    @param bob_bases: string of bases
    @return: list of bits as bits string, each representing the measurement result of a qubit
    I know that single bit is string...
    note: the length of qubits and bob_bases must be the same
    """
    
    measurements = [None] * len(qubits_from_alice)
    
    #TODO
        
    # hint
    # when the counts of the mesurement give 50% 0 and 50% 1: you can
    # 1) choose randomly or 
    # 2) use the method most_frequent() (on dictionary) to get the most frequent result
    # We prefer the second method, because it allows to test on real NISQ device.


    return ''.join(measurements) # return the measurements as a string
    


def compare_bases(alice_bases:str, bob_bases:str) -> list[int]:
    """
    Compare Alice's and Bob's bases and return the indices of the qubits to keep

    @param alice_bases: bits string of Alice's bases
    @param bob_bases: bits string of Bob's bases

    return: list of 0s and 1s, where 0 means discard the qubit and 1 means keep the qubit
    """
    bases_to_keep = [0] * len(alice_bases)

    #TODO

    return bases_to_keep


def extract_key_from_measurements(measured_key: str, keep_mask: list[int]) -> str:
    """
    Extracts the final key from the measured bits using a mask to indicate which bits to keep.
    
    @param measured_key: A string of measurement results (e.g. "0010101101").
    @param keep_mask: A list of 0s and 1s of the same length, where 1 means that the bit is kept.
                       (Renamed from bases_to_keep for clarity.)
    @return: The extracted key as a string.
    """
    key = ''
    
    #TODO

    return key

# --------------------------------------------------------
# part 2: Eavesdropping detection

def eve_intercept_qubits(qubits: list[QuantumCircuit], eve_bases: str) -> tuple[list[QuantumCircuit], str]:
    """
    Eve intercepts the qubits:
    - For each qubit, she uses her random chosen basis (eve_bases) to measure the qubit.
    - She then re-prepares a new qubit in the state corresponding to her measurement and basis.
    Returns a new list of QuantumCircuit objects for Bob. and a bit string of the measured bits from alice.
    """
    
    measured_intercepted_qubits = [None] * len(qubits) # Eve measurement results of the qubits from alice.
    intercepted_new_qubits = [None] * len(qubits) # New qubits prepared by Eve for Bob.
    
    #TODO
    
    return intercepted_new_qubits, ''.join(measured_intercepted_qubits)


def reveal_key_subset(key: str, reveal_fraction: float = 0.2) -> tuple[str, list[int]]:
    """
    Reveals a random subset from the provided key.
    @param key: The full raw key (string of bits).
    @param reveal_fraction: The fraction of the key to reveal.
    @return: A tuple (revealed_key_subset, indices) where revealed_key_subset is the
             substring consisting of bits at the sampled indices, and indices is the list
             of those indices.
    """
    # Build the subset string based on the sampled indices (Random sampling without replacement)
    
    subset = None
    sorted_indices = None

    # TODO
    
    return subset, sorted_indices


def remove_revealed_key(full_key: str, revealed_indices: list[int]) -> str:
    """
    Removes the bits at the revealed indices from the full key, so that the remaining bits form the secret key.
    
    @param full_key: The complete raw key as a string.
    @param revealed_indices: A list of indices of the bits that were revealed publicly.
    @return: The secret key with the revealed bits removed.
    """
    # Convert the list to a set for more efficient membership testing
    revealed_set = set(revealed_indices)
    secret_key = ''.join(bit for i, bit in enumerate(full_key) if i not in revealed_set)
    return secret_key


def bob_detect_eve(bob_raw_key: str, revealed_alice: tuple[str, list[int]], threshold: float = 0.0) -> bool:
    """
    Bob detects eavesdropping by comparing the subset of his key with the corresponding subset
    of Alice's key that was revealed publicly.
    
    @param bob_key: Bob's raw key (string of bits).
    @param revealed_alice: Tuple (alice_subset, indices) obtained from reveal_key_subset called on Alice's key.
    @param threshold: The maximum allowed error rate in the revealed subset.
    @return: True if eavesdropping is suspected (error rate exceeds threshold), otherwise False.
    """

    alice_subset, indices = revealed_alice
    
    error_rate = None
    # TODO: 

    # If error rate exceeds threshold, eavesdropping is suspected.
    return error_rate > threshold , error_rate


# --------------------------------------------------------

def bb84_protocol_no_eve()->str:
    """
    SIMPLIFIED BB84 protocol for pedagogical purposes (Part 1 of the challenge).
    
    This function demonstrates the CORE CONCEPTS of BB84:
    - Quantum encoding (Z and X bases)
    - Quantum measurement
    - Basis comparison (sifting)
    
    PEDAGOGICAL NOTE: This is NOT a complete BB84 implementation!
    Missing security steps:
    - No key subset revelation for channel verification
    - No eavesdropping detection
    - Returns the full raw key (not the final secret key)
    
    Use this for learning the basics. For the COMPLETE protocol,
    use bb84_protocol_eve_is_here() which includes all security steps.
    
    @return: The raw key (before security verification)
    """
    
    numqubits = 100 # the length of the bits string

    # step 1: Alice prepares the qubits, and send them to Bob
    #         also, it send the its bases to Bob

    alice_bits:str = generate_random_binary_string(numqubits)  # k - bits to encode: out of which the key will later be formed
    alice_bases:str = generate_random_binary_string(numqubits) # b - basis choices: determines the bases in which she will encode her bits.
    
    qubits_from_alice:list[QuantumCircuit] = alice_prepare_qubits(alice_bits, alice_bases)
    
    # -----------------------------------------------------------------
    # step 2: Bob measures the qubits
    #        also, he send the its bases to Alice
    
    bob_bases:str = generate_random_binary_string(numqubits)  # b' - basis choices: determines the bases in which he will measure the qubits.

    bob_mes_res:str = bob_measure_qubits(qubits_from_alice, bob_bases)

    print("Alice's bases:", alice_bases)
    print("Bob's bases: ", bob_bases)

    # -----------------------------------------------------------------
    # step 3: Alice and Bob compare their bases
    qubits_indices_to_keep:list[int] = compare_bases(alice_bases, bob_bases)
    print("Indices to keep:", qubits_indices_to_keep)

    # -----------------------------------------------------------------
    # step 4: Alice and Bob extract the key
    key:str = extract_key_from_measurements(bob_mes_res, qubits_indices_to_keep)
    print("Key:", key)

    return key

# --------------------------------------------------------

def bb84_protocol_eve_is_here(eve_present: bool = True) -> str:
    """
    COMPLETE BB84 protocol implementation (Part 2 of the challenge).
    
    This function implements the FULL BB84 protocol with all security measures:
    1. Quantum key exchange (encoding, measuring, sifting)
    2. Key subset revelation (sacrifice 20% for verification)
    3. Eavesdropping detection (compare revealed subsets)
    4. Final secret key generation (remove revealed bits)
    
    This is the REAL BB84 protocol used in practice!
    
    @param eve_present: If True, simulates an eavesdropper (Eve) intercepting qubits
                        If False, direct transmission from Alice to Bob
    @return: The final secret key (after removing revealed bits for verification)
             Returns ~80% of the raw key (20% sacrificed for security check)
    """
    numqubits = 100  # length of the bit strings

    # step 1) Alice's preparation:
    alice_bits: str = generate_random_binary_string(numqubits)   # message bits (secret)
    alice_bases: str = generate_random_binary_string(numqubits)  # basis choices for encoding
    qubits_from_alice:list[QuantumCircuit] = alice_prepare_qubits(alice_bits, alice_bases)
    
    # step 2) Eve's interception if active:
    if eve_present:
        eve_bases: str = generate_random_binary_string(numqubits)
        qubits_from_alice,_ = eve_intercept_qubits(qubits_from_alice, eve_bases) # Eve intercepts the qubits, we keep the same varaiable name just to remain consisitant with Bob when he recive the qubits (cause he don't really know where oit come s from)

    # step 3) Bob's measurement:
    bob_bases: str = generate_random_binary_string(numqubits)  # Bob's bases for measurement
    bob_mes_res: str = bob_measure_qubits(qubits_from_alice, bob_bases) # Bob thinks he measured Alice's qubits

    print("Alice's bases:", alice_bases)
    print("Bob's bases:  ", bob_bases)
    
    # step 4) Basis comparison (Sifting Phase):
    indices_mask:list[int] = compare_bases(alice_bases, bob_bases)
    print("Indices to keep (mask):", indices_mask)
    
    
    bob_raw_key:str = extract_key_from_measurements(bob_mes_res, indices_mask)
    alice_raw_key:str = extract_key_from_measurements(alice_bits, indices_mask)

    print("Bob's raw key:  ", bob_raw_key)
    print("Alice's raw key:", alice_raw_key)
    # debug: the key must be the same for both Alice and Bob
    #assert bob_raw_key == alice_raw_key, "The keys are not the same for Alice and Bob!"

    # step 5) 
    # Alice and Bob reveal a subset of their keys to detect eavesdropping.
    # since we are working from bob side, we will reveal a subset of Alice's key.
    alice_revealed_subset_indices = reveal_key_subset(alice_raw_key, reveal_fraction=0.2) # 20% reveal rate
    
    # step 6) Eavesdropping detection (using a 20% reveal rate, threshold error rate 0% scinarion)
    eve_detected, error_rate = bob_detect_eve(bob_raw_key, alice_revealed_subset_indices, threshold=0.0) # 0% error rate threshold: simplest case => detect or not eve. if we use acceptation error rate is > 0, this mean alice and bob will not have exactly the same key (they accept some error rate in the key), so there is another step for that scinario.
    
    if eve_detected:
        print("Eavesdropping detected! (Eve intercepted the qubits)")
        print(" We will not proceed with the final key....")
        raise ValueError("Eavesdropping detected! (Eve intercepted the qubits)")
        return None
    
   # If no eavesdropping detected, proceed with the final key.
    print("No eavesdropping detected.")
    
    # For final key, remove or discard the revealed bits.
    secrect_key:str = remove_revealed_key(bob_raw_key, alice_revealed_subset_indices[1])
   
    print("Final key:", secrect_key)
    return secrect_key

# --------------------------------------------------------


# =========================================================
# Funtion hleper decrypt multiple messages with the generated key

def decrypt_and_print_messages(key: str, filename: str = "encrypted_messages.txt"):
    """
    Read encrypted messages from a file, decrypt them using XOR with the given key, and print.

    Args:
        key (str): The key to use for XOR decryption.
        filename (str): The file to read encrypted messages from.
    """
    print("\nDecrypting all messages from", filename)
    with open(filename, "r") as f:
        for line in f:
            if ": " in line:
                msg_id, encrypted = line.split(": ", 1)
                decrypted = enc.decrypt_xor_repeating_key(encrypted.strip(), key)
                print(f"{msg_id}: {decrypted}")

# =========================================================

def main():

    key = bb84_protocol_no_eve() # part 1: BB84 protocol without eavesdropping (no Eve)
    
    # TODO: comment the line above and uncomment the line below to test the BB84 protocol with eavesdropping (Eve)
    #key = bb84_protocol_eve_is_here(eve_present=True) # part 2: BB84 protocol with eavesdropping (Eve)

    print(" Final key length:", len(key))
    print(" Key:", key)

    # step 5: alice encrypts a message with the key
    print(" xor_repeating_key encryption: ----------------")
    message = enc.message_test1
    print("Message:", message)
    message_encrypted = enc.encrypt_xor_repeating_key(message, key)
    print("Encrypted message:", message_encrypted)

    # step 6: Bob decrypts the message with the key
    message_decrypted = enc.decrypt_xor_repeating_key(message_encrypted, key)
    print("Decrypted message:", message_decrypted)

    """
    print(" caesar_cipher encryption: ----------------")
    message_encrypted = enc.encrypt_caesar_cipher(message, key)
    message_decrypted = enc.decrypt_caesar_cipher(message_encrypted, key)
    print("Encrypted message:", message_encrypted)
    print("Decrypted message:", message_decrypted)
    """

    # Decrypt multiple messages from file
    # using the generated key part 1:
    print("\nDecrypting multiple messages from file -> Part 1")
    decrypt_and_print_messages(key, filename="Shacks UdeS/quantum_crypto_BB84_challange/encrypted_messages_part1.txt")

    # using the generated key part 2:
    print("\nDecrypting multiple messages from file -> Part 2")
    decrypt_and_print_messages(key, filename="Shacks UdeS/quantum_crypto_BB84_challange/encrypted_messages_part2.txt")


if __name__ == "__main__":
    main()
