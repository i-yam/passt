**1.** In his 1950 paper, Alan Turing asked whether:
- a) machines can carry out arithmetic faster and more reliably than any human.
- **b) machines can think.**
- c) machines can build copies of themselves without any human help.
- d) machines can possess genuine subjective conscious experience.

> Turing opens with "Can machines think?" and then replaces it with the imitation game.

**2.** Karl Popper's falsifiability criterion states that a scientific claim:
- a) must be confirmed by a long series of carefully repeated experiments.
- **b) must in principle be refutable by observation.**
- c) must be stated in a precise and fully formal mathematical language.
- d) must be endorsed by a clear majority of recognized domain experts.

> A claim is scientific only if some observation could in principle prove it wrong.

**3.** "Strong AI" in the sense of Class 1 refers to:
- a) a model that has been trained on an unusually large and varied dataset.
- b) any system built out of many billions of tunable internal parameters.
- **c) a system with general cognitive ability comparable to a human.**
- d) a model that surpasses human scores on one narrow benchmark task.

> Strong AI means general intelligence across domains. Model size or one benchmark win is not it.

**4.** A theory that can explain every possible outcome, no matter what happens, is:
- a) the strongest possible kind of scientific theory, since nothing escapes it.
- **b) not falsifiable, and so not scientific in Popper's sense.**
- c) clearly falsifiable, precisely because it manages to cover every case.
- d) acceptable as science only when it is expressed in statistical terms.

> If no observation could ever contradict it, it predicts nothing and cannot be tested.

**5.** In supervised learning, the training data consists of:
- **a) inputs paired with known correct outputs.**
- b) inputs supplied on their own, with no target labels attached.
- c) a stream of rewards and penalties collected from an environment.
- d) a set of hand-written if-then rules supplied by a domain expert.

> Supervised learning learns a mapping from labeled examples.

**6.** Unsupervised learning is characterized by:
- a) a reward signal that tells the model how good each chosen action was.
- b) labeled training examples that are provided to the model in advance.
- **c) finding structure in data with no labels.**
- d) a fixed collection of decision rules written out by a human expert.

> Clustering and dimensionality reduction work on unlabeled data.

**7.** Reinforcement learning differs from supervised learning because the model:
- a) requires absolutely no data of any kind in order to learn its task.
- **b) learns from rewards and penalties received by acting, not from labeled examples.**
- c) is by its nature always non-parametric rather than parametric.
- d) is fundamentally unable to be trained using any form of gradient descent.

> The agent learns a policy through trial and feedback from an environment.

**8.** A pocket calculator is generally not considered AI because it:
- a) operates far too quickly for its behavior to count as intelligent.
- **b) follows fixed rules and learns nothing from data.**
- c) has no way to connect to the internet or any outside resource.
- d) is restricted to working with whole numbers and integer arithmetic.

> A calculator executes a fixed procedure. It does not learn or adapt.

**9.** Deduction proceeds:
- **a) from general rules to specific cases.**
- b) from a set of specific observed cases up to a general rule.
- c) from raw observation toward the fitting of a statistical model.
- d) from an input to an output by way of repeated random sampling.

> Deduction goes rule to case. If the rule holds, the conclusion is certain.

**10.** Induction proceeds:
- a) from a stated general rule down to a particular specific case.
- **b) from specific observations to a general rule.**
- c) from a formal mathematical proof toward its logical conclusion.
- d) from a produced output backward to the input that caused it.

> Induction generalizes from examples. The conclusion is probable, not guaranteed.

**11.** Most statistical machine learning is inductive because the model:
- a) is proven to be correct in advance, before it has seen any data at all.
- **b) infers a general rule from a finite sample, meant to hold on unseen data.**
- c) is guaranteed never to make a single mistake when faced with new data.
- d) does nothing more than memorize the exact contents of the training set.

> It generalizes from a sample, which is exactly why it can be wrong on new data.

**12.** Classic rule-based expert systems hit a wall mainly because:
- a) the computers of the era were simply not fast enough to run them.
- **b) hand-coding and maintaining the rules is expensive and brittle.**
- c) they had no mechanism for storing any knowledge whatsoever.
- d) such systems were prohibited by law across the European Union.

