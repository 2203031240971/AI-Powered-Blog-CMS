import React, { useEffect } from 'react';
import { useBlogStore, useSettingsStore } from '../store';
import { Link } from 'react-router-dom';
import { FiEye, FiCalendar } from 'react-icons/fi';
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';

dayjs.extend(relativeTime);

const BlogList = () => {
  const { blogs, loading, fetchBlogs } = useBlogStore();
  const { fetchCategories } = useSettingsStore();

  useEffect(() => {
    fetchBlogs({ status: 'published' });
    fetchCategories();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900">Blog Posts</h1>
          <p className="mt-4 text-xl text-gray-600">Discover our latest articles and insights</p>
        </div>

        {loading ? (
          <div className="text-center">Loading...</div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {Array.isArray(blogs) && blogs.length > 0 ? (
              blogs.map((blog) => (
                <Link key={blog.id} to={`/blog/${blog.id}`}>
                  <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
                    {blog.featured_image && (
                      <img
                        src={blog.featured_image}
                        alt={blog.title}
                        className="w-full h-48 object-cover"
                      />
                    )}
                    <div className="p-6">
                      <h2 className="text-xl font-bold text-gray-900 mb-2">{blog.title}</h2>
                      <p className="text-gray-600 text-sm mb-4">{blog.description}</p>
                      
                      <div className="flex items-center text-gray-500 text-sm space-x-4">
                        <div className="flex items-center space-x-1">
                          <FiEye className="w-4 h-4" />
                          <span>{blog.views_count} views</span>
                        </div>
                        <div className="flex items-center space-x-1">
                          <FiCalendar className="w-4 h-4" />
                          <span>{dayjs(blog.published_at).fromNow()}</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </Link>
              ))
            ) : (
              <div className="col-span-full text-center text-gray-500">No blogs available</div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default BlogList;
