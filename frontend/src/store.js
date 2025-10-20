import create from 'zustand';
import api from './api';

// Initialize authentication state from localStorage
const initializeAuth = () => {
  const token = localStorage.getItem('access_token');
  const savedUser = localStorage.getItem('user');
  
  if (token && savedUser) {
    try {
      return {
        isAuthenticated: true,
        user: JSON.parse(savedUser)
      };
    } catch (error) {
      console.error('Failed to parse saved user:', error);
      localStorage.removeItem('user');
      return {
        isAuthenticated: false,
        user: null
      };
    }
  }
  
  return {
    isAuthenticated: false,
    user: null
  };
};

const initialAuthState = initializeAuth();

export const useAuthStore = create((set) => ({
  user: initialAuthState.user,
  isAuthenticated: initialAuthState.isAuthenticated,
  loading: false,
  error: null,

  login: async (username, password) => {
    set({ loading: true, error: null });
    try {
      const response = await api.post('/auth/login/', { username, password });
      // Handle both token formats: token or access/refresh
      const accessToken = response.data.access || response.data.token;
      const refreshToken = response.data.refresh || null;
      
      if (accessToken) {
        localStorage.setItem('access_token', accessToken);
      }
      if (refreshToken) {
        localStorage.setItem('refresh_token', refreshToken);
      }
      
      // Save user data to localStorage for persistence
      const userData = response.data.user || { username };
      localStorage.setItem('user', JSON.stringify(userData));
      
      set({ 
        isAuthenticated: true, 
        user: userData,
        loading: false 
      });
      return response.data;
    } catch (error) {
      const errorMsg = error.response?.data?.detail || 
                      error.response?.data?.non_field_errors?.[0] ||
                      'Login failed';
      set({ 
        error: errorMsg,
        loading: false 
      });
      throw error;
    }
  },

  logout: () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user');
    set({ isAuthenticated: false, user: null });
  },

  register: async (userData) => {
    set({ loading: true, error: null });
    try {
      // Keep password2 for backend validation
      const response = await api.post('/users/', userData);
      set({ loading: false });
      return response.data;
    } catch (error) {
      const errorData = error.response?.data;
      let errorMsg = 'Registration failed';
      
      // Handle different error formats
      if (typeof errorData === 'object') {
        if (errorData.detail) errorMsg = errorData.detail;
        else if (errorData.username) errorMsg = `Username: ${errorData.username[0]}`;
        else if (errorData.email) errorMsg = `Email: ${errorData.email[0]}`;
        else if (errorData.password) errorMsg = `Password: ${errorData.password[0]}`;
        else if (errorData.password2) errorMsg = `Confirm Password: ${errorData.password2[0]}`;
        else errorMsg = JSON.stringify(errorData);
      } else {
        errorMsg = errorData || 'Registration failed';
      }
      
      set({ 
        error: errorMsg,
        loading: false 
      });
      throw error;
    }
  },

  fetchUser: async () => {
    try {
      const response = await api.get('/users/profile/');
      const userData = response.data;
      
      // Save user data to localStorage
      localStorage.setItem('user', JSON.stringify(userData));
      
      set({ user: userData, isAuthenticated: true });
      return userData;
    } catch (error) {
      // If fetch fails, clear stored data
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      localStorage.removeItem('user');
      set({ isAuthenticated: false, user: null });
    }
  },

  // Add a method to check and restore authentication
  checkAuth: () => {
    const token = localStorage.getItem('access_token');
    const savedUser = localStorage.getItem('user');
    
    if (token && savedUser) {
      try {
        const user = JSON.parse(savedUser);
        set({ isAuthenticated: true, user });
        return true;
      } catch (error) {
        console.error('Failed to restore auth:', error);
        localStorage.removeItem('user');
        set({ isAuthenticated: false, user: null });
        return false;
      }
    }
    
    set({ isAuthenticated: false, user: null });
    return false;
  },
}));

export const useBlogStore = create((set) => ({
  blogs: [],
  selectedBlog: null,
  loading: false,
  error: null,

  fetchBlogs: async (filters = {}) => {
    set({ loading: true, error: null });
    try {
      const response = await api.get('/blogs/blogs/', { params: filters });
      const blogsData = Array.isArray(response.data) ? response.data : response.data.results || [];
      set({ blogs: blogsData, loading: false });
      return blogsData;
    } catch (error) {
      set({ blogs: [], error: error.message, loading: false });
    }
  },

  fetchBlogDetail: async (id) => {
    set({ loading: true, error: null });
    try {
      const response = await api.get(`/blogs/blogs/${id}/`);
      set({ selectedBlog: response.data, loading: false });
      return response.data;
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  createBlog: async (data) => {
    set({ loading: true, error: null });
    try {
      // If data is FormData, we need to delete Content-Type to let browser set it with boundary
      const config = {};
      if (data instanceof FormData) {
        config.headers = {
          'Content-Type': undefined, // Let browser set the correct multipart/form-data with boundary
        };
      }
      
      const response = await api.post('/blogs/blogs/', data, config);
      set((state) => ({ 
        blogs: [...state.blogs, response.data], 
        loading: false 
      }));
      return response.data;
    } catch (error) {
      const errorMsg = error.response?.data?.detail || 
                       error.response?.data?.error ||
                       Object.values(error.response?.data || {}).flat().join(', ') ||
                       error.message;
      set({ error: errorMsg, loading: false });
      throw error;
    }
  },

  updateBlog: async (id, data) => {
    set({ loading: true, error: null });
    try {
      // If data is FormData, we need to delete Content-Type to let browser set it with boundary
      const config = {};
      if (data instanceof FormData) {
        config.headers = {
          'Content-Type': undefined, // Let browser set the correct multipart/form-data with boundary
        };
      }
      
      const response = await api.put(`/blogs/blogs/${id}/`, data, config);
      set({ selectedBlog: response.data, loading: false });
      return response.data;
    } catch (error) {
      set({ error: error.message, loading: false });
      throw error;
    }
  },

  deleteBlog: async (id) => {
    set({ loading: true, error: null });
    try {
      await api.delete(`/blogs/blogs/${id}/`);
      // Remove the deleted blog from the state
      set((state) => ({
        blogs: state.blogs.filter(blog => blog.id !== id),
        selectedBlog: state.selectedBlog?.id === id ? null : state.selectedBlog,
        loading: false
      }));
      return true;
    } catch (error) {
      const errorMsg = error.response?.data?.detail || 
                       error.response?.data?.error ||
                       'Failed to delete blog';
      set({ error: errorMsg, loading: false });
      throw error;
    }
  },
}));

export const useSettingsStore = create((set) => ({
  categories: [],
  tags: [],
  loading: false,

  fetchCategories: async () => {
    try {
      const response = await api.get('/blogs/categories/');
      const categoriesData = Array.isArray(response.data) ? response.data : response.data.results || [];
      set({ categories: categoriesData });
    } catch (error) {
      console.error('Failed to fetch categories:', error);
      set({ categories: [] });
    }
  },

  fetchTags: async () => {
    try {
      const response = await api.get('/blogs/tags/');
      const tagsData = Array.isArray(response.data) ? response.data : response.data.results || [];
      set({ tags: tagsData });
    } catch (error) {
      console.error('Failed to fetch tags:', error);
      set({ tags: [] });
    }
  },
}));
