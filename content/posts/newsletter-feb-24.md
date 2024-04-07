Title: February 2024 Newsletter
Subtitle: Announcing the first major release of our software product!
Date: 2024-2-12
Modified: 2024-2-12
Category: Company
Tags: company,newsletter
Authors: Ryan Buckley
Summary: We now have a web-based app that people can use to explore our wondrous permit data! 
Image: /images/shane.png


I've been looking forward to writing this newsletter for more than a year.

🥳 Today we invite you to sign up for our first major software release! 🥳

*   Anyone can register at [https://app.shovels.ai](https://app.shovels.ai)! All you need is an email address. Here's [a blog post](https://www.shovels.ai/blog/how-to-use-the-shovels-app/) about it!
*   It's free for now. There still are a few bugs I know about, and you'll find a few more. It's free because I want your feedback. I figure we'll start charging for access before the next newsletter.
*   Our [custom GPT](https://chat.openai.com/g/g-apAxK8WGu-shovels-ai) is getting LOTS of use too. Who knew making building permit and contractor data accessible would be such a useful thing? (We did 😇)[](https://www.shovels.ai/blog/how-to-use-the-shovels-api/)

The case for software
=====================

Shovels is a data company. That's our DNA. We're not very proficient (yet) at building software. We'll develop that skill as we go, but what will always set us apart is our devotion to clean, reliable, and useful data.

We launched our nationwide [building permit API](https://api.shovels.ai/redoc#tag/Permits) in August 2023. We followed that release with a [nationwide contractor API](https://api.shovels.ai/redoc#tag/Contractors) in November 2023. We now have a bunch of paying customers and meaningful revenue. 

Just getting this far is a big deal! And we'll continue to serve our current and new API customers. We ❤️ API deals.

But as you know, the building trades are in transition. Many companies that have a clear, burning need for our data have no means to access it through an API. ChatGPT is great for figuring out what we offer and getting some samples, but it's not great for most commercial uses. 

"This all sounds good, Ryan," they would say. "Reach out again when you have software."

Click.

So, now we have software.

**🥳 Introducing: Shovels app v1.0 🥳**
=======================================

Are you too excited to continue reading? I get it. [Click here](https://app.shovels.ai) to see it for yourself. 

The Shovels app introduces our three data features: **addresses**, **permits**, and **contractors**.

![]({static}/images/permits-filter.png)

In this screenshot, we're looking up all active air source heat pump permits in California that mention the brand Mitsubishi. It's popular! I looked up Fujitsu (what we have) too and didn't see nearly as many. 

The other potential uses are endless:

*   Search for all new permits statewide last month
*   Find all active commercial permits valued at over $1M
*   Look for wave pool permits (yes, somebody asked for this once)
*   Download to a CSV straight from the app
*   Anywhere in the good ol' US of A

Now, wouldn't it be interesting to see which contractors did these Mitsubishi heat pump installs? Click on a permit and you'll get to a permit profile page. On that profile page is (usually) going to be a contractor. Click and that, et voila.

We have contractor profiles!

![]({static}/images/shane.png)

Here we see every permit that Shane Patrick O'Malley (don't know him, hope he's nice!) has worked on. Shane does a ton of work in San Francisco. If you're curious, you can click on each of his permits and learn everything you need to know about each job.

To find more Shanes, hit the Contractors filter where you can look up all the heat pump installers in any ZIP code in the country. 

Or if you just want to look up the permits on an address, you can do that too. Click on Addresses.

![]({static}/images/addresses.png)

On the address profile page we're eventually going to show a bunch of property attributes, all of the permits, and all of the contractors. Contractor profiles are going to show a summary of all of their permits by type, stage, and eventually all of their business branches too. 

Yeesh. There's always so much more to do!

Things to do with permits: even more heat pump contractors
==========================================================

I recently [did a demo of Shovels](https://www.youtube.com/watch?v=kr0G9miWRDY) for the GreenHome Institute, a 501 c3 nonprofit with a mission to empower people to make healthier and more sustainable choices in the renovation and construction of the places we live.

This turned out to be a [really long, interesting conversation](https://www.youtube.com/watch?v=kr0G9miWRDY). We got into the nuts and bolts of how permit data works, and since there were many trades professionals in the audience, we got to go deep on how we classify permits and rate contractors. 

[Scroll ahead to minute 31](https://youtu.be/kr0G9miWRDY?feature=shared&t=1871) to see us dive into how the new Shovels app can help anyone find their perfect heat pump contractor.

The future
==========

As implied, this is the start of a loooong development process. We've only just begun to build the killer building permits application.

Imagine being able to look up a jurisdiction like Palo Alto and see everything in the permitting queue and get estimates on how long the review process will take.

Imagine being able to dive into building inspection results, even see who the inspector is, or see each step in the permit review process and how long it usually takes.

Imagine being able to filter for contractors by the number of heat pumps they've installed and how long it usually took.

Yep, it's all on the roadmap! Read even more detail in [our launch post](https://www.shovels.ai/blog/how-to-use-the-shovels-app/).

P.S. We're Silicon Valley famous: Here's [our mention on TWIST](https://www.youtube.com/watch?v=FfY92Zk0S4Q&t=3448s) with Elizabeth Yin, Zach Coelius, and Jason Calacanis 😎