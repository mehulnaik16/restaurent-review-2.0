# Streamlit Text Classification App

This Streamlit app is a text classification tool that uses Natural Language Processing (NLP) techniques and a Naive Bayes classifier to categorize text data.

## Features

- Text preprocessing including tokenization, stemming, and stop word removal.
- Vectorization using CountVectorizer.
- Model training and prediction using Multinomial Naive Bayes.
- User-friendly interface to input text and see classification results.

## Installation

To run this app, you need to have Python installed. You can install the required packages using `pip` and the provided `requirements.txt` file:

<h1>Streamlit Text Classification App</h1>

<p>This Streamlit app is a text classification tool that uses Natural Language Processing (NLP) techniques and a Naive Bayes classifier to categorize text data.</p>

<h2>Features</h2>
<ul>
  <li>Text preprocessing including tokenization, stemming, and stop word removal.</li>
  <li>Vectorization using CountVectorizer.</li>
  <li>Model training and prediction using Multinomial Naive Bayes.</li>
  <li>User-friendly interface to input text and see classification results.</li>
</ul>

<h2>Installation</h2>
<p>To run this app, you need to have Python installed. You can install the required packages using <code>pip</code> and the provided <code>requirements.txt</code> file:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>Usage</h2>
<ol>
  <li>Clone this repository:</li>
</ol>
<pre><code>git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
</code></pre>

<ol start="2">
  <li>Install the required packages:</li>
</ol>
<pre><code>pip install -r requirements.txt</code></pre>

<ol start="3">
  <li>Download the necessary NLTK data:</li>
</ol>
<pre><code>import nltk
nltk.download('stopwords')
</code></pre>

<ol start="4">
  <li>Run the Streamlit app:</li>
</ol>
<pre><code>streamlit run app.py</code></pre>

<h2>Files</h2>
<ul>
  <li><code>app.py</code>: The main file containing the Streamlit app code.</li>
  <li><code>requirements.txt</code>: A file listing all the dependencies.</li>
  <li><code>README.md</code>: This file.</li>
</ul>
