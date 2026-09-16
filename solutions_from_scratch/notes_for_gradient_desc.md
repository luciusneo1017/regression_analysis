How to find the best learning rate with respect to feature size so GD doesnt overshoot the min?
-> theorectically optimal fixed learning rate

TODO : research the relationship between the learning rate and size of features

# gradient_descent_high_multicollinearity.ipynb
1. GD on raw Longley data
-> divergence / overflow

2. Standardize features
-> stability improves

3. GD still converges slowly
-> inspect eigenvalues / condition number
- check geometry of OLS problem through the Hessian 2/n * XTX
- eigenvalues of XTX tells us how curved the loss func is in diff directions
- condition number = max eigenvalue of XTX / min eigenvalue of XTX
- large condition number -> loss func is a long narrow valley -> extremely slow convergence. loss func being a long narrow valley is also shows severe multicollinearity in cols of X 

4. Explain remaining issue:
-> multicollinearity / ill-conditioning
- ill-conditioning (small change in data can cause a large change in solution) -> coefficient instability + slow GD convergence