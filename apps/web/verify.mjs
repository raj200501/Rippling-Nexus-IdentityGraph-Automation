import fs from 'fs'
const required = ['src/App.tsx', 'src/pages/OrgGraphPage.tsx', 'src/styles/theme.css']
for (const file of required) {
  if (!fs.existsSync(new URL(file, import.meta.url))) {
    console.error(`Missing ${file}`)
    process.exit(1)
  }
}
console.log('web checks passed')
