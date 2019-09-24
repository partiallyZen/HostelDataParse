{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('Hostel.csv', index_col=0)\n",
    "#tokyo = df.loc[(df['City'] == 'Osaka') & (df['price'] < 1500)]\n",
    "kyoto = df.loc[(df['City'] == 'Kyoto') & (df['price'] < 1500)]\n",
    "city_list = list(df['City'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Osaka', 'Fukuoka-City', 'Tokyo', 'Hiroshima', 'Kyoto']\n"
     ]
    }
   ],
   "source": [
    "cl2 = []\n",
    "for row in city_list:\n",
    "    if row not in cl2:\n",
    "        cl2.append(row)\n",
    "\n",
    "print(cl2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                          name   City  price                Distance  score  \\\n",
      "63          Downtown Inn Kyoto  Kyoto   1000  1.4km from city centre    9.3   \n",
      "141           Hostel Ginkakuji  Kyoto   1300  2.7km from city centre    4.9   \n",
      "152               Hostel Mundo  Kyoto   1400  2.1km from city centre    8.4   \n",
      "153      Hostel Mundo Chiquito  Kyoto   1400  1.4km from city centre    9.5   \n",
      "264         Peace House Sakura  Kyoto   1300  1.8km from city centre    6.3   \n",
      "287  Santiago Guesthouse Kyoto  Kyoto   1300    2km from city centre    8.8   \n",
      "\n",
      "       rating  atmosphere  cleanliness  facilities  location  security  staff  \\\n",
      "63     Superb         8.9          9.7         9.7       9.1       9.1    8.6   \n",
      "141    Rating         2.0         10.0         6.0       6.0       2.0    2.0   \n",
      "152  Fabulous         8.0          8.6         8.0       8.0       8.7    8.9   \n",
      "153    Superb         9.0          9.8         9.3       9.0       9.8   10.0   \n",
      "264      Good         6.8          5.8         5.3       6.5       6.3    6.8   \n",
      "287  Fabulous         8.4          9.3         8.7       8.5       8.7    9.2   \n",
      "\n",
      "     valueformoney         lon        lat  \n",
      "63             9.7  135.755182  35.005277  \n",
      "141            6.0  135.791229  35.027017  \n",
      "152            8.8  135.747946  35.020426  \n",
      "153            9.8  135.753339  35.015514  \n",
      "264            7.0  135.773323  34.995831  \n",
      "287            8.8  135.775802  34.994416  \n"
     ]
    }
   ],
   "source": [
    "print(kyoto)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
