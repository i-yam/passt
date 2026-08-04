# Open Questions Pool — Overfit & Chill

Fifty open questions, published in advance, in the same spirit as the multiple-choice pool.

The exam is 20 multiple-choice questions drawn from the online MC pool plus 15 open questions drawn from the 50 below. Each open question is written to take a student no more than ten minutes. Answers are a few sentences, not essays. The grading note under each question (marked `>`) is for the instructor and lists what a full answer should contain.

Roughly four questions per class. Class 12 is kept short on purpose.

---

## Class 1: What Is Intelligence? What Is Knowledge?

**1.** Turing did not try to answer "Can machines think?" He replaced it with a different question. State the question he substituted and explain in one or two sentences why he thought the substitute was easier to work with.

> The imitation game: can a machine hold a text conversation well enough that a judge cannot reliably tell it from a person. The original question depends on undefined words like "think," so Turing swapped it for one you can actually run and score.

**2.** A friend says their horoscope app is scientific because it has been right about their mood many times. Use Popper to explain what is wrong with that defense, and say what would have to be true for the app to count as falsifiable.

> Being confirmed by hits is not the test. A claim is scientific only if some observation could in principle prove it wrong. The app would need to make a prediction specific enough that a clear outcome could contradict it.

**3.** A retailer has two years of purchase records with no labels and wants to find natural groups of customers. Name the learning category this task falls under and explain what separates it from supervised learning.

> Unsupervised learning. There are no target labels, so the model looks for structure in the data itself, rather than learning a mapping from inputs to known correct outputs.

**4.** Give one capability you would accept as evidence of strong (general) AI but not of narrow AI, and explain the distinction your example is meant to draw.

> Any answer that names a broad, transferable ability (reasoning across unrelated domains, learning a new kind of task without retraining) rather than one narrow benchmark win. The point is generality across domains versus competence at a single task.

---

## Class 2: Learning has many faces

**5.** Sort each of these into deduction or induction, and justify each in one sentence.
(a) "Every customer who churned last quarter had gone sixty days without a purchase, so this customer at sixty days will churn too."
(b) "Policy: any account inactive ninety days is closed. This account is at ninety-two days, so it will be closed."

> (a) is induction, generalizing from observed cases to a rule that is only probable. (b) is deduction, applying a stated rule to a case where the conclusion is certain if the rule holds.

**6.** Anscombe built four datasets with the same mean, variance, correlation, and fitted line that look nothing alike when plotted. What working habit is this meant to teach, and what mistake does it warn against?

> Plot the data before trusting any summary statistic. It warns against reading identical numbers as identical data. Statistical similarity is not the same as similarity.

**7.** Explain the trade-off between a parametric and a non-parametric model. Give one situation where you would accept the assumptions of a parametric model and one where you would not.

> Parametric fixes a functional form with a set number of parameters, which is simpler and more interpretable but can miss the real shape. Non-parametric lets the data define the shape, more flexible but hungrier for data. Accept the assumptions when you have a clear reason to expect that shape; refuse them when the pattern is unknown or clearly not that form.

**8.** Hand-coded rule systems were largely displaced by statistical learning. Give two reasons rule-based expert systems hit a wall as the problems grew.

> Every rule has to be written and maintained by hand, which is expensive. Exceptions multiply and the rules become brittle. Statistical learning reads patterns from data instead of enumerating them.

---

## Class 3: Linear Regression

**9.** Ordinary least squares gives the exact best-fit line in one step. Give one reason a practitioner might reach for gradient descent instead of the closed-form solution.

> The closed form gets expensive or impractical at scale (very many features or rows), and gradient descent generalizes to models that have no closed form. Either reason earns the mark.

**10.** Explain what the loss measures in linear regression and what a residual is. Say how the two are related.

> The loss measures how far the model's predictions sit from the actual values, commonly the mean of the squared residuals. A residual is one such gap, observed minus predicted. The loss is built by summing or averaging the residuals.

