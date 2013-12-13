#coding: utf-8

import csv
import os
import re
import nltk


if __name__ == '__main__':

    s = '''
    start: <pre> 123 </pre> test
    <pre><code>Error in model.frame.default(formula = expert_data_frame$t_labels ~ .,  :
      invalid type (list) for variable 'expert_data_frame$t_labels'
    </code></pre>

    <p>Here is the code how I import the matlab file and construct the dataframe:</p>

    <pre><code>all_exp_traintest &lt;- readMat(all_exp_filepath);
    len = length(all_exp_traintest$exp.traintest)/2;
        for (i in 1:len) {
          expert_train_df &lt;- data.frame(all_exp_traintest$exp.traintest[i]);
          labels = data.frame(all_exp_traintest$exp.traintest[i+302]);
          names(labels)[1] &lt;- ""t_labels"";
          expert_train_df$t_labels &lt;- labels;
          expert_data_frame &lt;- data.frame(expert_train_df);
          rf_model = randomForest(expert_data_frame$t_labels ~., data=expert_data_frame, importance=TRUE, do.trace=100);
        }
    </code></pre>
    '''
    
    body = re.sub(re.compile('<pre>(.*?)</pre>',re.MULTILINE|re.DOTALL), '',s)
    print body
    #work tokenize
    print '-'*10 + 'clean html'
    body = nltk.clean_html(body)
    body = body.lower()
    print body
    print '-'*20 + 'regex tokenize'
    pattern = r"([a-z])\w+"
    body = nltk.regexp_tokenize(body, pattern)
    print body
    

    
