## Definition chaîne de Markov 

### Def 
Une chaîne de Markov est un processus aléatoire vérifiant la propriété de Markov.
Dit simplement, la probabilité de passer d'un état $X_n$ à $X_{n+1}$ ne dépend que de $X_n$.
La chaîne de Markov posséde espace d'état fini ou dénombrables $\mathfrak{X}$, tel que pour $\alpha$ et $ \beta \in \mathfrak{X}$, il existe une probabilité $ \mathcal{P}(\beta|\alpha) \in [0,1]$, de passage de l'état $\beta$ sachant $\alpha$, autrement dit, il s'agit de la probabilité que l'état $\alpha$ passe à l'état $\beta$.

## Matrice / Graphe

### Matrice

Nous pouvons représenter les probabilités de passage à l'état $\beta$ sachant $\alpha$ avec une matrice dite de transition P, ou donc $P_{α,ꞵ}$ représente $ \mathcal{P}(\beta|\alpha)$ 
On peut aussi noter $P_{i, j}$ avec $i, j \in \llbracket 1,N \rrbracket$ ou $P_{i, j}$ avec $i, j \in \llbracket 1,+\infty \llbracket$ 
selon si le nombre d'états est fini et égal à $N \in \N$, ou infini dénombrable, avec $i$ et $j$ les "indices" de $\alpha$ et $\beta$.  
Cette matrice est toujours une matrice Stochastique, qui a donc comme propriété pour chacune de ses lignes, que la somme des élément est égal à 1.

Ou de façon plus imager avec une chaîne de Markov à N états :  

Avec la matrice de transition $
P = \begin{bmatrix}
P_{1,1} & P_{1,2} & ... & P_{1,N}\\
P_{2,1} & P_{2,2} & ... & P_{2,N}\\
\vdots & &\ddots & \vdots\\
P_{N,1} & P_{N,2} & ... & P_{N, N}\\
\end{bmatrix} \in \mathcal{M}([0,1]) \\
\forall i \in [1,N] : P_{i,1} + P_{i,2} + \dots + P_{i, N} = 1 \space \text{ou écrit autrement} \space  \forall i \in [1,n]: \sum_{j = 1}^n P_{i j} = 1
$ 

### Graphe

Il est relativement naturel de représenter la matrice de transition d'une chaîne de Markov par un graphe orienté, 
nous permettant de visuellement voir les probabilités de transitions entres les états.
Par exemeple, dans le cas d'une chaîne de Markov disposant de 3 états $\alpha , \beta$ et $\gamma $, ordonnés respectivement, avec la matrice de transition $\\
P = \begin{bmatrix}
0,1 & 0,4 & 0,4 \\
0,6 & 0,4 & 0 \\
0,1 & 0,1 & 0,8\\
\end{bmatrix}
$

Avec donc $ P_{\alpha,\beta} = P_{1,2} = \mathcal{P}(\beta|\alpha) = 0,4$.  
Et donc le graphe suivant :
$
\begin{pspicture}(-2,-2)(3,3.5)
   \psset{dotsize=0.2,labelsep=0.05,nodesep=0.1,unit=0.6,shortput=nab,arrows=->,arrowsize=0.3}
      \dotnode(0,0){p} \uput[d](0.4,-0.6){pluie}
      \dotnode(5,0){s} \uput[r](5.3,0){soleil}
      \dotnode(2.5,4){n} \uput[r](3,4){neige}
      \ncarc[arcangle=20]{p}{s}^{\textcolor{blue}{{\footnotesize $0,25$}}}
      \ncarc[arcangle=20]{s}{p}^{\textcolor{blue}{{\footnotesize $0,5$}}}
      \ncarc[arcangle=20]{p}{n}^{\textcolor{blue}{{\footnotesize $0,25$}}}
      \ncarc[arcangle=-20,arrows=<-]{p}{n}^{\textcolor{blue}{{\footnotesize $0,25$}}}
      \nccircle{n}{.5cm}^{\textcolor{blue}{{\footnotesize $0,5$}}}
      \nccircle[angle=90]{p}{.5cm}^{\textcolor{blue}{{\footnotesize $0,5$}}}
      \ncarc[arcangle=20]{n}{s}^{\textcolor{blue}{{\footnotesize $0,25$}}}
      \ncarc[arcangle=20]{s}{n}^{\textcolor{blue}{{\footnotesize $0,5$}}}
   \end{pspicture}
$