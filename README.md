# ecom-analytics-pipeline

## Project Structure

This is a mock readme.

```
ecom-analytics-pipeline/
├── data/
│   ├── raw/
│   ├── processed/
├── notebooks/
│   ├── exploratory/
│   ├── modeling/
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
├── tests/
│   ├── test_data_preprocessing.py
│   ├── test_feature_engineering.py
│   ├── test_model_training.py
├── README.md
├── requirements.txt
```

## Dataset

The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data).

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ecom-analytics-pipeline.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ecom-analytics-pipeline
    ```
3. I recommend using VSCode and then opening the project in a dev container:
    ```sh
    code .
    ```
4. The required dependencies will be installed automatically by uv in the dev container.

## Usage

1. Preprocess the data:
    ```sh
    python src/data_preprocessing.py
    ```
2. Perform feature engineering:
    ```sh
    python src/feature_engineering.py
    ```
3. Train the model:
    ```sh
    python src/model_training.py
    ```

## Testing

Run the tests to ensure everything is working correctly:
```sh
pytest tests/
```

## Contributing

Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.