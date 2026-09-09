# Notes of solving OLS
Normal eqns
Gradient descent

## Normal eqn
- Design matrix is a transformed predictor matrix

- Perfect multicollinearity prevents $(X^T X)^{-1}$ from being invertible



## General Notes
- The existence of multicollinearity affects stability of coefficients
    - test degree of multicollinearity in design matrix vs variance of coefficients 
- For OLS uniqueness, we do not need zero multicollinearity. Just need to avoid perfect multicollinearity. High but imperfect multicollinearity still gives a unique OLS solution, though coefficients can become unstable.
- Generally, higher degree of multicollinearity means higher variance in OLS estimates. $(X^T X)^{-1}$ becomes closer to singular
- Multicollinearity affects the size/stability of $(X^T X)^{-1}$
- Heteroskedasticity means the simple $\sigma^2(X^T X)^{-1}$ variance formula is wrong