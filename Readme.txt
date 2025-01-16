* Create virtual environment:
	conda create -n <env_name> python=3.x.x
* Install jupyter notebook:
	pip install notebook
* Install below dependencies: [reference: https://academy.finxter.com/how-to-create-an-interactive-web-application-using-a-jupyter-notebook/]
	pip install widgetsnbextension 
	pip install ipywidgets 
	pip install voila
* Run these in notebook cell: [reference: https://academy.finxter.com/how-to-create-an-interactive-web-application-using-a-jupyter-notebook/]
	!jupyter nbextension enable --py widgetsnbextension --sys-prefix
		* Running this might show an error "Exception: Jupyter command 'jupyter-contrib' not found."
		* Solution:
			* open anaconda terminal as administrator and run below commands: [reference: https://stackoverflow.com/questions/49647705/jupyter-nbextensions-does-not-appear]
				* conda install -c conda-forge jupyter_contrib_nbextensions
				* jupyter contrib nbextension install --user
	!jupyter serverextension enable voila --sys-prefix
* This should start the application without any error.
* Install additional libraries as needed.
	* pandas
	* markdown