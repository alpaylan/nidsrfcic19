from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 200 ,
                            random_state = 42 ,
                            oob_score = True ,
                            max_features='log2',
                            min_samples_leaf=10 )