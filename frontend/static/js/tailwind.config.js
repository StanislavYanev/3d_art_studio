tailwind.config = {
    darkMode: 'class',
    theme: {
      extend: {
        colors: {
          primary: {
            DEFAULT: '#4F46E5',     // bg-primary → индиго
            hover: '#4338CA',       // hover:bg-primary-hover
            light: '#6366F1',
          },
          accent: {
            DEFAULT: '#6366F1',     // text-accent → лилаво-синьо
            dark: '#818CF8',
          },
          surface: {
            DEFAULT: '#FFFFFF',     // bg-surface → бял фон
            dark: '#1F2937',        // dark:bg-surface-dark → gray-800
          },
          text: {
            base: '#1F2937',        // text-text-base → gray-800
            muted: '#6B7280',       // text-text-muted → gray-500
            dark: '#F9FAFB',        // dark:text-text-dark → white
          },
          border: {
            DEFAULT: '#E5E7EB',     // border-border → gray-200
            dark: '#374151',
          },
        },
      },
    },
  };
  