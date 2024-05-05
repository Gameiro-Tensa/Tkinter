import numpy as np


def sigmoid(z):
    """Sigmoid-Funktion"""
    return 1 / (1 + np.exp(-z))


def initialize_parameters(dim):
    """Initialisiert die Gewichte und den Bias"""
    w = np.zeros((dim, 1))
    b = 0
    return w, b


def propagate(w, b, X, Y):
    """Berechnet die Kosten und die Gradienten"""
    m = X.shape[1]

    # Vorwärtsberechnung (von Input zu Ausgabe)
    A = sigmoid(np.dot(w.T, X) + b)
    cost = -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))

    # Rückwärtsberechnung (Gradienten)
    dw = 1 / m * np.dot(X, (A - Y).T)
    db = 1 / m * np.sum(A - Y)

    cost = np.squeeze(cost)
    grads = {"dw": dw,
             "db": db}

    return grads, cost


def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost=False):
    """Optimiert die Parameter w und b durch Gradientenabstieg"""
    costs = []

    for i in range(num_iterations):

        # Berechne die Kosten und Gradienten
        grads, cost = propagate(w, b, X, Y)

        # Aktualisiere die Parameter
        w -= learning_rate * grads["dw"]
        b -= learning_rate * grads["db"]

        # Speichere die Kosten alle 100 Iterationen
        if i % 100 == 0:
            costs.append(cost)

        # Ausgabe der Kosten
        if print_cost and i % 100 == 0:
            print("Kosten nach Iteration {}: {}".format(i, cost))

    params = {"w": w,
              "b": b}

    grads = {"dw": grads["dw"],
             "db": grads["db"]}

    return params, grads, costs


def predict(w, b, X):
    """Klassifiziert die Eingabedaten"""
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))

    # Vorhersage
    A = sigmoid(np.dot(w.T, X) + b)

    # Rundet die Vorhersage auf 0 oder 1
    for i in range(A.shape[1]):
        Y_prediction[0, i] = 1 if A[0, i] > 0.5 else 0

    return Y_prediction


# Kombiniert alle Funktionen in ein Modell
def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    """Logistische Regression Modell"""
    # Initialisiere die Parameter
    w, b = initialize_parameters(X_train.shape[0])

    # Gradientenabstieg
    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)

    # Extrahiere die Parameter
    w = parameters["w"]
    b = parameters["b"]

    # Vorhersage für die Trainings- und Testdaten
    Y_prediction_train = predict(w, b, X_train)
    Y_prediction_test = predict(w, b, X_test)

    # Auswertung der Genauigkeit
    print("Trainingsgenauigkeit: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("Testgenauigkeit: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    # Rückgabe der Ergebnisse
    d = {"Kosten": costs,
         "Trainingsvorhersage": Y_prediction_train,
         "Testvorhersage": Y_prediction_test,
         "w": w,
         "b": b,
         "Lernrate": learning_rate,
         "Anzahl Iterationen": num_iterations}

    return d