**11.** Batch gradient descent is precise and can get stuck. Stochastic gradient descent is noisy and often works better. Explain how the noise can be an advantage.

> The per-sample updates are cheap and jittery. That jitter can knock the search out of a shallow local minimum or flat spot where the clean version would settle, so a sloppier path can reach a better place.

**12.** The learning rate is set very high and the loss keeps growing instead of shrinking. Explain what is going wrong, in terms of the loss surface.

> The steps are too large, so instead of stepping down toward the minimum the weights overshoot it and land higher up the surface each time. The loss diverges rather than converging.

---

## Class 4: Local Models & Geometry

**13.** Explain the difference between a global and a local model in one or two sentences, and name one model of each type from this course.

> A global model fits one rule to all the data (linear regression). A local model lets different regions behave differently (K-NN). Global commits to a single equation; local decides based on where you are.

**14.** A K-NN classifier is run with K equal to 1, then with K equal to 50, on the same data. Describe how the decision boundary changes and what happens to bias and variance.

> At K equal to 1 the boundary is jagged and follows every point, low bias and high variance. At K equal to 50 it smooths out, higher bias and lower variance. Larger K averages over more neighbours.

**15.** Two analysts use the same K-NN model on the same point but pick different distance metrics, and they get different predictions. Explain how that is possible.

> The metric decides which points count as "near," so it changes which neighbours get to vote. Euclidean, Manhattan, and cosine can select different neighbour sets for the same point, and different voters give a different answer.

**16.** Explain in plain terms why K-NN gets worse as you add more features. Name the phenomenon.

> The curse of dimensionality. As features pile up the points spread out and distances flatten toward each other, so "nearest" stops picking out anything meaningfully close.

**17.** In high-dimensional space, most of a cube's volume sits in its corners and two random vectors are almost perpendicular. Why should someone building a distance-based model care about these facts?

> Because the model leans on distance and nearness meaning something, and in high dimensions they stop behaving the way intuition from two or three dimensions expects. Points concentrate at similar distances and directions decorrelate, so the model's basic assumption weakens.

---

## Class 5: Regularization

**18.** A model scores near-perfect on the training data and poorly on new data. Name what is happening and explain how regularization is meant to help.

> Overfitting: the model has memorized the training set, including its noise. Regularization adds a penalty for complexity or large weights, trading a little training fit for a model that holds up better on unseen data.

**19.** Ridge and Lasso both shrink coefficients. Describe the difference in what they do to those coefficients, and say which one performs feature selection.

> Ridge (L2) shrinks all coefficients toward zero but keeps them, spreading weight across correlated features. Lasso (L1) can push individual coefficients exactly to zero, dropping features. Lasso is the one that selects features.

**20.** The regularization strength is turned up steadily from low to high. Describe what happens to bias and to variance as it climbs.

> Bias rises and variance falls. More regularization means a simpler, more constrained model, which fits the training data less closely but swings around less when the data changes.

**21.** A marketing dataset has two hundred candidate features and you suspect only a handful actually matter. Which penalty would you reach for, and why?

> Lasso (L1), because it can zero out the coefficients of the features that do not help, leaving a smaller model built from the ones that do. That is feature selection in disguise.

---

## Class 6: Classification Fundamentals

**22.** Logistic regression outputs a number between 0 and 1. Explain what that number is and how the model turns it into a class decision.

> It is a probability, produced by squashing the linear score through the sigmoid. A threshold (often 0.5) then converts the probability into a class: above the line one class, below it the other.

**23.** A churn model reports ninety-five percent accuracy on a dataset where ninety-five percent of customers do not churn. Explain why that accuracy figure is close to worthless here, and name a metric that would tell you more.

> A model that always predicts "will not churn" also scores ninety-five percent while catching zero churners. Accuracy hides that on imbalanced classes. Precision, recall, or F1 would reveal how it does on the churners you actually care about.

**24.** Define precision and recall in your own words. Give one business situation where you would optimize for precision and one where you would optimize for recall.