> Every rule must be written and maintained by hand, and exceptions multiply fast.

**13.** Anscombe's Quartet shows that:
- a) four different regression models can fit a single dataset about equally well.
- **b) summary statistics can be identical for datasets of very different shape.**
- c) linear regression has no way of coping with outliers in the data.
- d) a strong correlation between variables does not establish causation.

> Four datasets share mean, variance, correlation and regression line, yet look nothing alike.

**14.** A semantic network or ontology is an example of:
- **a) explicit knowledge representation, where facts and relations are coded by hand.**
- b) a deep neural network built from many stacked, trainable hidden layers.
- c) an unsupervised method that clusters unlabeled data into similar groups.
- d) a reinforcement learning policy learned from rewards in an environment.

> These encode knowledge as nodes and labeled links, defined in advance by humans.

**15.** Statistical learning displaced hand-coded rule systems mainly because it:
- a) manages to work effectively without requiring any training data or labeled examples at all.
- b) is in every single case fully transparent and easy to interpret.
- **c) learns patterns directly from data instead of relying on enumerated rules.**
- d) is structurally incapable of ever overfitting the training data.

> Let the data define the rules, and you stop writing them one by one.

**16.** The practical lesson of Anscombe's Quartet for a working analyst is:
- a) trust the correlation coefficient ahead of any visual plot of the data.
- **b) plot the data before trusting any summary statistic.**
- c) default to a linear model regardless of what the data looks like.
- d) strip out every outlier from the data before doing anything else.

> Statistical similarity is not similarity. Look at the data.

**17.** Ordinary least squares (OLS) for linear regression yields:
- **a) a closed-form analytic solution.**
- b) only an approximate answer obtained through repeated iteration.
- c) a probabilistic output bounded between zero and one.
- d) exactly the same result as K-NN run with K equal to one.

> OLS solves the normal equations directly. No iteration needed.

**18.** Stochastic gradient descent updates the parameters:
- a) using the gradient computed over the entire training set at every step.
- **b) using the gradient from a single sample or a small batch per step.**
- c) without making any use of gradients during the update at all.
- d) only after the loss has already been driven all the way to zero.

> The full dataset per step is batch gradient descent. SGD uses one sample or a mini-batch.

**19.** The loss function in linear regression measures:
- a) the total count of input features included in the model.
- **b) how far the model's predictions sit from the actual values.**
- c) the size of the learning rate used during gradient descent.
- d) the number of training steps taken before the model converged.

> Mean squared error sums the squared gaps between prediction and truth.

**20.** Gradient descent moves the weights:
- a) in the same direction as the gradient, which raises the loss.
- **b) in the direction opposite the gradient, to decrease the loss.**
- c) in random directions until the loss happens to drop a little.
- d) strictly along one fixed axis chosen ahead of time.

> The negative gradient points downhill on the loss surface.

**21.** A residual in a regression model is:
- a) the slope of the straight line that the model has fitted.
- **b) the difference between an observed value and the model's prediction.**
- c) the learning rate multiplied by the current gradient value.
- d) the total number of features the model was given to use.

> Residual equals observed minus predicted. Residual plots reveal where the model fails.

**22.** If the learning rate in gradient descent is set far too high, the algorithm typically:
- a) converges much faster than usual with no downside whatsoever.
- **b) overshoots the minimum and may diverge.**
- c) is mathematically guaranteed to land on the global minimum.
- d) stops paying attention to the data and ignores it entirely.

> Steps too large bounce past the minimum and the loss can blow up.

**23.** One practical reason to prefer stochastic gradient descent over full-batch gradient descent is:
- a) it is guaranteed to reach a strictly lower loss than batch descent.
- **b) the noisy updates are cheap and can help escape poor local minima.**
- c) it removes any need to choose or tune a learning rate at all.
- d) it loads the entire dataset into memory at once for every step.

> Per-sample updates scale to large data, and the noise can jolt the search out of shallow traps.

**24.** Feature scaling (normalization) before gradient descent mainly helps by:
- a) altering which of the input features actually end up mattering to the model's predictions.
- **b) putting features on comparable ranges so the optimizer converges more smoothly.**
- c) doing away with the need to set a learning rate altogether.
- d) ensuring the training error is driven all the way down to zero.

