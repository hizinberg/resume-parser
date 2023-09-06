import joblib
import numpy as np
import os




def find(data):
    skills = joblib.load(os.path.abspath (os.path.join( __file__,"..//..//modelsai//skills.mod")))
    model = joblib.load(os.path.abspath (os.path.join( __file__,"..//..//modelsai//clfmodel.mod")))
    transform = joblib.load(os.path.abspath (os.path.join( __file__,"..//..//modelsai//wordvector.mod")))


    print(data.items())
    sample = np.array([str(data['skills'])])



    tra = transform.transform(sample)


    ans = model.predict(tra)


    print(skills[int(ans)])



    return [skills[int(ans)],data['skills']]