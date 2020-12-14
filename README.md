# Spot-Language Model

This project was created to build an NLP solution for programming language detection out of source code.

![banner](banner.png)

## Link to Medium Article
[How I Built a Classification Model for Source Code Languages](https://towardsdatascience.com/classification-model-for-source-code-programming-languages-40d1ab7243c2)

## Supported Languages
The trained model supports the following languages:

<table border="1" class="dataframe">
  <tbody>
    <tr>
      <td>C</td>
      <td>C++</td>
      <td>Objective-C</td>
      <td>C#</td>
      <td>Swift</td>
    </tr>
    <tr>
      <td>Ruby</td>
      <td>Julia</td>
      <td>Lua</td>
      <td>Java</td>
      <td>Groovy</td>
    </tr>
    <tr>
      <td>Kotlin</td>
      <td>Scala</td>
      <td>Shell</td>
      <td>Batchfile</td>
      <td>PowerShell</td>
    </tr>
    <tr>
      <td>Python</td>
      <td>Markdown</td>
      <td>HTML</td>
      <td>PHP</td>
      <td>CSS</td>
    </tr>
    <tr>
      <td>TypeScript</td>
      <td>JavaScript</td>
      <td>CoffeeScript</td>
      <td>Haskell</td>
      <td>Perl</td>
    </tr>
    <tr>
      <td>Go</td>
      <td>SQL</td>
      <td>Rust</td>
      <td>TeX</td>
      <td>Erlang</td>
    </tr>
    <tr>
      <td>Visual Basic</td>
      <td>Dart</td>
      <td>Pascal</td>
      <td>Jupyter Notebook</td>
      <td></td>
    </tr>
  </tbody>
</table>

## Demonstration
To try the model out, you can follow this [link](https://spot-language.herokuapp.com/) to the Demo App deployed on **Heroku**.
## Training:
To train the model, you need to download the dataset we used through this [kaggle notebook](https://www.kaggle.com/amalhasni/creating-labeled-code-snippets-dataset). You can read it, to see how we extracted it from **"Github Repos"** dataset or run the all cells to skip to the download link at the end directly.

Once you have the dataset, replace the `DATA_PATH` variable with the appropriate value in the `train.py` and run the code to see the accuracy it gives you. It should be around 97%.

You can use libraries such as `joblib` or `pickle` to serialize it, if you need to use it at a later time.