> Unscaled features stretch the loss surface and slow or destabilize descent.

**25.** In the weight-space view of linear regression, fitting a line means:
- a) committing every single training point to memory exactly.
- b) selecting the steepest slope that the data could possibly allow.
- **c) finding the weights that minimize the loss over the data.**
- d) assigning values to the weights completely at random.

> Each weight setting is a point in weight space with a loss. Fitting is finding the low point.

**26.** A parametric model is a model that:
- a) has no parameters at all that can be adjusted during training.
- **b) assumes a fixed functional form with a finite, predetermined number of parameters.**
- c) keeps all of the training data in memory and queries it directly at prediction time.
- d) cannot be regularized by any penalty placed on its coefficients.

> A line has two parameters regardless of dataset size. Storing all data is non-parametric.

**27.** K-nearest-neighbours with K equal to 1 generally produces:
- a) high bias paired with comparatively low variance.
- **b) low bias and high variance.**
- c) both high bias and high variance at the same time.
- d) both low bias and low variance at the same time.

> K=1 follows every point exactly. Small data changes swing the boundary.

**28.** In very high-dimensional space, a hypersphere inscribed in a hypercube of equal edge length:
- a) gradually approaches the full volume of the surrounding cube.
- **b) goes to zero as a fraction of the cube's volume.**
- c) holds at a fixed ratio that does not depend on the dimension.
- d) grows without bound and diverges toward infinity.

> Almost all the volume ends up in the corners. The inscribed sphere vanishes.

**29.** K-nearest-neighbours is a non-parametric method because it:
- a) has exactly one tunable parameter that it learns from the data.
- **b) keeps the training data and uses it directly at prediction time.**
- c) starts from the assumption that the underlying data is linear.
- d) is trained by running gradient descent over its parameters.

> KNN does no training step. It defers all work to query time.

**30.** Increasing K in K-nearest-neighbours generally:
- a) lowers the bias while raising the variance of the predictions.
- **b) raises bias and lowers variance, smoothing the decision boundary.**
- c) has no real effect on the shape of the decision boundary.
- d) turns the method into a parametric model with fixed form.

> Averaging over more neighbours smooths the boundary and steadies predictions.

**31.** The choice of distance metric in KNN matters because it:
- a) changes how many distinct output classes the problem has.
- **b) determines which points count as "near," and so which neighbours vote.**
- c) becomes irrelevant the moment the value of K has been fixed.
- d) affects only how long the training takes, rather than the actual predictions it makes.

> Euclidean, Manhattan and cosine distance can pick different neighbours for the same point.

**32.** A counterintuitive effect of high dimensionality is that:
- a) all of the data points collapse onto one identical location.
- **b) two random vectors are almost certainly close to orthogonal.**
- c) distances between points become much easier to interpret.
- d) every point ends up sitting exactly at the center of the space.

> In high dimensions random directions are nearly perpendicular, and distances concentrate.

**33.** Global models differ from local models in that:
- **a) a global model fits one rule to all data, while a local model lets regions behave differently.**
- b) global models are, essentially by their own definition, always non-parametric rather than parametric in form.
- c) local models are unable to produce any predictions at all.
- d) global models can operate without needing any training data.

> Linear regression is global. KNN is local.

**34.** KNN tends to degrade as the number of features grows because:
- a) it immediately exhausts all of the available system memory.
- **b) points become sparse and distances lose their meaning.**
- c) it can no longer find room to store the training data.
- d) the class labels attached to the data simply vanish.

> The curse of dimensionality flattens distances, so "nearest" stops being meaningful.

**35.** Compared with ridge (L2), lasso (L1):
- a) shrinks the coefficients of every feature uniformly and by the same amount.
- **b) can set individual coefficients exactly to zero, implicitly selecting features.**
- c) requires no hyperparameter at all to control the regularization strength.
- d) can only ever be applied to classification rather than regression problems.

> L1 can zero coefficients and drop features. L2 shrinks them but keeps them all.

**36.** Increasing the regularization strength typically causes:
- a) lower bias together with higher variance.
- **b) higher bias and lower variance.**
- c) no effect at all on the bias-variance trade-off.
- d) higher bias and higher variance occurring together.

