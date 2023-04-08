# ✨ Segment Anything 🚀 - Streamlit WebApp [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
Streamlit based implementation for the The ![Segment Anything Model (SAM)](https://github.com/facebookresearch/segment-anything) developed by ![Meta AI research](https://github.com/facebookresearch).

![Animation](https://user-images.githubusercontent.com/29462447/230744183-b07af944-dc28-4da8-8d37-f6a81ea13800.gif)

## Installation:
* Simply run the command ```pip install -r requirements.txt``` to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Create a ```model``` directory and save the model checkpoints which can be downloaded from [here.](https://github.com/facebookresearch/segment-anything#model-checkpoints)
3. Simply run the command: 
```
streamlit run app.py
```
4. Navigate to http://localhost:8501 in your web-browser.
5. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading images, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

| UI  | Results  |
|-----|----------|
| ![output_final](https://user-images.githubusercontent.com/29462447/230743523-6aaae5cc-9492-40ba-91e5-cb7bf62e322a.png)  | ![output_1](https://user-images.githubusercontent.com/29462447/230743520-fe039b06-1d52-4d8d-b361-8765d103b5d2.png)  |

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker 
```


### Citation
```
@article{kirillov2023segany,
  title={Segment Anything}, 
  author={Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C. and Lo, Wan-Yen and Doll{\'a}r, Piotr and Girshick, Ross},
  journal={arXiv:2304.02643},
  year={2023}
}
```
