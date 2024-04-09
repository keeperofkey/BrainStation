# Background

VISION is a relatively new technology company located in the Bay Area of San
Francisco, California, USA. They specialize in computer vision – the same kind
of technology that Tesla uses in their autonomous driving feature.

Computer vision is a branch of artificial intelligence (AI), that essentially
allows computers to "see" and understand images, videos, etc. While video and
photos are all digital these days, your devices don’t really "know" what is
inside those images or videos. For example, when humans look at a photograph of
a landscape, we will be able to determine what composes the photo, such as
blades of grass, trees, flowers, a river, mountains, etc.

Computers need "training" to identify these objects and to derive meaning from
the provided data. Once computers have an understanding of "what they are
looking at" (the data, image or video being presented), analysis can be
performed to make inferences about the data and extrapolate results. An example
of this might be training a system to review images of manufactured products.
If the computer is able to see enough examples of what a "compliant" or
"passable" product is, along with examples of what might be a "defective" or
"rejected" product, then it can help machines sort good from bad parts.

The same can be said about self driving, identifying cars on the road, how fast
they are moving, etc. The computer can then decide what course of action to
take such as how fast to drive, and what to do when presented with a road sign.

## Services

VISION’s goal is to help companies develop computer vision solutions for their
own custom needs and use cases. They offer a variety of computer vision
services and solutions to make this a reality.

## A Data Collection, Ingestion, & Management Interface

If customers need to train for specific use cases, VISION has made
comprehensive software that allows its customers to upload, organize, and
manage image or video data used to train an artificial intelligence model.

There are a number of considerations here including file size and type, number
of files, content of data being uploaded (e.g. intellectual property), storage
location of the data, and more.

## A Data Annotation & Labeling Interface

AI systems don’t inherently "know" what the data being presented is. Humans
need to point out those patterns by leaving annotations or labels, among other
supporting data/metadata.

The provided interface helps make that process easy and scalable by allowing
users to provide examples or leverage the company’s proprietary software to
help speed up the data annotation and labeling process.

Computer Vision Example Source: Mindy Support

## Training Data Library & Model Library

VISION has solutions tailored to different levels of effort and involvement
desired by customers. Their training data library houses a vast amount of
different image and video data that can be used to train a computer vision
model. Rather than having clients search, organize and manage all the training
data, they can obtain a massive amount of value by using collections already
curated by VISION. It’s important to note there are privacy, security,
intellectual property and other considerations to consider for VISION’s library
along with how that data is being used.

If clients don’t want to train their own artificial intelligence model, they
can use a pre-trained one provided by VISION. While this is an added cost, it
is also an added value to clients, simplifying their process to build a
solution. The downside here is that pre-trained models lack the same level of
customization and control given to custom-developed models.

# The Company

The company’s success hinges on 3 core pillars:

Data: AI solutions require a tremendous amount of well-organized, high quality
data. AI companies have been found to frequently scrape large amounts of data
from the web without regard for the source or ownership of the data. This is
currently a fiercely debated legal issue within the tech and AI space. All data
used by VISION is stored in the United States. Currently, all of their clients
are US companies. People: To stay ahead of competitors, VISION relies on
industry-leading talent to help them develop innovative solutions. VISION has
about 200 employees in the Bay Area headquarters. They also rely on a number of
vendors and contractors to provide everything from office snacks and cleaning,
to software and collaboration tools, document shredding, cloud server rentals
(e.g. AWS), accounting, etc. They also have a small 24hr contracted
cybersecurity monitoring team that works out of India. This team helps fill any
gaps in monitoring during off-hours. Tech: VISION has to maintain a highly
efficient tech infrastructure both for their employees and their clients.
Internal IT assets need to function correctly and must remain secure to help
keep the company’s data and apps secure. Infrastructure used for client
solutions must also remain secure, yet accessible to the right individuals both
internally and externally.

## The Client

VISION has just finalized a deal with a large healthcare provider operating
clinics and diagnostic labs which process all varieties of medical diagnostics
including blood tests, x-rays, ultrasounds, MRIs, etc. The client has a full
suite of services for their patients and employs a large number of staff
including technicians, nurses, doctors, admin staff, etc. They have over 60,000
employees globally and have dedicated lab facilities, but also clinics within
partner organizations such as pharmacy and grocery chains.

The client is looking to improve their efficiency with test reporting and
results interpretation, specifically for their imaging tests which includes
MRIs (localized and whole body), CT Scans, x-rays and ultrasounds. In short,
they are looking for an automated way to increase accuracy for detection of
anomalies and are considering piloting full automated interpretations for
select types of tests and conditions.

With regards to accuracy, there will always be a level of both human and
machine error. By leveraging computer vision, the client aims to have machines
run the first review of all important medical imaging, and will require the
support of human reviewers to point out anything in the results that the AI
model may have missed. For select procedures such as measuring the angle of
vertebrae in the spine, machines should be able to calculate this with a high
degree of accuracy to free up human resources for other tasks.

## Client Onboarding

While no formal solution has been developed, you’ve been provided with an
example proposal from the project management team at VISION. As a cybersecurity
team member at VISION and a consultant for this engagement, it’s your
responsibility to provide early security suggestions to guide the development
of the project. Be sure to make and state any assumptions as you provide your
suggestions.

# IT Infrastructure & Data Flow

## Client Device & Imaging Equipment

The first step of this process begins at the client’s facilities and clinics.
The imaging devices are connected to computers to record and store the results.
A technician operating the machine first opens up the patient’s file and
confirms the tests being done.

Once the image is captured and saved to the client’s file, the first step of
the process is complete. All client records are stored by the patient in the
cloud which can be accessed at any machine in the client’s facilities. The
imaging result is also stored in the cloud environment, specific to the client.
This covers the data capture and storage components of the tech infrastructure.

## Data Processing

VISION’s services are running on their own secure cloud infrastructure which is
separate from all clients. In order to get the data to be processed, a secure
connection will need to be established with the client’s systems.

The data will then be processed by VISION’s systems, but considerations need to
be made around any medical and technology regulation. There are also questions
around if the data should be stored or cached in VISION’s systems or if it will
also be used to help train the model. These items have not yet been decided.

## Communication of Results

Once a result has been determined by VISION’s systems, they need to be
privately communicated to the client. In some cases, it will also need to be
communicated (along with the annotated image itself) back to the patient
directly. All data sent directly to the patient goes through an app the client
developed.

This step is especially important as the information needs to be communicated
to the right person (e.g. client staff or patient) to ensure the right message
and interpretation is sent. There are instances where manual review of results
is also needed.

There will also be scenarios where select information needs to be sent to
insurance companies for records or billings, and where results and annotated
images (e.g. x-ray measurements and calculations) will need to be sent to
family doctors, hospitals, or other healthcare providers outside of the
client’s company. This communication will have to occur directly from the
output of VISION’s systems, and must be done securely.

# Questions to Consider

The use of artificial intelligence warrants the consideration of many questions. While this is not an exhaustive list, you may want to consider some or all of the following questions when providing your security recommendations.

- Where are we getting training data for the model?
- How old is the data? Does that matter?
- Is the training data personally identifiable? Is that a problem? Is there a way to de-anonymize the data?
- How do we make adjustments for patients of different ages? (The gap between vertebrae in a young child and adult are different, how can we make sure the model accounts for what is normal given a variety of biological factors such as age)
- How should the data be stored? Think about physical IT assets being used as well as access and other security concepts.
- Which stakeholders inside VISION and the client’s organization should get access to specific data?
- Should this data persist or be cached locally on devices?
- Should this data be easily accessible?