> More regularization means a simpler model: higher bias, lower variance.

**37.** High bias in a model corresponds to:
- **a) a model too rigid to capture the real pattern (underfitting).**
- b) a model far too sensitive to the particular training data.
- c) a model that achieves an error of zero on the training set.
- d) a model that has been given far too many input features.

> Bias is systematic error from oversimplified assumptions.

**38.** High variance in a model corresponds to:
- a) a model that disregards the structure of the training data almost entirely when it is fitted.
- **b) a model overly sensitive to the particular training sample (overfitting).**
- c) a model built from too few parameters to fit anything.
- d) a model that records no error at all on the test set.

> Variance is how much the fitted model swings when the training data changes.

**39.** Simpson's paradox describes a situation where:
- a) two separate models happen to produce the very same prediction.
- **b) a trend present in every subgroup reverses when the groups are combined.**
- c) the accuracy of a model rises as more features are added to it.
- d) regularization ends up stripping every feature out of the model.

> The UC Berkeley admissions case: each department favored women, the aggregate looked the opposite.

**40.** Adding a polynomial feature such as x² to a linear regression:
- a) makes the model non-linear in its parameters as well as its inputs.
- **b) lets the model fit curves while staying linear in the parameters.**
- c) is something that turns out to be mathematically impossible to do.
- d) always brings about a reduction in the model's test error.

> x² is just another input column. The model stays linear in the weights.

**41.** Ridge regression (L2) handles a group of correlated features by:
- a) dropping all but one of the correlated features outright.
- **b) shrinking them all and spreading weight across them.**
- c) leaving the correlated features completely unchanged.
- d) forcing every one of those coefficients down to zero.

> L2 keeps every feature small rather than choosing among correlated ones.

**42.** Minimizing training error is not the goal of learning because:
- a) the training error of a model is something that cannot be computed.
- **b) a model can drive training error to zero by memorizing noise and still fail on new data.**
- c) the training error and the test error of a model always turn out to be exactly equal in the end.
- d) the test set is in practice never available to the modeler at all.

> Zero training error often signals overfitting, not a good model.

**43.** Regularization works by adding to the loss:
- a) a quantity of additional training data drawn from the same source.
- **b) a penalty that grows with model complexity or the size of the weights.**
- c) a reward for fitting the training set as perfectly as possible.
- d) a constant value chosen completely at random each time.

> The penalty discourages large weights, trading a little fit for stability.

**44.** A headline reports that average household income rose, yet income fell within every age group. The most likely explanation is:
- a) a simple arithmetic mistake somewhere in the calculation.
- **b) a shift in group sizes, a form of Simpson's paradox.**
- c) the effect of applying regularization to the underlying model.
- d) overfitting of the model to its training data.

> Aggregation can hide subgroup trends when the mix of groups changes.

**45.** The fundamental difference between regression and classification is that:
- a) regression relies entirely on gradient descent for fitting, while classification never makes use of it.
- **b) regression predicts a continuous value, classification predicts a discrete category.**
- c) classification simply cannot be carried out using any linear model.
- d) classification, unlike regression, needs no labeled training data.

> Regression predicts a number, classification predicts a class. Both use labels.

**46.** Accuracy as a classification metric can mislead when:
- a) the classes in the dataset are evenly balanced.
- **b) the classes are strongly imbalanced.**
- c) the model has been given too few input features.
- d) the decision boundary turns out to be exactly linear.

> On 95% negatives, "always no" scores 95% accuracy and detects nothing.

**47.** The "naive" assumption in Naive Bayes is that:
- a) every class in the problem is taken to be equally likely.
- **b) features are conditionally independent given the class.**
- c) the data is assumed to be perfectly linearly separable.
- d) there are only ever exactly two classes to choose between.

> The assumption is usually false, yet the classifier often works well anyway.

**48.** Precision is defined as:
- **a) true positives divided by all predicted positives.**
- b) true positives divided by the count of all actual positives.
- c) all correct predictions divided by the total number of predictions.
- d) false positives divided by the number of true negatives.

> Of the items the model flagged, how many were right.

