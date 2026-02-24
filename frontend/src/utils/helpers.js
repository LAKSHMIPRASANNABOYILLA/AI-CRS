export function formatDate(dateStr) {
  return new Date(dateStr).toLocaleString();
}

export function truncate(str, maxLength = 80) {
  if (!str) return '';
  return str.length > maxLength ? str.slice(0, maxLength) + '...' : str;
}
