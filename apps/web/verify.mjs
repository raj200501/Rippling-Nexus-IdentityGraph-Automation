import fs from 'fs'

const required = ['index.html', 'src/preview.js', 'src/styles/theme.css']
for (const file of required) {
  if (!fs.existsSync(new URL(file, import.meta.url))) {
    console.error(`Missing ${file}`)
    process.exit(1)
  }
}

const preview = fs.readFileSync(new URL('src/preview.js', import.meta.url), 'utf8')
if (!preview.includes('Boot OK')) {
  console.error('Boot OK panel is missing from preview app')
  process.exit(1)
}

const navLinks = (preview.match(/\['\//g) || []).length
if (navLinks < 3) {
  console.error('Expected at least 3 navigation routes in preview app')
  process.exit(1)
}

console.log('web checks passed')