**49.** Recall is defined as:
- a) true positives divided by the count of all predicted positives.
- **b) true positives divided by all actual positives.**
- c) true negatives divided by the total number of actual negatives.
- d) the harmonic mean taken between accuracy and precision.

> Of the items that were actually positive, how many the model caught.

**50.** The F1 score is:
- a) the plain arithmetic mean of accuracy and recall.
- **b) the harmonic mean of precision and recall.**
- c) the simple product of precision and recall multiplied together.
- d) the raw count of true positives produced by the model.

> F1 punishes a large gap between precision and recall.

**51.** A flu test is 99% accurate, but only 1 in 1000 people has the flu. A positive result means the actual chance of having flu is:
- a) roughly 99 percent, matching the stated accuracy of the test.
- **b) low, because false positives swamp the rare true cases.**
- c) exactly 50 percent, an even split between the two possibilities.
- d) effectively certain that the person does have the flu.

> With a tiny prior, most positives are false positives. Base rates dominate.

**52.** Logistic regression produces:
- a) an unbounded continuous prediction with no fixed range.
- **b) a probability between 0 and 1 via the sigmoid.**
- c) a hard class label with no associated probability at all.
- d) a cluster assignment that groups similar points together.

> The sigmoid squashes the linear score into a probability, then a threshold decides the class.

**53.** A marketing team runs an expensive outbound campaign and can only afford to contact the customers a model flags as likely buyers. The metric they should prioritize is:
- **a) precision, so that flagged customers are actually likely to convert.**
- b) recall, so that no potential buyer is ever missed by the model.
- c) raw accuracy measured across the entire customer base.
- d) the total number of input features the model was trained on.

> Each contact costs money. A false positive wastes spend on someone who will not buy, so they want the flagged set to be right.

**54.** In real-time fraud detection, recall usually matters more than precision because:
- a) raising a false alarm carries no real cost to the bank at all.
- **b) missing a real fraud is more costly than reviewing a false alarm.**
- c) fraudulent transactions form the majority class in the data.
- d) the precision of such a model simply cannot be measured.

> A missed fraud is money gone. A false flag costs a review. The errors are not equal.

**55.** A decision tree makes predictions by:
- a) fitting one single global linear equation across the whole of the data in just one step.
- **b) recursively partitioning the feature space and assigning each region an output.**
- c) averaging together the outputs of the K nearest neighbours.
- d) computing a probability by passing a score through the sigmoid.

> Each split carves the space. Each leaf is a region with a prediction.

**56.** A leaf node in a decision tree represents:
- a) a feature on which the tree will choose to split next.
- **b) a final prediction for all points that reach it.**
- c) the root from which the entire tree originally grows.
- d) the learning rate that governs how the tree is built.

> Once you reach a leaf, the tree has decided.

**57.** Information gain at a split is:
- a) the total number of samples that arrive at the node.
- **b) the reduction in impurity achieved by the split.**
- c) the overall depth of the tree once it is fully grown.
- d) the accuracy of the tree measured on the test set.

> The tree chooses the split that drops impurity the most.

**58.** Entropy at a node is highest when:
- a) every sample at the node belongs to one single class.
- **b) the classes are evenly mixed.**
- c) the node in question happens to be a terminal leaf.
- d) the node contains only a single training sample.

> Maximum uncertainty is a 50/50 mix. A pure node has entropy zero.

**59.** Gini impurity measures:
- a) the overall depth that the decision tree reaches once it has been fully grown out on the data.
- **b) the chance of misclassifying a randomly drawn sample labeled by the node's class distribution.**
- c) the number of input features available for splitting.
- d) the learning rate that controls how the tree grows.

> Like entropy, it is lowest for a pure node and highest for an even mix.

**60.** A node containing samples of only one class has:
- a) the maximum possible entropy for that node.
- **b) zero impurity.**
- c) an information gain value that is left undefined.
- d) the largest Gini value the node could possibly take.

> A pure node needs no further split.

**61.** A common reason decision trees are favored in regulated settings is that:
- a) they reliably reach the very highest predictive accuracy of any available model on the task.
- **b) their decisions can be read and explained, satisfying interpretability requirements.**
- c) they are structurally incapable of ever overfitting the data.
- d) they can be built and used without any training data at all.