> Precision: of the cases the model flagged, how many were right. Recall: of the cases that were actually positive, how many it caught. Optimize precision when acting on a flag is costly (an expensive outbound campaign). Optimize recall when a miss is costly (fraud, disease).

**25.** A test is ninety-nine percent accurate and a customer tests positive for a trait held by only one in a thousand people. Explain roughly why the real chance the customer has the trait is far below ninety-nine percent, and name what dominates the result.

> The trait is rare, so among all positives the false positives from the large healthy majority outnumber the few true cases. The base rate (the prior) dominates, not the test's accuracy.

**26.** Explain what moving the decision threshold up or down does to precision and recall, and why you cannot push both to the maximum at once.

> Raising the threshold flags fewer, more confident cases, so precision rises and recall falls. Lowering it catches more, so recall rises and precision falls. They trade against each other, which is why one threshold cannot maximize both.

---

## Class 7: Decision Trees

**27.** A decision tree plays twenty questions greedily. Explain what "greedy" means here and why the first question matters most.

> Greedy means it picks the single best split available right now, without looking ahead to how later splits will play out. The first split divides the whole dataset, so a good or bad choice there shapes everything below it.

**28.** Entropy and Gini both measure impurity at a node. Say when impurity is highest and when it is zero, and explain what information gain rewards.

> Impurity is highest when the classes are evenly mixed and zero when a node holds a single class. Information gain rewards the split that drops impurity the most, moving from mixed nodes toward pure ones.

**29.** On the Titanic data, "sex" turns out to be a better first split than "age." Explain what makes one feature a better split than another, in terms of impurity.

> The better feature is the one whose split leaves the resulting groups purer, that is, cuts impurity more. Splitting on sex separates survivors from non-survivors more cleanly than age does, so it gives more information gain.

**30.** A credit-scoring tree splits on postal code, and the bank never fed it the applicant's ethnicity. Explain how the model could still end up discriminating.

> Postal code can correlate with ethnicity and act as a stand-in for it. The tree learns the proxy and reproduces the protected pattern, so leaving the sensitive feature out does not remove the bias if a correlated feature carries it.

---

## Class 8: Ensembles

**31.** One deep tree overfits, but a forest of trees generalizes. Explain why averaging many diverse, slightly-wrong trees beats a single tree.

> If the trees are diverse, their errors point in different directions and tend to cancel when averaged, which lowers variance. A single tree has nothing to cancel its mistakes against.

**32.** Explain the core difference between bagging and boosting in how the base learners are trained.

> Bagging trains its learners independently and in parallel, each on a resampled version of the data, then averages them. Boosting trains them in sequence, each new learner focusing on the errors the previous ones made.

**33.** Gradient boosting fits each new tree to the leftovers of the trees before it. Explain what "leftovers" means here and what the learning rate controls.

> The leftovers are the residuals, the part of the target the current ensemble still gets wrong. Each new tree is fit to those. The learning rate controls how large a step each tree contributes, trading speed for the risk of overshooting into overfitting.

**34.** For a random forest to help, its trees have to be diverse. Name the two sources of randomness that make the trees differ from one another.

> Each tree trains on its own bootstrap sample of the rows, and at each split it may only choose from a random subset of the features. Together these make the trees disagree.

---

## Class 9: Validation & Model Selection

**35.** Why do we evaluate a model on held-out data instead of the data it trained on? Say what each score actually tells you.

> The training score tells you how well the model memorized the data it already saw. The held-out score estimates how it will do on data it has not seen, which is the thing you actually want to know. Scoring on the training set flatters the model.

**36.** Explain the tension in deciding how much data to put in the test set versus the training set.

> It is one fixed budget split two ways. More training data builds a better model; more test data gives a more reliable estimate of how good it is. Every row you move to one side you take from the other.

**37.** Explain the difference between a parameter and a hyperparameter, and give one example of each from this course.

> Parameters are learned from the data during training, like the weights of a regression line. Hyperparameters are set before training, like K in K-NN or the regularization strength. You tune the second to help the model learn the first.

