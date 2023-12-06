import {FC} from 'react'

interface props{
  id:string
}

export const SpotifyCard:FC<props> = ({id}) => {
  return (
    <iframe width="25%" height="152" className='rounded-lg min-w-[280px]' src={`https://open.spotify.com/embed/track/${id}?utm_source=generator&amp;theme=0`} frameBorder={0} allowFullScreen allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
  )
}
