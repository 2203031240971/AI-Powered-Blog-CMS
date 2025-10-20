import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { toast } from 'react-toastify';
import { useBlogStore, useAuthStore } from '../store';

const UserProfile = () => {
  const { user, isAuthenticated } = useAuthStore();
  const { blogs, fetchBlogs, loading, deleteBlog } = useBlogStore();
  const [deleting, setDeleting] = useState(null);
  const [myBlogs, setMyBlogs] = useState([]);
  const [profileLoading, setProfileLoading] = useState(true);

  useEffect(() => {
    // Fetch only current user's blogs and store locally to compute stats reliably
    let mounted = true;
    const load = async () => {
      setProfileLoading(true);
      try {
        // First, try to fetch ALL blogs to see if any exist in the database
        console.log('Fetching all blogs first to debug...');
        const allBlogs = await fetchBlogs({});
        console.log('All blogs in database:', allBlogs);
        
        // Now fetch user's blogs specifically
        if (user && user.id) {
          console.log('User data:', user);
          console.log('Fetching blogs for user ID:', user.id);
          const data = await fetchBlogs({ author: user.id });
          if (mounted) {
            setMyBlogs(Array.isArray(data) ? data : []);
            console.log('User blogs fetched:', data);
          }
        } else {
          console.warn('User not available or missing id:', user);
          if (mounted) setMyBlogs([]);
        }
      } catch (err) {
        console.error('Error fetching blogs:', err);
        if (mounted) setMyBlogs([]);
      } finally {
        if (mounted) setProfileLoading(false);
      }
    };
    load();
    return () => { mounted = false; };
  }, [user, fetchBlogs]);

  // Use the fetched list for stats and display
  const userBlogs = myBlogs;

  const handleDelete = async (id, title) => {
    const confirmMessage = `Are you sure you want to delete "${title}"?\n\nThis action cannot be undone!`;
    
    if (window.confirm(confirmMessage)) {
      setDeleting(id);
      try {
        await deleteBlog(id);
        toast.success('Blog deleted successfully!', {
          position: "top-right",
          autoClose: 3000,
        });
        // Refresh the local blog list
        try {
          const data = await fetchBlogs({ author: user.id });
          setMyBlogs(Array.isArray(data) ? data : []);
        } catch (e) {
          setMyBlogs([]);
        }
      } catch (error) {
        console.error('Failed to delete blog:', error);
        toast.error(error.response?.data?.detail || 'Failed to delete blog. Please try again.', {
          position: "top-right",
          autoClose: 5000,
        });
      } finally {
        setDeleting(null);
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-6xl mx-auto px-4">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">My Dashboard</h1>
              <p className="text-gray-600 mt-2">
                Welcome back, <span className="font-semibold">{user?.username || user?.email}</span>!
              </p>
            </div>
            <Link
              to="/blog/create"
              className="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-lg hover:from-blue-700 hover:to-purple-700 transition-all shadow-md hover:shadow-lg"
            >
              ✍️ Create New Blog
            </Link>
          </div>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="flex items-center">
              <div className="p-3 bg-blue-100 rounded-full">
                <svg className="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <div className="ml-4">
                <p className="text-gray-500 text-sm">Total Blogs</p>
                <p className="text-2xl font-bold text-gray-900">{userBlogs.length}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="flex items-center">
              <div className="p-3 bg-green-100 rounded-full">
                <svg className="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div className="ml-4">
                <p className="text-gray-500 text-sm">Published</p>
                <p className="text-2xl font-bold text-gray-900">
                  {userBlogs.filter(b => b.status === 'published').length}
                </p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="flex items-center">
              <div className="p-3 bg-yellow-100 rounded-full">
                <svg className="w-8 h-8 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div className="ml-4">
                <p className="text-gray-500 text-sm">Drafts</p>
                <p className="text-2xl font-bold text-gray-900">
                  {userBlogs.filter(b => b.status === 'draft').length}
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* My Blogs */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">My Blogs</h2>
          
          {profileLoading || loading ? (
            <div className="text-center py-12">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
              <p className="text-gray-600 mt-4">Loading your blogs...</p>
            </div>
          ) : userBlogs.length === 0 ? (
            <div className="text-center py-12">
              <svg className="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              <p className="text-gray-600 text-lg mb-4">You haven't created any blogs yet</p>
              <Link
                to="/blog/create"
                className="inline-block px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-colors"
              >
                Create Your First Blog
              </Link>
            </div>
          ) : (
            <div className="space-y-4">
              {userBlogs.map((blog) => (
                <div key={blog.id} className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h3 className="text-xl font-semibold text-gray-900">{blog.title}</h3>
                        <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                          blog.status === 'published' 
                            ? 'bg-green-100 text-green-800' 
                            : 'bg-yellow-100 text-yellow-800'
                        }`}>
                          {blog.status === 'published' ? '✓ Published' : '📝 Draft'}
                        </span>
                        {blog.is_featured && (
                          <span className="px-3 py-1 rounded-full text-xs font-semibold bg-purple-100 text-purple-800">
                            ⭐ Featured
                          </span>
                        )}
                      </div>
                      <p className="text-gray-600 mb-2">{blog.description || 'No description'}</p>
                      <div className="flex items-center gap-4 text-sm text-gray-500">
                        <span>📅 {new Date(blog.created_at).toLocaleDateString()}</span>
                        {blog.category && <span>🏷️ {blog.category.name}</span>}
                        <span>👁️ {blog.views_count} views</span>
                        {blog.tags && blog.tags.length > 0 && (
                          <span>🔖 {blog.tags.length} tags</span>
                        )}
                      </div>
                    </div>
                    <div className="flex gap-2 ml-4">
                      <Link
                        to={`/blog/${blog.id}`}
                        className="px-4 py-2 bg-blue-100 text-blue-700 rounded-lg hover:bg-blue-200 transition-colors text-sm font-medium"
                      >
                        View
                      </Link>
                      <Link
                        to={`/blog/${blog.id}/edit`}
                        className="px-4 py-2 bg-green-100 text-green-700 rounded-lg hover:bg-green-200 transition-colors text-sm font-medium"
                      >
                        Edit
                      </Link>
                      <button
                        onClick={() => handleDelete(blog.id, blog.title)}
                        disabled={deleting === blog.id}
                        className={`px-4 py-2 rounded-lg transition-colors text-sm font-medium flex items-center gap-2 ${
                          deleting === blog.id 
                            ? 'bg-gray-300 text-gray-500 cursor-not-allowed' 
                            : 'bg-red-100 text-red-700 hover:bg-red-200'
                        }`}
                      >
                        {deleting === blog.id ? (
                          <>
                            <svg className="animate-spin h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            Deleting...
                          </>
                        ) : (
                          <>
                            🗑️ Delete
                          </>
                        )}
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default UserProfile;