**38.** Describe how K-fold cross-validation works and why it gives a more reliable estimate than a single train/test split.

> The data is cut into K parts. Each part serves as the test set once while the other K minus one parts train, and the scores are averaged. Every point gets tested once, so the estimate does not depend on one lucky or unlucky split.

**39.** The median wage in a country rose while it fell within every education group. Name the effect and explain in plain terms how both statements can be true at the same time.

> Simpson's paradox. The mix of groups shifted. If more people moved into higher-earning education groups, the overall median can climb even as each group's own median slips. Aggregation hides the change in group sizes.

---

## Class 10: Recommendations & Neural Networks

**40.** Explain the difference between collaborative filtering and content-based filtering. Name one thing each approach needs that the other does not.

> Collaborative filtering recommends based on the behaviour of users with similar taste, so it needs other users' history. Content-based filtering matches item features to what you have liked before, so it needs described item attributes but not other users.

**41.** A streaming service adds a brand-new film with no viewing history. Name the problem this creates for recommendations and explain why ranking by popularity makes it worse.

> The cold-start problem: with no history there is nothing to base a recommendation on. Popularity ranking sends viewers to items that are already popular, which makes them more popular still, so new items stay invisible in a rich-get-richer loop.

**42.** Conway's Game of Life runs on four simple rules and never mentions a glider, yet gliders walk across the screen. What idea about neural networks is this used to illustrate?

> Emergence. Simple local rules can produce rich global behaviour that nobody programmed in directly. A neural network can likewise do things no one wrote down explicitly, out of many simple parts.

**43.** Describe what a single neuron does to its inputs. Name the three operations it applies before producing an output.

> It weights each input, adds a bias, and squashes the total through a non-linear function into an output (for example a confidence between zero and one). Weight, add bias, activate.

**44.** Stacking more layers gives a network abilities a single neuron does not have. Explain in plain terms what depth buys you.

> Depth lets the network build features in stages. Early layers catch simple patterns, later layers combine them into more complex ones. A single neuron can only draw one straight boundary; layered depth composes many into something richer.

---

## Class 11: LLMs & Generative AI

**45.** Mechanically, what is a language model trained to do? Explain how that one task ends up producing fluent sentences.

> It is trained to predict the next token given the text so far. Doing that well, over and over, one token at a time, chains into fluent text, because each guess is conditioned on everything already written.

**46.** A trigram model writes grammatical text that drifts into nonsense over a paragraph. Explain why a model that only looks at the last couple of words loses the thread.

> It has no memory beyond the last word or two, so it cannot track the topic, a subject introduced three sentences ago, or where the argument was going. Each local guess can be fine while the whole drifts, because nothing holds the long-range context.

**47.** A diffusion model and a next-word model are described as doing the same job in opposite directions. Say what each one starts with and what it produces.

> The next-word model starts with words and adds one word at a time until it has text. The diffusion model starts with a screen of noise and removes noise pass by pass until an image is left. Both turn a guess about "what should come next" into finished output, one building up, one clearing away.

**48.** A student types "make this better" and gets back a worse essay. Explain why that happens, and name one failure that no wording of the prompt will fix.

> The model does exactly what the vague instruction implies, adding length and polish without knowing what "better" means to that student, so it rounds off the good parts too. No prompt fixes a failure that lives in the model itself, such as inventing facts it states with confidence, or not knowing something specific to you it was never told.

---

## Class 12: AI in Practice

**49.** A hiring model is trained on ten years of past hiring decisions. Explain how it could turn out biased even though nobody wrote a biased rule.

> Historical data encodes historical decisions. If past hiring favoured some groups, the model learns that pattern as the target to reproduce, and can carry it forward or sharpen it, without anyone ever writing the bias down.

**50.** To read an AI system as a citizen rather than as a user, name at least two questions you should ask about it, and say briefly why each one matters.

> Any two of: what does it optimize for, whose interests does that serve, what data was it trained on, who can be harmed by it. The optimization target and its incentives usually explain the system's behaviour better than how pleasant it is to use.
