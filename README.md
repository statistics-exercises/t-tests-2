# Sampling the t-distribution

Thus far we have formulated the hypothesis tests we have done thus far by assuming that the test statistic:

![](https://render.githubusercontent.com/render/math?math=T=\frac{1}{\sigma\sqrt{n}}\sum_{i=1}^n(X_i-\mu))

is a sample from a standard normal random variable.  Furthermore, the grounds for making this assumption is the central limit theorem. 

There is a slight wrinkle in what we are doing, however:  we often have to __estimate__ the standard deviation we use in the above expression by computing the sample variance (i.e. we have to replace ![](https://render.githubusercontent.com/render/math?math=\sigma) with ![](https://render.githubusercontent.com/render/math?math=S_n)).  In the next couple of tasks, we thus want to investigate whether the fact that we are estimating the standard deviation has an effect on the distribution of T.

__With that in mind lets first write a function to generate random variables from the distribution that is sampled by the random variable T when the exact standard deviation is replaced by an estimate of this quantity.__  To complete the exercise you are going to have to complete the function called `gen_t_variable`, which takes one argument in input `n`.  To generate the random variable we want you are going to generate `n` standard normal random variables, ![](https://render.githubusercontent.com/render/math?math=X_i), and you are going to compute a sample mean and an unbiased estimate of the sample variance using:

![](https://render.githubusercontent.com/render/math?math=\overline{X}_n=\frac{1}{n}\sum_{i=1}^nX_i\qquad\textrm{and}\qquad\S_n^2=\frac{n}{n-1}\left(\frac{1}{n}\sum_{i=1}^nX_i^2-\overline{X}_n^2\right))

The final random variable (which should be returned from your function) is then computed as:

![](https://render.githubusercontent.com/render/math?math=T=\frac{\overline{X}_n}{S_n/sqrt{n}})

I have written this as T, as the random variable we generate in this, is from the same distribution as was sampled by T in the previous exercise.  
