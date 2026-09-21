# Gram-Schidmt Successive Orthogonalization 

Lets assume for this example we have no intercept and two feature columns $x_1$ and $x_2$. We fit a linear model of the form

$$
y = \beta_1x_1 + \beta_2x_2 + \epsilon
$$

We want to find $\hat{\beta_1}$ and $\hat{\beta_2}$ such that 


$$
\hat{y} = \hat{\beta_1}x_1 + \hat{\beta_2}x_2
$$

Each column vector $y,\hat{y},\beta_1,\beta_2$ can be intepreted geometrically. Each of these column vectors are vectors in n-dimensional ambient space, where n is the number of observations in our dataset.

$$
y,\hat{y},\beta_1,\beta_2 \in \mathbb{R}^n
$$

In Gram-Schimdt, we are trying to find a new orthogonal basis for our column space.
Lets set the first column vector as the direction of our first orthogonal basis, and lets call this $z_1$.
$$
z_1 = x_1
$$

We then project our second column vector $x_2$ on our first orthogonal basis vector $z_1$. This projected vector $\operatorname{proj}_{z_1}(x_2)$ is given by 
$$
proj_{z_1}x_2 = \frac{z_1 \cdot x_2}{z_1 \cdot z1} z_1
$$

Lets also define the vector orthogonal to the $proj_{z_1}x_2$ as $z_2$.
Since 
$$
proj_{z_1}x_2 + z_2 = z_1
$$
$$
z_2 = z_1 - proj_{z_1}x_2 
$$

By construction, $z_1$ and $z_2$ are orthogonal. To construct our OLS equation with our new orthogonal basis, we project our target vector $y$ onto each of our new orthogonal basis vectors $z_1$ and $z_2$.

$$
proj_{z_1}y = \frac{z_1 \cdot y}{z_1 \cdot z1} z_1
$$

$$
proj_{z_2}y = \frac{z_2 \cdot y}{z_2 \cdot z2} z_2
$$

Here we define 
$
\frac{z_1 \cdot y}{z_1 \cdot z1}
$
as $\hat{\alpha_1}$ and
$
\frac{z_2 \cdot y}{z_2 \cdot z2}
$ as $\\hat{alpha_2}$, where both $\hat{\alpha}_1$ and $\hat{\alpha}_2$ are scalars.
(Although I do know the ESL textbook defines them as $\beta_1$ and $\beta_2$ but I want to contrast these coefficients from the regular OLS coefficients later.)

Just like how a vector in space can be broken down into its resulting sum of two of its orthogonal vectors, we can sum up both our projection vectors on their respective orthogonal basis to yield $\hat{y}$ . This is because both $proj_{z_1}y$ and $proj_{z_2}y$ are orthogonal to each other.

$$
\hat{y} = proj_{z_1}y + proj_{z_2}y = \frac{z_1 \cdot y}{z_1 \cdot z1} z_1 + \frac{z_2 \cdot y}{z_2 \cdot z2} z_2 = \alpha_1 z_1 + \alpha_2 z_2
$$

The equation
$$
\hat{y} = \hat{\alpha_1} z_1 + \hat{\alpha_2} z_2
$$ looks
similar to the regular OLS equation
$$
\hat{y} = \hat{\beta_1} x_1 + \hat{\beta_2} x_2
$$
when put side-by-side.

The difference in both equations is that our feature columns vectors have changed. Thus the projection of y onto our column vectors have changed as well. This means both equations have to be interpeted differently.

Here $x_1$ and $x_2$ are our original column vectors while $z_1$ and $z_2$ are our new orthogonal basis vectors. The scalars $\hat{\alpha_j}$ scale their respective $z_j$'s to form the projection of $y$ onto these orthogonal directions. The sum of these projection vectors gives the point in $span(z_1,z_2)$ that is closest to $y$. By construction, $z_1$ and $z_2$ are themselves mutually orthogonal.

Similarly the scalars $\hat{\beta}_j$ scale their respective column vectors $x_j$'s to form the fitted vector $\hat{y}$. When the $x_j$'s are mutually orthogonal, each term $\hat{\beta}_j x_j$ can also be intepreted as the individual projection of $y$ onto the direction $x_j$, and these projection vectors can be summed to obtained the projection of $y$ onto $span(x_1,x_2)$. However, when the $x_j$'s are not orthogonal, the coefficients $\hat{\beta}_j$ must be determined jointly, and the individual projections of $y$ onto each $x_j$ cannot simply be added to obtain the projection of $y$ onto the $span(x_1,x_2)$.

Key: The projection vector $\hat{y}$ onto a span (span($x_j$'s) or span($z_j$'s)) is not generally equal to the sum of the $y$ projections onto the spanning vectors unless those vectors are orthogonal.

That said, the column space spanned by the $z_j$'s will be the same as column space spanned by the $x_j$'s. Gram-Schmidt finds a new orthogonal basis for the same column space.

The fitted vector $\hat{y}$ is a function of the target vector $y$ and column space onto which $y$ is projected onto. The scalar coefficients are a function of the particular basis used to represet that column space.

## Intepretation of the linear equation from Gram-Schmidt
From Gram-Schmidt, we obtain the equation

$$
\hat{y} = \hat{\alpha}_1 z_1 + \hat{\alpha}_2 z_2
$$

Here, $z_1$ and $z_2$ represents our new orthogonal basis of the column space spanned by $x_1$ and $x_2$. That also means that our intepretation of this equation will be different from

$$
\hat{y} = \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2
$$

In this example, we set $z_1 = x_1$ so both $z_1$ and $x_1$ represent the same feature column vector. However, $z_2$ is the residual vector after $x_2$ is orthogonalized with respect to $z_1$. That is, we extract the vector $z_2$ which represents the component of $x_2$ that is not already contained in the direction spanned by $z_1$. $z_2$ is the resultant vector when $x_2$ is adjusted for $z_1$, or is 'orthogonalized' with respect to $z_1$, as per ESL's notation.

As the coefficients $\hat{\alpha}_j$'s depend on the particular basis used to represent the column space, their interpretation differs from that of the original regression coefficients $\hat{\beta}_j$'s.

Geometrically, $\hat{\alpha}_j$ scales the orthogonalized basis vector $z_j$, while $\hat{\beta}_j$ scaled the orginal feature vector $x_j$.

In an applied regression context,



## When our column vectors are already orthogonal to each other

## When we include the intercept in our linear equation


* ESL refers to the Elements of Statistical Learning textbook