> You can trace exactly why the model decided as it did.

**62.** EU rules around credit scoring push toward interpretable models because:
- **a) a person denied credit can demand an explanation of the decision.**
- b) interpretable models are in every case more accurate than the alternatives.
- c) black-box models happen to run faster than interpretable ones.
- d) decision trees can be trained without needing any data at all.

> The right to an explanation favors models whose logic can be stated.

**63.** When a credit-scoring tree splits on postal code, the danger is that:
- a) postal codes carry no predictive value whatsoever for the task.
- **b) the feature can act as a proxy for a protected attribute like ethnicity.**
- c) the tree is converted into a parametric model by the split.
- d) the entropy at that node immediately collapses to zero.

> Dropping a protected attribute does not help if a correlated feature smuggles it back in.

**64.** A decision tree grown to full depth on the training set tends to:
- a) underfit the data and miss the real underlying pattern.
- **b) overfit by memorizing the training data, including its noise.**
- c) settle into a state of unusually high bias.
- d) generalize to new data essentially perfectly.

> An unconstrained tree can fit every point. Depth limits and pruning fight this.

**65.** A random forest combines:
- a) a single deep tree that has been heavily pruned back.
- **b) many trees trained on bootstrap samples with random feature subsets.**
- c) one linear model combined together with a single decision tree.
- d) gradient descent applied on top of a KNN classifier.

> Bootstrap aggregating plus random features makes the trees diverse.

**66.** Averaging many diverse, slightly-wrong models works because it:
- a) raises the overall bias of the combined model.
- **b) reduces variance, since independent errors tend to cancel.**
- c) does away with the need for any training data.
- d) guarantees that the combined error drops to zero.

> Diversity is the point. Correlated trees would not help.

**67.** Bagging (bootstrap aggregating) trains its learners:
- **a) independently, each on a resampled version of the data.**
- b) sequentially, with each learner correcting the previous one.
- c) jointly, with a meta-model stacked on top of them.
- d) on identical data with no resampling applied at all.

> Independent learners, then average or vote.

**68.** Boosting differs from bagging in that it:
- a) trains every single one of its base learners fully in parallel and independently of one another.
- **b) trains learners sequentially, each focusing on the previous ones' errors.**
- c) makes no use of weak learners of any kind.
- d) is unable to use decision trees as its base learners.

> Boosting chases the leftovers: each model targets what the last got wrong.

**69.** Stacking builds an ensemble by:
- a) averaging together a set of essentially identical models all trained in the very same way.
- **b) training a meta-model to combine the predictions of several base models.**
- c) pruning back a single tree until it stops overfitting.
- d) resampling the training data one time before fitting.

> The meta-model learns how to weigh the base learners.

**70.** A bootstrap sample is drawn:
- a) without replacement, producing a sample smaller than the original.
- **b) with replacement, so some points repeat and others are left out.**
- c) only from the held-out test set rather than the training data.
- d) by sorting the data and taking it in a fixed order.

> Sampling with replacement gives each tree a slightly different dataset.

**71.** Compared with a single decision tree, a random forest usually:
- a) tends to overfit the training data even more badly.
- **b) generalizes better thanks to lower variance.**
- c) ends up being considerably easier to interpret.
- d) is trained on a smaller portion of the data.

> You trade the readability of one tree for the stability of many.

**72.** Feature importance from a random forest tells you:
- a) the exact causal effect that each feature has on the target.
- **b) roughly how much each feature contributed to the model's splits.**
- c) the learning rate that was used while fitting the model.
- d) precisely which training samples ended up misclassified.

> It ranks features by contribution. It is association, not proof of causation.

**73.** The purpose of a held-out test set is to:
- a) train the model to a higher level of accuracy.
- **b) estimate performance on data the model has not seen.**
- c) enlarge the pool of data available for training.
- d) tune the learning rate over the course of training.

> Evaluating on the training set tells you how well it memorized, not how well it generalizes.

**74.** In K-fold cross-validation, the data is:
- **a) split into K parts; each part serves as the test set once while the rest train.**
- b) split just a single time into one training set and one separate held-out test set.
- c) used in its entirety for training with nothing held back.
- d) shuffled thoroughly and then discarded before fitting.

