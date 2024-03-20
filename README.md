## Friend or Foe - Multi-Modal Military Target Identification


![Friend or Foe Banner](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/103202628/9612e483-3abf-4eee-b812-5fd434df96c2)

## Overview 🌟
The "Friend or Foe" project, developed by a team from the University of Washington for the course EE P 567: Machine Learning for Cybersecurity, introduces a groundbreaking approach to military target identification using a combination of advanced machine learning models. By leveraging the YOLOv8 algorithm and the Segment Anything Model (SAM), our project offers a robust solution for differentiating between friendly and enemy forces in real-time, aiming to mitigate the risks of friendly fire and enhance operational decision-making on the battlefield.

## Context 🔍
Modern battlefields present an intricate challenge in target identification due to the utilization of camouflage, guerrilla tactics, and the physical and psychological strains on soldiers. Our solution addresses these challenges by integrating cutting-edge image recognition and segmentation technologies, providing soldiers with an AI-assisted tool that significantly improves accuracy in identifying and classifying military personnel based on their visual signatures. This technology aims to reduce casualties caused by misidentification and augment the effectiveness of military engagements.

## Project Scope 📐
**Inclusion:** Our model focuses on identifying military personnel from the United States and Russian armed forces, differentiating them as 'friendly' or 'foe' for project purposes. This distinction is crucial for training the AI to recognize different uniforms and equipment visually.
**Exclusion:** The project explicitly does not cover the recognition of civilians in military attire, the distinction between non-combatants and combatants, or identification of individuals in non-standard or obsolete military uniforms.
**Challenges:** Developing a comprehensive and balanced dataset was a significant challenge, overcome by assembling images from publicly available sources, categorized by military branch. Sophisticated data augmentation techniques and a robust machine learning model were essential in addressing issues such as camouflage and occlusions.

## Technical Approach 🛠
Utilizing the YOLOv8 and SAM models, our project applies advanced machine learning techniques for real-time object detection and segmentation. The models were trained on a custom dataset of military personnel, focusing on optimizing performance despite the challenges of camouflage and image occlusions. Our methodology included fine-tuning the models to achieve high accuracy in classification tasks, incorporating data augmentation for robustness, and testing under various conditions to ensure reliability and effectiveness in real-world scenarios.


## Experimental Results and Analysis 📊
Our experimentation demonstrated the potential of our AI-driven system to accurately distinguish between friendly and enemy forces, achieving a mean Average Precision (mAP) of 75.7%. These results underline the system's capability to enhance situational awareness and decision-making in military operations. The project also explored the integration of a challenge-response system (CRS) for added security, showcasing the system's adaptability to different operational needs.

## Proof of Concept
For showcasing the real-time application usage of the YOLOv8s trained model
![webcam_video_demo_FFMMMTI](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/29029748/90dd5774-6125-4f7c-b484-d7e788ebdb56)

[Refer to the README.md in the webcam_demo folder](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/blob/main/webcam_demo/README.md)

For showcasing the image/video analysis (detection and segmentation) usage of the YOLOv8x trained model
![StreamlitDeploymentDemo](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/assets/29029748/06a1e06f-f4b6-46db-b3de-17728a3bd228)

[Refer to the README.md in the app folder](https://github.com/Naif-Ganadily/Friend-or-Foe-Multi-Modal-Military-Target-Identification/blob/main/app/README.md)

## Installation and Usage 🔌
- Clone the git
- Follow the app and webcam_demo README files
- Comply with the Disclaimer and Limitation of Liability as outlined, in accordance with the terms specified in the LICENSE.md.

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
