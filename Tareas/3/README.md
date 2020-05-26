# Expectation-Maximization

## Algoritmo

1. Inicializar <math>$p(w|\theta_d)$</math> con valores aleatorios
2. Mientras verosimilitud no cambie:
    1. Mejorar esa inicialización de forma iterativa usando paso-E y paso-M

### Paso-E

$$
p^{(n)}(z = 0 | w) = \frac{p(\theta_d) * p^{(n)}(w|\theta_d)}{p(\theta_d) * p^{(n)}(w | \theta_d) + p(\theta_B) * p(w| \theta_B)}
$$

### Paso-M

$$
p^{(n+1)}(w | \theta_d) = \frac{count(w, d) p^{(n)}(z = 0 | w)}{\sum_{w' = w_1}^{w_M}count(w', d) p^{(n)}(z = 0 | w')}
$$

## Ejemplo

d = "w1 w1 w1 w1 w2 w2 w3 w3 w3 w3 w4 w4"

\begin{array}{|c|c|}
Palabra & count & p(w | \theta_B) & p^{(1)}(w | \theta_d) & p^{(1)}(z = 0 | w)&p^{(2)}(w | \theta_d)&p^{(2)}(z = 0 | w)\\
w_1&  4&  0.5&  0.25&  0.33&  0.20\\
w_2&  2&  0.3&  0.25&  0.45&  0.14\\
w_3&  4&  0.1&  0.25&  0.71&  0.44\\
w_4&  2&  0.1&  0.25&  0.71&  0.22
\end{array}

*Tarea: Resolver la tabla hasta n = 6 y programar ambas fórmulas*

## Desarrollo

[Jupyter Notebook](./Expectation_Maximization.ipynb)