import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { toast } from 'react-toastify';
import { useBlogStore, useSettingsStore } from '../store';

const BlogEditor = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { createBlog, updateBlog, fetchBlogDetail, selectedBlog, loading } = useBlogStore();
  const { categories, tags, fetchCategories, fetchTags } = useSettingsStore();
  
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    description: '',
    category: '',
    status: 'draft',
    is_featured: false,
  });
  
  const [selectedTags, setSelectedTags] = useState([]);
  const [imageFile, setImageFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [aiSummary, setAiSummary] = useState('');
  const [isGeneratingSummary, setIsGeneratingSummary] = useState(false);

  // Load categories and tags on component mount
  useEffect(() => {
    fetchCategories();
    fetchTags();
  }, [fetchCategories, fetchTags]);

  // Load existing blog if editing
  useEffect(() => {
    if (id) {
      fetchBlogDetail(id);
    }
  }, [id, fetchBlogDetail]);

  useEffect(() => {
    if (selectedBlog && id) {
      setFormData({
        title: selectedBlog.title || '',
        content: selectedBlog.content || '',
        description: selectedBlog.description || '',
        category: selectedBlog.category?.id || '',
        status: selectedBlog.status || 'draft',
        is_featured: selectedBlog.is_featured || false,
      });
      setSelectedTags(selectedBlog.tags?.map(t => t.id) || []);
      setImagePreview(selectedBlog.featured_image);
      setAiSummary(selectedBlog.ai_summary?.summary || '');
    }
  }, [selectedBlog, id]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      // Check file size (max 5MB)
      if (file.size > 5 * 1024 * 1024) {
        toast.error('Image size should be less than 5MB');
        return;
      }

      // Check file type
      if (!file.type.startsWith('image/')) {
        toast.error('Please select an image file');
        return;
      }

      setImageFile(file);

      // Create preview
      const reader = new FileReader();
      reader.onloadend = () => {
        setImagePreview(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleGenerateSummary = async () => {
    if (!formData.content || formData.content.length < 100) {
      toast.error('Please write at least 100 characters to generate a summary');
      return;
    }

    setIsGeneratingSummary(true);
    try {
      // Simulate AI summary generation (replace with actual API call)
      const summary = await generateAISummary(formData.content);
      setAiSummary(summary);
      toast.success('AI Summary generated successfully!');
    } catch (error) {
      toast.error('Failed to generate summary. Please try again.');
      console.error(error);
    } finally {
      setIsGeneratingSummary(false);
    }
  };

  const generateAISummary = async (content) => {
    // Simulate API call - replace with actual OpenAI integration
    return new Promise((resolve) => {
      setTimeout(() => {
        const words = content.split(' ').slice(0, 50).join(' ');
        resolve(`${words}... [AI-generated summary]`);
      }, 2000);
    });
  };

  const handleSubmit = async (e, status = 'draft') => {
    e.preventDefault();

    if (!formData.title.trim()) {
      toast.error('Please enter a title');
      return;
    }

    if (!formData.content.trim()) {
      toast.error('Please enter content');
      return;
    }

    try {
      const blogData = new FormData();
      blogData.append('title', formData.title);
      blogData.append('content', formData.content);
      
      // Truncate description to 300 characters
      const description = (formData.description || aiSummary || '').substring(0, 300);
      if (description) {
        blogData.append('description', description);
      }
      
      blogData.append('status', status);
      blogData.append('is_featured', formData.is_featured);
      
      if (formData.category) {
        blogData.append('category_id', formData.category);
      }
      
      // Send tag IDs as JSON array string (backend will parse it)
      if (selectedTags.length > 0) {
        const tagIdsJson = JSON.stringify(selectedTags);
        console.log('Sending tag_ids:', tagIdsJson);
        console.log('Selected tags array:', selectedTags);
        blogData.append('tag_ids', tagIdsJson);
      }
      
      if (imageFile) {
        blogData.append('featured_image', imageFile);
      }

      // Log FormData contents for debugging
      console.log('FormData contents:');
      for (let [key, value] of blogData.entries()) {
        console.log(`  ${key}:`, value instanceof File ? `File(${value.name})` : value);
      }

      if (id) {
        // Update existing blog
        await updateBlog(id, blogData);
        toast.success('Blog updated successfully!');
      } else {
        // Create new blog
        await createBlog(blogData);
        toast.success('Blog created successfully!');
      }
      
      navigate('/dashboard');
    } catch (error) {
      console.error('Blog creation error:', error);
      console.error('Error response:', error.response?.data);
      
      // Show detailed error message
      const errorMsg = error.response?.data?.detail || 
                       error.response?.data?.error ||
                       Object.entries(error.response?.data || {})
                         .map(([key, value]) => `${key}: ${Array.isArray(value) ? value.join(', ') : value}`)
                         .join('; ') ||
                       error.message ||
                       (id ? 'Failed to update blog' : 'Failed to create blog');
      
      toast.error(errorMsg);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-5xl mx-auto px-4">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900">
            {id ? '✏️ Edit Blog Post' : '✨ Create New Blog Post'}
          </h1>
          <p className="text-gray-600 mt-2">
            Write your content and let AI help you create summaries
          </p>
        </div>

        <form onSubmit={(e) => handleSubmit(e, 'draft')} className="space-y-6">
          {/* Title */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              📝 Blog Title *
            </label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              placeholder="Enter an engaging title for your blog..."
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-lg"
              required
            />
          </div>

          {/* Image Upload */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              🖼️ Featured Image
            </label>
            <div className="mt-2">
              {imagePreview && (
                <div className="mb-4">
                  <img
                    src={imagePreview}
                    alt="Preview"
                    className="max-w-md h-64 object-cover rounded-lg border-2 border-gray-200"
                  />
                  <button
                    type="button"
                    onClick={() => {
                      setImageFile(null);
                      setImagePreview(null);
                    }}
                    className="mt-2 text-red-600 hover:text-red-700 text-sm font-medium"
                  >
                    Remove Image
                  </button>
                </div>
              )}
              <input
                type="file"
                accept="image/*"
                onChange={handleImageChange}
                className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
              />
              <p className="text-xs text-gray-500 mt-1">
                PNG, JPG, GIF up to 5MB
              </p>
            </div>
          </div>

          {/* Category & Tags */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-white rounded-lg shadow-sm p-6">
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                🏷️ Category
              </label>
              <select
                name="category"
                value={formData.category}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="">Select a category</option>
                {categories.map((cat) => (
                  <option key={cat.id} value={cat.id}>
                    {cat.name}
                  </option>
                ))}
              </select>
            </div>

            <div className="bg-white rounded-lg shadow-sm p-6">
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                🔖 Tags
              </label>
              <div className="space-y-2">
                <div className="flex flex-wrap gap-2 mb-2">
                  {tags.map((tag) => (
                    <button
                      key={tag.id}
                      type="button"
                      onClick={() => {
                        // Ensure we're storing the ID as a number
                        const tagId = typeof tag.id === 'number' ? tag.id : parseInt(tag.id, 10);
                        console.log('Toggling tag:', tag.name, 'ID:', tagId);
                        setSelectedTags(prev => {
                          const newTags = prev.includes(tagId)
                            ? prev.filter(t => t !== tagId)
                            : [...prev, tagId];
                          console.log('Updated selected tags:', newTags);
                          return newTags;
                        });
                      }}
                      className={`px-3 py-1 rounded-full text-sm font-medium transition-colors ${
                        selectedTags.includes(tag.id)
                          ? 'bg-blue-500 text-white'
                          : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                      }`}
                    >
                      {tag.name}
                    </button>
                  ))}
                </div>
                <p className="text-xs text-gray-500">
                  Click to select/deselect tags. {selectedTags.length} selected.
                </p>
              </div>
            </div>
          </div>

          {/* Content Editor */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              ✍️ Blog Content *
            </label>
            <textarea
              name="content"
              value={formData.content}
              onChange={handleChange}
              placeholder="Write your blog content here... You can use Markdown formatting."
              rows="20"
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent font-mono text-sm leading-relaxed"
              required
            />
            <div className="mt-2 flex items-center justify-between">
              <p className="text-xs text-gray-500">
                Character count: {formData.content.length} | Words: {formData.content.split(/\s+/).filter(w => w).length}
              </p>
              <p className="text-xs text-blue-600">
                💡 Tip: Use Markdown for formatting (# for headings, ** for bold, etc.)
              </p>
            </div>
          </div>

          {/* AI Summary Section */}
          <div className="bg-gradient-to-r from-purple-50 to-blue-50 rounded-lg shadow-sm p-6 border-2 border-purple-200">
            <div className="flex items-center justify-between mb-4">
              <label className="block text-sm font-semibold text-gray-700">
                🤖 AI-Generated Summary
              </label>
              <button
                type="button"
                onClick={handleGenerateSummary}
                disabled={isGeneratingSummary || !formData.content}
                className={`px-6 py-2 rounded-lg font-semibold transition-all ${
                  isGeneratingSummary || !formData.content
                    ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                    : 'bg-gradient-to-r from-purple-600 to-blue-600 text-white hover:from-purple-700 hover:to-blue-700 shadow-md hover:shadow-lg'
                }`}
              >
                {isGeneratingSummary ? (
                  <>
                    <span className="inline-block animate-spin mr-2">⚙️</span>
                    Generating...
                  </>
                ) : (
                  <>🤖 Generate AI Summary</>
                )}
              </button>
            </div>

            {aiSummary ? (
              <div className="bg-white rounded-lg p-4 border-2 border-purple-300">
                <p className="text-gray-700 leading-relaxed">{aiSummary}</p>
                <p className="text-xs text-gray-500 mt-2">
                  ✨ AI-generated summary - You can edit the description field below
                </p>
              </div>
            ) : (
              <div className="bg-white rounded-lg p-4 border-2 border-dashed border-purple-300">
                <p className="text-gray-500 text-center">
                  Write some content and click "Generate AI Summary" to create a summary automatically
                </p>
              </div>
            )}
          </div>

          {/* Description (Manual or AI) */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              📄 Description / Excerpt
            </label>
            <textarea
              name="description"
              value={formData.description}
              onChange={(e) => {
                // Limit to 300 characters
                const value = e.target.value.substring(0, 300);
                setFormData({...formData, description: value});
              }}
              placeholder="Write a short description or use the AI-generated summary above..."
              rows="4"
              maxLength={300}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
            <div className="flex justify-between items-center mt-1">
              <p className="text-xs text-gray-500">
                This will be shown in blog previews and search results
              </p>
              <p className={`text-xs font-semibold ${
                formData.description.length > 280 ? 'text-red-600' : 'text-gray-500'
              }`}>
                {formData.description.length}/300 characters
              </p>
            </div>
          </div>

          {/* Featured Checkbox */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <label className="flex items-center space-x-3 cursor-pointer">
              <input
                type="checkbox"
                name="is_featured"
                checked={formData.is_featured}
                onChange={handleChange}
                className="w-5 h-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
              />
              <span className="text-sm font-semibold text-gray-700">
                ⭐ Mark as Featured Post
              </span>
            </label>
          </div>

          {/* Action Buttons */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex flex-wrap gap-4 justify-between items-center">
              <button
                type="button"
                onClick={() => navigate(-1)}
                className="px-6 py-3 border-2 border-gray-300 text-gray-700 font-semibold rounded-lg hover:bg-gray-50 transition-colors"
              >
                ← Cancel
              </button>

              <div className="flex gap-4">
                <button
                  type="submit"
                  onClick={(e) => handleSubmit(e, 'draft')}
                  disabled={loading || isGeneratingSummary}
                  className="px-8 py-3 bg-gray-600 text-white font-semibold rounded-lg hover:bg-gray-700 transition-colors shadow-md hover:shadow-lg disabled:opacity-50"
                >
                  💾 Save as Draft
                </button>

                <button
                  type="button"
                  onClick={(e) => handleSubmit(e, 'published')}
                  disabled={loading || isGeneratingSummary}
                  className="px-8 py-3 bg-gradient-to-r from-green-600 to-blue-600 text-white font-semibold rounded-lg hover:from-green-700 hover:to-blue-700 transition-all shadow-md hover:shadow-lg disabled:opacity-50"
                >
                  🚀 Publish Now
                </button>
              </div>
            </div>
          </div>
        </form>

        {/* Help Section */}
        <div className="mt-8 bg-blue-50 rounded-lg p-6 border-2 border-blue-200">
          <h3 className="font-semibold text-blue-900 mb-3">📚 Quick Tips:</h3>
          <ul className="space-y-2 text-sm text-blue-800">
            <li>• <strong>Markdown Support:</strong> Use # for headings, ** for bold, * for italic</li>
            <li>• <strong>AI Summary:</strong> Write at least 100 characters to generate an AI summary</li>
            <li>• <strong>Images:</strong> Upload a featured image to make your post more engaging</li>
            <li>• <strong>Tags:</strong> Add relevant tags to help readers find your content</li>
            <li>• <strong>Draft vs Publish:</strong> Save as draft to review later, or publish to make it public</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default BlogEditor;
