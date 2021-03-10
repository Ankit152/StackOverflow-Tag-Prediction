# Stack Overflow Tag Prediction 🏷️


`A machine learning model that predicts tags for a given question and body.`

<p align="center">
  <img src="https://github.com/Ankit152/StackOverflow-Tag-Prediction/blob/main/img/so-logo.jpg" >
</p>


**Dataset Link:** https://www.kaggle.com/imoore/60k-stack-overflow-questions-with-quality-rate

## For developers, by developers 👨‍💻

Stack Overflow is an open community for anyone that codes. They help you get answers to your toughest coding questions, share knowledge with your coworkers in private, and find your next dream job.

## For businesses, by developers 🕴️

Their mission is to help developers write the script of the future. This means helping you find and hire skilled developers for your business and providing them the tools they need to share knowledge and work effectively.

### Problem Defination 🤔

Given a `Title` and the `Body` of a question, we have to predict the relevant tags such that the question gets recommended to the `right domain expert` so that the expert can `answer the question correctly`.

### Business Constraints ✔️

* To predict as many tags as possible with very high `precision` and `recall`.
* `Incorrect tags` could impact the `customer experience` on Stack Overflow.
* No strict latency constraints. The model should be able to generate the relevant tags in a `reasonable` amount of `time`.

### Data 🗄️

* `train.csv` = 48 MB
* `test.csv` = 16 MB

The data consists of 6 columns.

1. Id: Represents the ID of the question
2. Title: Represents the title of the question
3. Body: Represents the body of the question where the question is explained properly
4. Tags: The tags relevant for the question asked
5. CreationDate: The date at which the question was asked
6. Type: Deals with the quality of the question

Our main important features in the dataset are `Title`,`Body` and `Tags`.

## Plots for better understanding 📊

### Countplot of Tags per question 📈

*`This is the countplot of number of tags per question.`*

<p align="center">
  <img src="https://github.com/Ankit152/StackOverflow-Tag-Prediction/blob/main/img/tagCount.jpg" height=612>
</p>

The key take away from the above plot is that most of the question has `2` or `3` tags in them.

### Distribution of Tags 📉

*`This is the distribution of number of times the tag appeared in questions.`*
<p align="center">
  <img src="https://github.com/Ankit152/StackOverflow-Tag-Prediction/blob/main/img/tagDistribution.jpg" height=612>
</p>

The key take away from the above plot is that a tag is appearing 5 time in max.

### WordCloud ☁️

*`This is the wordcloud generated from the tags and it's count.`*
<p align="center">
  <img src="https://github.com/Ankit152/StackOverflow-Tag-Prediction/blob/main/img/wordcloud.jpg">
</p>

The more frequent tags appears to be bigger in the wordcloud and vice versa.
