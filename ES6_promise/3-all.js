import uploadPhoto from './utils.js'
import createUser from './utils.js'

export default function  handleProfileSignup() {
    return  Promise.all([
        uploadPhoto,
        creatUser
    ])
        .then(([photo, user]) => {
            console.log(photo.body, user.firstName, user.lastName);
        })
        .catch(() => new Error('Signup system offline'));
}