> Every point gets to be in the test set exactly once. Scores are averaged.

**75.** Leave-one-out cross-validation on n samples trains:
- a) just one single model over the whole dataset.
- **b) n models, each leaving out a single sample.**
- c) K models, for some chosen K smaller than n.
- d) no models at all during the procedure.

> Clean in theory, costly in practice for large n.

**76.** The difference between a parameter and a hyperparameter is that:
- **a) parameters are learned from data; hyperparameters are set before training.**
- b) hyperparameters are learned from data while parameters are chosen by hand.
- c) the two terms refer to exactly the same thing.
- d) hyperparameters exist only within neural networks.

> Weights are parameters. The regularization strength or K is a hyperparameter.

**77.** Grid search finds hyperparameters by:
- a) guessing a single hyperparameter configuration at random and then stopping there immediately.
- **b) evaluating every combination from a predefined grid and keeping the best.**
- c) training just one model and accepting its settings as final.
- d) running gradient descent directly on the target labels.

> Exhaustive over the grid, which is why it gets expensive fast.

**78.** Stratified cross-validation is used mainly to:
- a) make the overall training and validation procedure run noticeably faster than before.
- **b) preserve the class proportions in each fold for imbalanced data.**
- c) get rid of the test set during the procedure.
- d) increase the learning rate used while training.

> Without stratification, a fold might miss a rare class entirely.

**79.** Tuning many hyperparameters against the same validation set risks:
- a) underfitting the training set badly rather than fitting it the way the search intended.
- **b) overfitting to the validation set, so the estimate becomes optimistic.**
- c) eliminating all of the features from the model.
- d) turning the model into a parametric one.

> Repeated peeking at the validation set quietly leaks information into the choice.

**80.** Evaluating on held-out data assumes that:
- **a) the test data comes from the same distribution as the training data.**
- b) the test set is always larger in size than the training set that was used to fit the model.
- c) the model achieves an error of zero on the training data.
- d) the data being evaluated carries no labels at all.

> If the world shifts, a clean test score can still mislead.

**81.** The core tension in choosing a train/test split is that:
- a) adding still more test data to the evaluation always makes the underlying model itself better too.
- **b) more training data builds a better model, while more test data gives a more reliable estimate.**
- c) the chosen split has no effect on either of the two.
- d) the training set and the test set have to be equal in size.

> You are dividing a fixed budget between learning and measuring.

**82.** The cold-start problem in recommendation systems is:
- a) the recommendation system is slow to respond and load whenever it has only just started up.
- **b) there is too little data on a new user or item to make good recommendations.**
- c) the model has been given far too many features to handle.
- d) the server hosting the system has gone offline entirely.

> No history means nothing to base a recommendation on.

**83.** Collaborative filtering recommends items based on:
- **a) the behavior of users with similar tastes.**
- b) the written text description attached to each item.
- c) a fixed collection of hand-written recommendation rules.
- d) the listed price of the item and nothing else.

> Users who liked what you liked point toward what you might like next.

**84.** Content-based filtering recommends items by:
- a) copying whatever the most popular users happened to do.
- **b) matching item features to a user's past preferences.**
- c) selecting items completely at random for each user.
- d) disregarding the individual user's history altogether.

> It compares item attributes rather than other users' behavior.

**85.** The Galton board (balls bouncing through pegs) illustrates how:
- a) recommendations end up being produced in an essentially random and unpredictable way.
- **b) many small independent chances add up to a bell-shaped distribution.**
- c) gradient descent finds the minimum of a loss surface.
- d) the entropy of a distribution is calculated in practice.

> Repeated binary choices produce the binomial, which approaches the normal curve.

**86.** The "popularity trap" in recommendation systems refers to:
- a) items that were once popular gradually ending up removed from the catalog over time.
- **b) popular items getting recommended more, which makes them more popular still.**
- c) users developing a strong dislike for the most popular items.
- d) a software bug somewhere in the recommendation database.

> A rich-get-richer loop. Early advantage compounds, and new items struggle.

**87.** Conway's Game of Life demonstrates that:
- a) complex behavior demands an equally complex set of rules.
- **b) a few simple local rules can produce rich global patterns.**
- c) cellular automata are incapable of carrying out computation.
- d) randomness is a prerequisite for any structure to emerge.

