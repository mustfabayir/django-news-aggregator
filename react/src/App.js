import { Routes, Route } from 'react-router-dom'
import News from './components/News'
import NewsDetails from './components/NewsDetails'
function App() {
  return (
    <div>
		<header>
			<h1><a href="index.html">Hello World</a></h1>
	
		</header>
	
	
		<div id="secwrapper">
	
			<section>
        <Routes>
          <Route path="/" element={<News/>}/>
          <Route path=":id" element={<NewsDetails/>}/>
        </Routes>
			</section>
		</div>
	
	
	</div>
  );
}

export default App;
