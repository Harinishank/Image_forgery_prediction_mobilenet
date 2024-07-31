# Image Forgery Detection using MobileNet Algorithm

## Overview

This project focuses on detecting forged images using a pre-trained MobileNet model. Image forgery, which involves altering an image to mislead viewers, has become a significant concern with the proliferation of digital media. This project aims to provide an efficient and effective solution to identify such manipulations.

## Features

- **Pre-trained MobileNet Model:** Utilizes the MobileNet architecture, which is known for its efficiency and performance on mobile and embedded devices.
- **Forgery Detection:** Capable of detecting various types of forgeries, including splicing, copy-move, and inpainting.
- **Easy Integration:** Designed to be easily integrated into applications and workflows for real-time or batch processing.

## Prerequisites

To run the project, you need to have the following installed:

- Python 3.x
- TensorFlow or TensorFlow Lite
- OpenCV
- NumPy

You can install these dependencies using:

```bash
pip install tensorflow opencv-python numpy
```

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Harinishank/image-forgery-detection.git
   cd image-forgery-detection
   ```

2. **Download the Pre-trained Model:**

   Download the pre-trained MobileNet model or use the provided script to fetch it. Ensure the model is placed in the `models` directory.

3. **Run the Detection Script:**

   Use the following command to run the forgery detection script on an input image:

   ```bash
   python detect_forgery.py --input path/to/your/image.jpg
   ```

   The script will output whether the image is forged and highlight the manipulated areas if detected.

## Usage

The main script, `detect_forgery.py`, accepts the following arguments:

- `--input`: Path to the input image.
- `--model`: (Optional) Path to the pre-trained MobileNet model.
- `--output`: (Optional) Path to save the output image with highlighted forgeries.

Example:

```bash
python detect_forgery.py --input image.jpg --output output.jpg
```

## Project Structure

- `models/`: Contains the pre-trained MobileNet model.
- `scripts/`: Includes scripts for training and testing the model.
- `data/`: Directory for storing datasets used for training and testing.
- `detect_forgery.py`: Main script for detecting image forgeries.
- `README.md`: Project documentation.

## Training the Model

To train the model from scratch or fine-tune it, follow the instructions in `scripts/train_model.py`. Ensure you have the necessary dataset, and modify the script according to your dataset's structure.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [MobileNet](https://arxiv.org/abs/1704.04861) for providing a lightweight deep learning model suitable for mobile devices.
- The open-source community for the tools and libraries that make this project possible.

## Contact

For any questions or suggestions, please open an issue or contact [harini.200577@gmail.com]
