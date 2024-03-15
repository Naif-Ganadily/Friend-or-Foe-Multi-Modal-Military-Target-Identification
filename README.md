## Friend or Foe - Multi-Modal Military Target Identification


![Friend or Foe Banner](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/103202628/9612e483-3abf-4eee-b812-5fd434df96c2)

## Overview 🌟
The "Friend or Foe" project leverages advanced machine learning techniques to accurately identify military personnel in images, classifying them as either friendly or hostile entities. Utilizing a multi-modal approach, this AI-driven system aims to significantly enhance decision-making accuracy in high-pressure military engagements by minimizing the risks associated with misidentification.

## Context 🔍
In the complex and fast-paced environment of modern warfare, correctly distinguishing between ally and enemy combatants is crucial but challenging due to diverse uniforms and equipment. Our project addresses this challenge by applying cutting-edge image recognition technology to accurately detect and classify military targets based on their visual signatures.

## Project Scope 📐
- **Inclusion**: Focus on identifying personnel from two distinct military forces, labeled as 'friendly' and 'foe' for the purposes of this project.
- **Exclusion**: The system is not designed to recognize civilians in military-like attire, differentiate non-combatants from combatants, or identify personnel wearing obsolete or non-standard military uniforms.

## Challenges 🚧
- Assembling a comprehensive dataset was achieved by pooling publicly available images, categorized into specific military branches and subsequently narrowed down into two primary classes for simplicity.
- Overcoming the camouflaging effect and image occlusions involved sophisticated data augmentation techniques and the adoption of a robust machine learning model capable of high-accuracy classification despite these challenges.


## Technical Highlights 💡
- Dataset Preparation: Utilized Roboflow for dataset augmentation and preprocessing, enhancing the initial set of 1100 images to 2652 through techniques like random rotation, Gaussian blur, and noise addition, ensuring a diverse training set.
- Model Training: Selected YOLOv8 variants for their balance between speed and accuracy, adapting model training to encompass a range of complexities from simple object detection to intricate segmentation tasks, demonstrating a nuanced understanding of model capabilities.

## Proof of Concept
For showcasing the real-time application usage of the YOLOv8s trained model
![webcam_video_demo_FFMMMTI](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/29029748/90dd5774-6125-4f7c-b484-d7e788ebdb56)

[Refer to the README.md in the webcam_demo folder]([https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/blob/main/app/README.md](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/blob/main/webcam_demo/README.md))

For showcasing the image/video analysis (detection and segmentation) usage of the YOLOv8x trained model
![StreamlitDeploymentDemo](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/29029748/06a1e06f-f4b6-46db-b3de-17728a3bd228)

[Refer to the README.md in the app folder](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/blob/main/app/README.md)

## Installation and Usage 🔌
- TODO

## License 📄
- CC BY-NC-SA 4.0 [Link to the LICENSE.md](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/blob/main/LICENSE.md)
- [Link to the documentation of the legal license](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en)

## Acknowledgments 👏
- Mention of Professor Radha Poovendran at the University of Washington, Seattle, WA, for his association with the project.
- A big thank you to our team members – Andrew Jeon, Bassam Halabiya, Naif A. Ganadily, and Zachary Saunders – for their dedication and teamwork, which have been crucial in advancing this project.

## Disclaimer and Limitation of Liability ⚠️

- **No Warranty:** The "Friend or Foe - Multi-Modal Military Target Identification System" and all associated materials are provided "AS IS" and "AS AVAILABLE," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. The creators, developers, and contributors do not warrant that the software will be error-free, that defects will be corrected, or that the service is free of viruses or other harmful components.

- **Use at Your Own Risk:** Any use of this software is at your own risk. You assume full responsibility for any loss that results from your use of the software, including any downloads from it. The creators, developers, and contributors shall not be liable for any direct, indirect, incidental, special, consequential, or exemplary damages, including but not limited to, damages for loss of profits, goodwill, use, data, or other intangible losses, resulting from (i) your access to or use of or inability to access or use the software; (ii) any conduct or content of any third party on the software; or (iii) unauthorized access, use, or alteration of your transmissions or content, whether based on warranty, contract, tort (including negligence), or any other legal theory, whether or not we have been informed of the possibility of such damage.

- **Indemnification:** You agree to defend, indemnify, and hold harmless the project's creators, developers, and contributors from and against any and all claims, damages, obligations, losses, liabilities, costs, debts, and expenses (including but not limited to attorney's fees) arising from your use of, or inability to use, the software.

- **Acknowledgment:** By using this software, you acknowledge that you have read this disclaimer and agree to its terms.
