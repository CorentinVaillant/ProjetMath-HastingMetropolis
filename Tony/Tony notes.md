% TOUT CE QUI SUIT NE SERA PAS DANS LE RENDU FINAL TEL QUEL : A RETRAVAILLER
\section{DESCRIPTION DE L'ALGO (ce qu'on a compris)}

(Tony, je marque ici ce que j'ai compris) \textbf{Pourquoi a-t-on besoin de HM ?} \\
Partons d'une distribution de points donnés dans un graphique avec autant de dimensions que l'on veut. Cela peut être une gaussienne, une intégrale, une estimation bayésienne... Imaginons ensuite que cette distribution ne peut pas être réprésentée facilement (trop de dimentions, intégrale incalculable). Nous voudrions calculer l'espérence de cette distribution mais comme nous ne savons pas à quoi elle ressemble, il est difficile d'appliquer cette méthode de calcul. \\

Espérance analytique : \\
1 - definition générale \url{https://fr.wikipedia.org/wiki/Espérance_mathématique}\\
Si la variable aléatoire continue réelle \( X \) admet une densité de probabilité \( f \), son espérance est définie comme :
\[
\mathbb{E}[X] = \int_{-\infty}^{\infty} x f(x) \, dx,
\]
à condition que l'intégrale soit absolument convergente. \\

2 - chatgpt qui donne une formule équivalente plus adaptée à la forme utilisée habituellement pour HM, car plus générale
\[
\mathbb{E}[f(x)] = \int f(x) P(x) \, dx
\]

Avec \(f(x)\) une fonction quelconque (si \(f(x) = x\) c'est l'espérence simple ou si \(f(x) = x^2\) il s'agit de la variance, etc.) et \(P(x)\) la densité de probabilité. \\

Ces deux formules sont difficiles (voire impossible) à calculer explicitement dans des espaces de grande dimension ou pour des distributions \( P(x) \) complexes. Il faut alors \textbf{échantillonner} pour utiliser l'autre formule. \\

Estimation empirique :
\[
\mathbb{E}[g(x)] \approx \frac{1}{N} \sum_{i=1}^N g(x_i), \quad x_i \sim P(x)
\]

On génère \( N \) échantillons \( x_i \) indépendants selon \( P(x) \).  
L'espérance est estimée par la moyenne des évaluations de \( g(x_i) \) sur ces échantillons. \\

On comprend donc l'importance de réaliser des échantillonages sur les distributions étudiées, cela sert à analyser en profondeur ces distributions. \\


\textbf{En quoi HM est plus optimisé que les autres méthodes d'échantillonages ?} \\
De ce que j'ai compris, on peut représenter HM comme une chaine de Markov dans laquelle on ne connait pas vraiment les états, on peut seulement tirer au hasard une valeur parmi 










\section{CHOSES A FAIRE}

Définir ce qu'est un échantillonnage en général => c'est ce que fait HM \\
Faire le lien entre échantillongage optimisé et les méthodes MCMC \\