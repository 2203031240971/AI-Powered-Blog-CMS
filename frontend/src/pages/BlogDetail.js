import React, { useEffect, useState } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { toast } from 'react-toastify';
import { useBlogStore, useAuthStore } from '../store';
import ReactMarkdown from 'react-markdown';
import dayjs from 'dayjs';

const BlogDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { selectedBlog, loading, fetchBlogDetail, deleteBlog } = useBlogStore();
  const { user, isAuthenticated } = useAuthStore();
  const [deleting, setDeleting] = useState(false);

  useEffect(() => {
    if (id) {
      fetchBlogDetail(id);
    }
  }, [id, fetchBlogDetail]);

  const isAuthor = isAuthenticated && selectedBlog && (
    selectedBlog.author === user?.username || 
    selectedBlog.author === user?.email ||
    selectedBlog.author_id === user?.id
  );

  const handleDelete = async () => {
    const confirmMessage = `Are you sure you want to delete "${selectedBlog.title}"?\n\nThis action cannot be undone!`;
    
    if (window.confirm(confirmMessage)) {
      setDeleting(true);
      try {
        await deleteBlog(id);
        toast.success('Blog deleted successfully!', {
          position: "top-right",
          autoClose: 3000,
        });
        // Redirect to home page after deletion
        navigate('/');
      } catch (error) {
        console.error('Failed to delete blog:', error);
        toast.error(error.response?.data?.detail || 'Failed to delete blog. Please try again.', {
          position: "top-right",
          autoClose: 5000,
        });
        setDeleting(false);
      }
    }
  };

  if (loading) return <div className="text-center py-12">Loading...</div>;

  if (!selectedBlog) return <div className="text-center py-12">Blog not found</div>;

  return (
    <div className="bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8">
        {/* Author Actions - Show if user is the author */}
        {isAuthor && (
          <div className="mb-6 pb-6 border-b border-gray-200 flex justify-end gap-3">
            <Link
              to={`/blog/${id}/edit`}
              className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors text-sm font-medium flex items-center gap-2"
            >
              ✏️ Edit Blog
            </Link>
            <button
              onClick={handleDelete}
              disabled={deleting}
              className={`px-4 py-2 rounded-lg transition-colors text-sm font-medium flex items-center gap-2 ${
                deleting 
                  ? 'bg-gray-300 text-gray-500 cursor-not-allowed' 
                  : 'bg-red-600 text-white hover:bg-red-700'
              }`}
            >
              {deleting ? (
                <>
                  <svg className="animate-spin h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Deleting...
                </>
              ) : (
                <>
                  🗑️ Delete Blog
                </>
              )}
            </button>
          </div>
        )}

        <h1 className="text-4xl font-bold text-gray-900 mb-4">{selectedBlog.title}</h1>
        
        <div className="flex items-center justify-between mb-8 text-gray-600">
          <div>
            <span className="font-semibold">{selectedBlog.author}</span>
            <span className="mx-2">•</span>
            <span>{dayjs(selectedBlog.published_at).format('MMMM D, YYYY')}</span>
          </div>
          <span>{selectedBlog.views_count} views</span>
        </div>

        {selectedBlog.featured_image && (
          <img
            src={selectedBlog.featured_image}
            alt={selectedBlog.title}
            className="w-full h-96 object-cover rounded-lg mb-8"
          />
        )}

        {selectedBlog.ai_summary && (
          <div className="bg-blue-50 border-l-4 border-blue-600 p-6 mb-8">
            <h3 className="text-lg font-semibold text-blue-900 mb-2">AI Summary</h3>
            <p className="text-blue-800">{selectedBlog.ai_summary.summary}</p>
            {selectedBlog.ai_summary.key_points && (
              <div className="mt-4">
                <h4 className="font-semibold text-blue-900 mb-2">Key Points:</h4>
                <ul className="list-disc list-inside text-blue-800">
                  {selectedBlog.ai_summary.key_points.map((point, idx) => (
                    <li key={idx}>{point}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}

        <div className="prose prose-lg max-w-none">
          <ReactMarkdown>{selectedBlog.content}</ReactMarkdown>
        </div>

        <div className="mt-8 pt-8 border-t border-gray-200">
          <h3 className="text-xl font-bold text-gray-900 mb-4">Comments</h3>
          {selectedBlog.comments?.length > 0 ? (
            <div className="space-y-4">
              {selectedBlog.comments.map((comment) => (
                <div key={comment.id} className="bg-gray-50 p-4 rounded">
                  <div className="font-semibold text-gray-900">{comment.author}</div>
                  <p className="text-gray-700 mt-2">{comment.content}</p>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-gray-600">No comments yet</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default BlogDetail;
