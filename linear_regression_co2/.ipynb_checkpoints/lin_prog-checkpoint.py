{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python3\n",
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"\n",
    "Created on Wed Mar 18 01:36:31 2020\n",
    "\n",
    "@author: De Dol\n",
    "\"\"\"\n",
    "# this is a program to build a machine learning module \n",
    "#with a linear progression to predict the co2 emmition of\n",
    " #   certain verhicles..\n",
    "\n",
    "# importing the needed libraries\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import pylab as pl\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#reading the data\n",
    "df = pd.read_csv(\"fuel_consumption.csv\",encoding= 'unicode_escape')\n",
    " \n",
    " #looking at the data\n",
    "df.head()\n",
    "plt.show()"
   ]
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
