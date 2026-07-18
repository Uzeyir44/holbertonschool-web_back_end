export default function handleResponseFromAPI(promise) {
    promise.then(() => {
        return {
            status: 200,
            body: 'success'
        };
    });

    promise.catch(() => {
        return new Error();
    });

    promise.finally(() => {
        return 'Got a response from the API to the console';
    });
}