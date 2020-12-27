# Restituisce un nodo
def nodo(x, s, d):
	return [x, s, d]

# Restituisce una foglia
def foglia(x):
	return [x, None, None]

# Restituisce l'albero vuoto
def vuoto():
	return None

# Restituisce il valore della radice
def radice(A):
	return A[0]

# Restituisce il sottoalbero sinistro
def sinistro(A):
	return A[1]

# Restituisce il sottoalbero destro
def destro(A):
	return A[2]

# Restituisce True se è vuoto
def isVuoto(A):
	return A is None

# Restituisce True se è una foglia
def isFoglia(A):
	return isVuoto(sinistro(A)) and isVuoto(destro(A))

def max_sx(A):
	if isVuoto(destro(A)):
		# Se il nodo non ha un sottoalbero destro, il massimo sta nella radice
		return radice(A)
	# Chiamo ricorsivamente sul sottoalbero destro
	return max_sx(destro(A))

def min_dx(A):
	if isVuoto(sinistro(A)):
		# Se il nodo non ha un sottoalbero sinistro, il minimo sta nella radice
		return radice(A)
	# Chiamo ricorsivamente sul sottoalbero sinistro
	return min_dx(sinistro(A))

def m(A):
	# Solo se l'albero non è vuoto e non è una foglia posso calcolare la media richiesta
	if not isVuoto(A):
		if not isFoglia(A):
			# Richiamo le funzioni desiderate e restituisco la media dei due valori
			max_sinistro = max_sx(sinistro(A))
			min_destro = min_dx(destro(A))
			return (max_sinistro + min_destro)/2
# Test richiesti del progetto
E1 = nodo(2, nodo(1, foglia(0), vuoto()), foglia(3))
E2 = nodo(8, nodo(7, foglia(6), vuoto()), foglia(9))
A = nodo(5, E1, E2)
print(m(A))

