import { useEffect, useState } from 'react'
import './App.css'

function App() {
	const [data, setData] = useState([])
	const [searchValue, setSearchValue] = useState('')
	useEffect(() => {
		console.log('fetch')
		fetch(
			`https://1103-82-112-65-1.ngrok-free.app/videos?query=${searchValue}`,
			{
				// mode: 'no-cors',
			}
		).then((res) => res.json().then(setData))
		// .then((data) => {
		// 	console.log(data)
		// 	setData(data)
		// })
	}, [searchValue])

	return (
		<>
			<input onInput={(e) => setSearchValue(e.currentTarget.value)} />
			<div>
				{data.map((row) => {
					return Object.keys(row).map((key) => {
						return (
							<div>
								{key} - {row[key]}
							</div>
						)
					})
				})}
			</div>
		</>
	)
}

export default App