> Emergence: complexity from simplicity, with no global blueprint.

**88.** At a conceptual level, a neural network computes by:
- a) storing all of the training data and querying it later.
- **b) composing layers of non-linear transformations.**
- c) sorting the input features into a particular order.
- d) applying one single linear equation to the input.

> Stacked layers with non-linearities let it represent complicated functions.

**89.** Depth (more layers) helps a neural network because it:
- a) cuts down the total number of trainable parameters that the network needs in order to work.
- **b) lets the network build features hierarchically, simpler ones combining into complex ones.**
- c) removes the network's dependence on having any training data.
- d) provides a guarantee that the network will never overfit.

> Early layers catch edges, later layers catch shapes, and so on.

**90.** At its mechanical core, a large language model:
- a) looks the answer up in a stored database of facts.
- **b) predicts the next token given the preceding text.**
- c) follows a set of grammar rules written out by hand.
- d) runs the input through a single decision tree.

> Trained to continue text, it generates one token at a time.

**91.** An LLM "hallucination" is:
- a) an image that the model has been asked to generate.
- **b) a confident output that is factually wrong or invented.**
- c) a failure occurring in the underlying hardware.
- d) a particular category of training data fed to it.

> Fluent and plausible does not mean true. The model optimizes for likely text, not verified fact.

**92.** Prompt engineering is best described as:
- a) retraining the underlying weights of the model from scratch.
- **b) shaping the input to steer the model's output toward what you want.**
- c) directly editing the source code that the model runs on.
- d) attaching labels to the data used to train the model.

> It controls the framing and instructions, not the underlying model.

**93.** NIST benchmarks of face recognition systems have found that accuracy:
- a) stays identical across every demographic group that was tested.
- **b) can vary across demographic groups, with higher error rates for some.**
- c) reaches a perfect score whenever the lighting is good.
- d) depends on nothing more than the price of the camera.

> Performance gaps across groups are a documented and consequential finding.

**94.** When a study says a medical AI "outperforms" doctors, the careful reader checks:
- a) only the single headline accuracy figure that happened to be reported in the abstract.
- **b) how the evaluation was set up and whether it reflects real clinical use.**
- c) the total number of parameters contained in the model.
- d) the brand name of the hardware the model was run on.

> Lab performance on a curated dataset is not the same as performance in a clinic.

**95.** A model trained on historically biased data will tend to:
- a) correct that bias on its own without any intervention.
- **b) reproduce and sometimes amplify the bias in its predictions.**
- c) ignore the patterns present in the data altogether.
- d) become more accurate specifically on minority groups.

> The model learns the decisions encoded in the data, fair or not.

**96.** A hard fact about mathematical fairness definitions is that:
- a) there is a single agreed-upon definition that everyone uses.
- **b) several reasonable definitions exist and cannot all hold at once.**
- c) fairness is something that is always straightforward to guarantee.
- d) fairness and accuracy are guaranteed never to come into conflict.

> Equal false positive rates and equal predictive value can be mutually exclusive.

**97.** Reading an AI system as a citizen rather than a user means asking:
- a) only whether the system is polished, enjoyable, and genuinely fun for people to use.
- **b) what it optimizes for, whose interests that serves, and who can be harmed.**
- c) only how fast the system manages to run in practice.
- d) only how much the system ends up costing to operate.

> The optimization target and its incentives often matter more than the interface.

**98.** EU AI regulation is broadly organized around:
- a) an outright, blanket ban placed on essentially every form of machine learning there is.
- **b) a risk-based approach, with stricter rules for higher-risk uses.**
- c) the sheer size of the model and nothing else besides.
- d) the particular programming language used to build it.

> Higher-stakes applications face stronger obligations.

**99.** To "map" an AI system (e.g. a streaming feed), a useful first step is to identify its:
- a) physical location of the data-center servers that the whole system happens to run on.
- **b) likely ML type, training data, optimization target, and potential harms.**
- c) font and the color scheme of its user interface.
- d) date on which the system was first released.

> Naming the optimization target usually reveals why the system behaves as it does.
