"""
Create sample/reference blog posts to help users understand the blog structure.
Run this after init_data.py to populate with example blogs.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.blogs.models import Blog, Category, Tag
from apps.users.models import User
from django.utils import timezone
from datetime import timedelta

# Sample blog posts data
SAMPLE_BLOGS = [
    {
        'title': 'Getting Started with Python: A Beginner\'s Guide',
        'description': 'Learn the fundamentals of Python programming with this comprehensive guide. Perfect for beginners who want to start their coding journey.',
        'content': '''# Getting Started with Python: A Beginner's Guide

Welcome to the world of Python programming! This guide will help you take your first steps into coding.

## Why Python?

Python is one of the most popular programming languages in the world, and for good reason:

- **Easy to Learn**: Python's syntax is clear and readable
- **Versatile**: Use it for web development, data science, AI, automation, and more
- **Large Community**: Tons of resources and libraries available
- **High Demand**: Python developers are in high demand in the job market

## Installing Python

1. Go to [python.org](https://python.org)
2. Download the latest version for your operating system
3. Run the installer (make sure to check "Add Python to PATH")
4. Verify installation by opening terminal and typing: `python --version`

## Your First Python Program

Let's write the classic "Hello, World!" program:

```python
print("Hello, World!")
```

That's it! Save this in a file called `hello.py` and run it:

```bash
python hello.py
```

## Basic Concepts

### Variables
```python
name = "John"
age = 25
height = 5.9
is_student = True
```

### Data Types
- **Strings**: Text data (`"Hello"`)
- **Integers**: Whole numbers (`42`)
- **Floats**: Decimal numbers (`3.14`)
- **Booleans**: True/False values

### Control Flow
```python
# If statements
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Loops
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

### Functions
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

## Next Steps

1. **Practice Daily**: Coding is a skill that improves with practice
2. **Build Projects**: Start with simple projects like a calculator or todo list
3. **Join Communities**: Participate in forums like Stack Overflow and Reddit
4. **Learn Libraries**: Explore popular libraries like NumPy, Pandas, Django, Flask

## Conclusion

Python is an excellent language for beginners and professionals alike. Start small, practice regularly, and don't be afraid to make mistakes. Happy coding!

---

*Tags: Python, Programming, Tutorial, Beginner*
*Category: Technology*
''',
        'category': 'Technology',
        'tags': ['Python', 'Tutorial', 'Beginner', 'Programming'],
        'is_featured': True,
        'status': 'published',
    },
    {
        'title': 'Building a Successful Startup: Lessons Learned',
        'description': 'Key insights and practical advice from building a startup from scratch. Learn what works and what doesn\'t in the entrepreneurial journey.',
        'content': '''# Building a Successful Startup: Lessons Learned

Starting a business is an exciting but challenging journey. Here are the key lessons I've learned from my entrepreneurial experience.

## 1. Start with a Real Problem

Don't build a solution looking for a problem. Instead:
- Identify a genuine pain point in the market
- Talk to potential customers early and often
- Validate your idea before investing heavily

## 2. Build an MVP First

**Minimum Viable Product (MVP)** is crucial:

- Launch quickly with core features
- Get feedback from real users
- Iterate based on data, not assumptions
- Don't wait for perfection

## 3. Focus on Customer Acquisition

The best product means nothing without customers:

### Effective Strategies:
1. **Content Marketing**: Share valuable content consistently
2. **Social Media**: Engage authentically with your audience
3. **SEO**: Optimize for search engines from day one
4. **Networking**: Build relationships in your industry
5. **Partnerships**: Collaborate with complementary businesses

## 4. Manage Your Finances Wisely

Cash flow is king in startups:

- Keep burn rate low
- Track every expense
- Set aside emergency funds
- Don't raise money too early
- Bootstrap as long as possible

## 5. Build the Right Team

Your team makes or breaks your startup:

### Key Qualities to Look For:
- **Adaptability**: Startup environment changes rapidly
- **Passion**: Believe in the mission
- **Skills**: Complement your weaknesses
- **Culture Fit**: Align with company values

## 6. Embrace Failure and Pivot

Not everything will work:

- Test hypotheses quickly
- Be willing to pivot when data shows you should
- Learn from failures
- Iterate constantly

## 7. Take Care of Yourself

Burnout is real:

- Set boundaries
- Exercise regularly
- Get enough sleep
- Maintain relationships outside work
- Remember why you started

## Common Mistakes to Avoid

1. ❌ Building in isolation without customer feedback
2. ❌ Hiring too many people too quickly
3. ❌ Focusing on features instead of benefits
4. ❌ Ignoring competition
5. ❌ Underestimating time and resources needed

## Conclusion

Building a startup is a marathon, not a sprint. Focus on solving real problems, listen to your customers, manage resources wisely, and don't forget to take care of yourself along the way.

Remember: Every successful entrepreneur has failed multiple times. The key is to learn, adapt, and keep moving forward.

---

*Category: Business*
*Tags: Startup, Entrepreneurship, Business Strategy*
''',
        'category': 'Business',
        'tags': ['Startup', 'Business', 'Entrepreneurship', 'Guide'],
        'is_featured': True,
        'status': 'published',
    },
    {
        'title': '10 Morning Habits That Will Transform Your Life',
        'description': 'Discover powerful morning routines practiced by successful people. Small changes in your morning can lead to big improvements in your life.',
        'content': '''# 10 Morning Habits That Will Transform Your Life

How you start your morning sets the tone for the entire day. Here are 10 powerful habits to transform your mornings and your life.

## 1. Wake Up Early (5:00 AM - 6:00 AM)

The early bird really does catch the worm:
- Quiet time for focused work
- Less distractions
- Sense of accomplishment before the day starts

**Tip**: Go to bed earlier to make this sustainable.

## 2. Hydrate Immediately

Your body is dehydrated after 8 hours of sleep:
- Drink 16-32 oz of water first thing
- Add lemon for extra benefits
- Kickstarts your metabolism

## 3. Make Your Bed

This simple act creates momentum:
- Gives you an immediate win
- Creates order in your environment
- Sets a productive tone

As Admiral McRaven says: "If you want to change the world, start by making your bed."

## 4. Morning Meditation (10-20 minutes)

Benefits of daily meditation:
- Reduces stress and anxiety
- Improves focus and clarity
- Enhances emotional well-being
- Boosts creativity

**Apps to try**: Headspace, Calm, Insight Timer

## 5. Exercise or Move Your Body

Physical activity in the morning:
- Releases endorphins
- Increases energy levels
- Improves mental clarity
- Boosts metabolism

Options:
- 30-minute workout
- Yoga session
- Morning walk/jog
- Quick HIIT routine

## 6. Eat a Healthy Breakfast

Fuel your body properly:

### Great Breakfast Options:
- Oatmeal with fruits and nuts
- Greek yogurt with granola
- Eggs with vegetables
- Smoothie bowl
- Avocado toast

Avoid: Sugary cereals, processed foods

## 7. Practice Gratitude

Start with thankfulness:
- Write 3 things you're grateful for
- Reflects on positive aspects of life
- Shifts mindset to abundance
- Reduces stress

## 8. Review Your Goals

Keep your vision clear:
- Read your long-term goals
- Visualize success
- Plan your top 3 priorities for the day
- Align daily actions with bigger picture

## 9. Limit Phone Use

Don't start with distractions:
- Avoid checking phone for first hour
- No social media scrolling
- No email checking
- Focus on intentional activities

## 10. Read or Learn Something New

Feed your mind:
- Read 10-20 pages of a book
- Listen to a podcast
- Watch an educational video
- Learn a new skill

**Recommendation**: Read personal development, business, or professional books.

## Creating Your Routine

You don't have to do all 10 immediately:

### Week 1-2:
- Wake up early
- Drink water
- Make your bed

### Week 3-4:
- Add meditation
- Add exercise

### Week 5+:
- Incorporate remaining habits
- Adjust based on what works

## Sample Morning Routine Timeline

**5:00 AM** - Wake up, drink water  
**5:10 AM** - Meditation  
**5:30 AM** - Exercise  
**6:30 AM** - Shower  
**7:00 AM** - Healthy breakfast  
**7:30 AM** - Gratitude journal & goal review  
**8:00 AM** - Start work/day  

## Conclusion

Consistency is key. It takes 21 days to form a habit and 90 days to make it a lifestyle. Start small, be patient with yourself, and watch how these morning habits transform your life.

Remember: You don't have to be great to start, but you have to start to be great!

---

*Category: Lifestyle*
*Tags: Habits, Productivity, Self-Improvement, Morning Routine*
''',
        'category': 'Lifestyle',
        'tags': ['Lifestyle', 'Health', 'Productivity', 'Tips'],
        'is_featured': False,
        'status': 'published',
    },
    {
        'title': 'Introduction to Machine Learning: Key Concepts',
        'description': 'Understand the fundamentals of machine learning, from basic concepts to practical applications. A must-read for aspiring AI enthusiasts.',
        'content': '''# Introduction to Machine Learning: Key Concepts

Machine Learning (ML) is transforming every industry. This guide will help you understand the fundamentals.

## What is Machine Learning?

Machine Learning is a subset of Artificial Intelligence where computers learn from data without being explicitly programmed.

### Types of Machine Learning:

1. **Supervised Learning**
   - Learning from labeled data
   - Examples: Classification, Regression
   - Use cases: Spam detection, Price prediction

2. **Unsupervised Learning**
   - Finding patterns in unlabeled data
   - Examples: Clustering, Dimensionality Reduction
   - Use cases: Customer segmentation, Anomaly detection

3. **Reinforcement Learning**
   - Learning through trial and error
   - Agent learns to make decisions
   - Use cases: Game playing, Robotics

## Key Concepts

### 1. Features and Labels
- **Features**: Input variables (X)
- **Labels**: Output variable (y)
- **Example**: Predicting house prices
  - Features: Size, location, bedrooms
  - Label: Price

### 2. Training and Testing
```python
# Split data
train_data = data[:80%]  # 80% for training
test_data = data[80%:]   # 20% for testing

# Train model
model.fit(train_data)

# Evaluate
accuracy = model.score(test_data)
```

### 3. Common Algorithms

#### Linear Regression
- Predicts continuous values
- Simple and interpretable
- Use: Price prediction, Sales forecasting

#### Logistic Regression
- Binary classification
- Outputs probability
- Use: Email spam, Disease diagnosis

#### Decision Trees
- Easy to interpret
- Handles non-linear data
- Use: Credit approval, Customer churn

#### Random Forest
- Ensemble of decision trees
- More accurate than single tree
- Use: Fraud detection, Recommendation systems

#### Neural Networks
- Inspired by human brain
- Powerful for complex patterns
- Use: Image recognition, NLP

### 4. Model Evaluation

**Metrics for Classification:**
- Accuracy: Overall correctness
- Precision: Correct positive predictions
- Recall: Finding all positives
- F1 Score: Balance of precision and recall

**Metrics for Regression:**
- MAE: Mean Absolute Error
- RMSE: Root Mean Squared Error
- R²: How well model explains variance

## Practical Example: Iris Classification

```python
# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")
```

## Common Pitfalls

### 1. Overfitting
- Model learns training data too well
- Poor performance on new data
- **Solution**: Use cross-validation, regularization

### 2. Underfitting
- Model too simple
- Poor performance on all data
- **Solution**: Use more complex model, add features

### 3. Data Quality Issues
- Garbage in, garbage out
- Missing values, outliers, errors
- **Solution**: Clean and preprocess data

## Getting Started with ML

### Step 1: Learn Python
- NumPy, Pandas for data manipulation
- Matplotlib, Seaborn for visualization
- Scikit-learn for ML algorithms

### Step 2: Understand Statistics
- Probability
- Distributions
- Hypothesis testing

### Step 3: Practice with Datasets
- Kaggle competitions
- UCI ML Repository
- Real-world projects

### Step 4: Build Projects
- Start simple (Iris classification)
- Gradually increase complexity
- Share on GitHub

## Resources

**Online Courses:**
- Andrew Ng's ML Course (Coursera)
- Fast.ai Practical Deep Learning
- Google's ML Crash Course

**Books:**
- "Hands-On Machine Learning" by Aurélien Géron
- "Pattern Recognition and ML" by Christopher Bishop
- "Deep Learning" by Goodfellow, Bengio, Courville

**Tools:**
- Jupyter Notebooks
- Google Colab
- TensorFlow/PyTorch

## Conclusion

Machine Learning is a powerful tool, but it's not magic. Success requires:
- Understanding fundamentals
- Quality data
- Appropriate algorithms
- Continuous learning

Start with simple projects, master the basics, and gradually tackle more complex problems. The journey of a thousand miles begins with a single step!

---

*Category: Technology*
*Tags: Machine Learning, AI, Data Science, Tutorial*
''',
        'category': 'Technology',
        'tags': ['AI', 'Machine Learning', 'Python', 'Tutorial'],
        'is_featured': False,
        'status': 'published',
    },
    {
        'title': 'Healthy Meal Prep: A Week\'s Worth of Delicious Recipes',
        'description': 'Save time and eat healthy with these easy meal prep recipes. Complete with shopping list and preparation tips for busy professionals.',
        'content': '''# Healthy Meal Prep: A Week's Worth of Delicious Recipes

Meal prepping saves time, money, and helps you eat healthier. Here's your complete guide!

## Benefits of Meal Prep

✅ Saves 5-10 hours per week  
✅ Reduces food waste  
✅ Saves $100+ monthly on food  
✅ Helps maintain healthy eating  
✅ Reduces decision fatigue  

## Essential Equipment

- **Containers**: Glass or BPA-free plastic (4-6 cup capacity)
- **Measuring cups**: For portion control
- **Sharp knives**: Make prep work easier
- **Cutting board**: Large, stable surface
- **Sheet pans**: For batch cooking
- **Slow cooker**: Optional but helpful

## Weekly Meal Plan

### Monday: Grilled Chicken Bowl
**Prep Time**: 30 minutes

**Ingredients**:
- 6 chicken breasts
- 2 cups brown rice
- 3 cups broccoli
- Olive oil, garlic, herbs

**Instructions**:
1. Marinate chicken in olive oil, garlic, herbs
2. Grill chicken for 6-7 minutes per side
3. Cook rice according to package
4. Steam broccoli for 5 minutes
5. Divide into 6 containers

**Nutrition** (per serving):
- Calories: 450
- Protein: 40g
- Carbs: 45g
- Fat: 12g

### Tuesday: Quinoa Buddha Bowl
**Prep Time**: 25 minutes

**Ingredients**:
- 2 cups quinoa
- 2 cans chickpeas
- 4 cups mixed vegetables (bell peppers, cucumber, tomatoes)
- Tahini dressing

**Instructions**:
1. Cook quinoa
2. Roast chickpeas at 400°F for 25 min
3. Chop vegetables
4. Assemble bowls, dressing on side

### Wednesday: Turkey Chili
**Prep Time**: 45 minutes

**Ingredients**:
- 2 lbs ground turkey
- 2 cans black beans
- 2 cans diced tomatoes
- 1 onion, bell peppers
- Chili spices

**Instructions**:
1. Brown turkey in large pot
2. Add vegetables, cook 5 minutes
3. Add beans, tomatoes, spices
4. Simmer 30 minutes
5. Portion into containers

**Serve with**: Brown rice or whole wheat bread

### Thursday: Salmon and Sweet Potato
**Prep Time**: 35 minutes

**Ingredients**:
- 6 salmon fillets
- 4 large sweet potatoes
- 3 cups green beans
- Lemon, herbs

**Instructions**:
1. Cube sweet potatoes, toss in olive oil
2. Roast at 425°F for 25 minutes
3. Season salmon with lemon, herbs
4. Bake salmon at 400°F for 12-15 minutes
5. Steam green beans

### Friday: Beef Stir-Fry
**Prep Time**: 30 minutes

**Ingredients**:
- 2 lbs lean beef strips
- Mixed stir-fry vegetables
- 2 cups brown rice
- Soy sauce, ginger, garlic

**Instructions**:
1. Cook rice
2. Marinate beef in soy sauce, ginger, garlic
3. Stir-fry vegetables
4. Cook beef quickly over high heat
5. Combine and portion

## Weekend Meals

**Saturday**: Egg muffins with turkey sausage  
**Sunday**: Greek chicken with roasted vegetables

## Shopping List

### Proteins:
- [ ] 6 chicken breasts
- [ ] 2 lbs ground turkey
- [ ] 6 salmon fillets
- [ ] 2 lbs beef strips
- [ ] Dozen eggs

### Grains:
- [ ] Brown rice (3 cups)
- [ ] Quinoa (2 cups)

### Vegetables:
- [ ] Broccoli (3 cups)
- [ ] Sweet potatoes (4 large)
- [ ] Green beans (3 cups)
- [ ] Bell peppers (6)
- [ ] Onions (3)
- [ ] Mixed salad greens

### Pantry:
- [ ] Olive oil
- [ ] Spices and herbs
- [ ] Canned beans
- [ ] Canned tomatoes
- [ ] Soy sauce

## Meal Prep Tips

### 1. Schedule It
- Pick a day (usually Sunday)
- Block 2-3 hours
- Make it a routine

### 2. Prep in Batches
- Cook all proteins together
- Prep all vegetables at once
- Use multiple pans/burners

### 3. Storage Guidelines
- **Cooked meals**: 3-4 days in fridge
- **Raw prepped ingredients**: 2-3 days
- **Freeze extra**: Up to 3 months

### 4. Food Safety
- Cool food before storing
- Label containers with dates
- Reheat to 165°F

### 5. Keep It Interesting
- Rotate recipes weekly
- Try new seasonings
- Mix and match components

## Time-Saving Hacks

1. **Pre-cut vegetables**: Buy frozen or pre-cut (costs more but saves time)
2. **Instant Pot**: Cook rice and proteins simultaneously
3. **Sheet pan meals**: Everything cooks on one pan
4. **Batch cooking**: Double recipes, freeze half
5. **Simple seasonings**: Salt, pepper, garlic powder work for most meals

## Common Mistakes to Avoid

❌ Making too much variety (stick to 3-4 recipes)  
❌ Not labeling containers  
❌ Skipping snack prep  
❌ Using containers that leak  
❌ Forgetting to thaw frozen meals  

## Sample Daily Schedule

**Sunday 2:00 PM** - Shopping  
**Sunday 3:00 PM** - Start prep  
**Sunday 3:15 PM** - Chop all vegetables  
**Sunday 3:45 PM** - Start cooking proteins  
**Sunday 4:30 PM** - Cook grains  
**Sunday 5:00 PM** - Assemble meals  
**Sunday 5:30 PM** - Clean up  

## Conclusion

Meal prepping might seem overwhelming at first, but it becomes easier with practice. Start with just 2-3 recipes and gradually increase as you get comfortable.

Remember: Consistency beats perfection. Even prepping a few meals is better than none!

---

*Category: Food*
*Tags: Meal Prep, Healthy Eating, Recipes, Nutrition*
''',
        'category': 'Food',
        'tags': ['Food', 'Health', 'Guide', 'Lifestyle'],
        'is_featured': False,
        'status': 'published',
    },
]

def create_sample_blogs():
    """Create sample blog posts with proper relationships."""
    
    print("Creating sample blog posts...\n")
    
    # Get or create admin user
    admin_user = User.objects.filter(is_superuser=True).first()
    if not admin_user:
        admin_user = User.objects.filter(is_staff=True).first()
    if not admin_user:
        admin_user = User.objects.first()
    
    if not admin_user:
        print("❌ Error: No users found in database!")
        print("   Please create a user first using: python manage.py createsuperuser")
        return
    
    print(f"✓ Using author: {admin_user.username}\n")
    
    created_count = 0
    
    for blog_data in SAMPLE_BLOGS:
        # Check if blog already exists
        if Blog.objects.filter(title=blog_data['title']).exists():
            print(f"⊘ Skipped: '{blog_data['title']}' (already exists)")
            continue
        
        # Get category
        try:
            category = Category.objects.get(name=blog_data['category'])
        except Category.DoesNotExist:
            print(f"❌ Category '{blog_data['category']}' not found!")
            continue
        
        # Create blog
        blog = Blog.objects.create(
            title=blog_data['title'],
            description=blog_data['description'],
            content=blog_data['content'],
            author=admin_user,
            category=category,
            status=blog_data['status'],
            is_featured=blog_data['is_featured'],
            published_at=timezone.now() if blog_data['status'] == 'published' else None,
            views_count=0
        )
        
        # Add tags
        for tag_name in blog_data['tags']:
            try:
                tag = Tag.objects.get(name=tag_name)
                blog.tags.add(tag)
            except Tag.DoesNotExist:
                print(f"   ⚠ Tag '{tag_name}' not found, skipping")
        
        print(f"✓ Created: '{blog.title}'")
        print(f"   Category: {category.name}")
        print(f"   Tags: {', '.join([t.name for t in blog.tags.all()])}")
        print(f"   Status: {blog.status}")
        print(f"   Featured: {'Yes' if blog.is_featured else 'No'}")
        print()
        
        created_count += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Sample blog creation complete!")
    print(f"   Created: {created_count} new blogs")
    print(f"   Total blogs: {Blog.objects.count()}")
    print(f"   Published: {Blog.objects.filter(status='published').count()}")
    print(f"   Featured: {Blog.objects.filter(is_featured=True).count()}")
    print(f"{'='*60}\n")
    
    # Show blog list
    print("📝 All Blogs in Database:\n")
    for blog in Blog.objects.all().order_by('-created_at'):
        status_icon = "✓" if blog.status == 'published' else "📝"
        feature_icon = "⭐" if blog.is_featured else "  "
        print(f"{status_icon} {feature_icon} {blog.title}")
        print(f"   By: {blog.author.username} | Category: {blog.category.name if blog.category else 'None'}")
        print(f"   Tags: {', '.join([t.name for t in blog.tags.all()[:3]])}")
        print()

if __name__ == '__main__':
    print("\n" + "="*60)
    print("  CREATING SAMPLE/REFERENCE BLOG POSTS")
    print("="*60 + "\n")
    
    # Check if categories and tags exist
    if Category.objects.count() == 0:
        print("❌ No categories found!")
        print("   Please run: python init_data.py first\n")
        exit(1)
    
    if Tag.objects.count() == 0:
        print("❌ No tags found!")
        print("   Please run: python init_data.py first\n")
        exit(1)
    
    create_sample_blogs()
    
    print("\n💡 Tip: View these blogs at http://localhost:3000/")
    print("   Use them as references when creating your own blogs!\n")
