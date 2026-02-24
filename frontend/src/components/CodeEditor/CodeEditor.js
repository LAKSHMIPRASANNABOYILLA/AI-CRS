import React, { useState } from 'react';
import Editor from '@monaco-editor/react';

const LANGUAGES = ['python', 'javascript', 'typescript', 'java', 'go', 'rust', 'cpp', 'csharp'];

function CodeEditor({ onSubmit, loading }) {
  const [title, setTitle] = useState('');
  const [language, setLanguage] = useState('python');
  const [code, setCode] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title && language && code) {
      onSubmit(title, language, code);
    }
  };

  return (
    <form className="code-editor" onSubmit={handleSubmit}>
      <div className="form-row">
        <input
          type="text"
          placeholder="Review title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <select value={language} onChange={(e) => setLanguage(e.target.value)}>
          {LANGUAGES.map((lang) => (
            <option key={lang} value={lang}>{lang}</option>
          ))}
        </select>
      </div>
      <Editor
        height="400px"
        language={language}
        value={code}
        onChange={setCode}
        theme="vs-dark"
        options={{ minimap: { enabled: false }, fontSize: 14 }}
      />
      <button type="submit" disabled={loading || !code}>
        {loading ? 'Reviewing...' : 'Submit for Review'}
      </button>
    </form>
  );
}

export default CodeEditor;
