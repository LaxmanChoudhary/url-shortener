"use client";

import { useState } from "react";

export default function Home() {
  const [inputUrl, setInputUrl] = useState("");
  const [shortenedUrl, setShortenedUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(shortenedUrl).then(
      function () {
        setCopied(true);
        setTimeout(function () {
          setCopied(false);
        }, 2000);
      },
      function (err) {
        console.error("Could not copy text: ", err);
      }
    );
  };

  const onSubmitHandler = (e: React.FormEvent) => {
    let processedUrl = inputUrl;
    // preprocess url
    if (!/^https?:\/\//i.test(processedUrl)) {
      processedUrl = "https://" + processedUrl;
      setInputUrl(processedUrl);
    }

    e.preventDefault();
    setLoading(true);
    fetch("/shorten", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url: processedUrl }),
    })
      .then((response) => response.json())
      .then((data) => {
        setShortenedUrl(data.short_url);
      })
      .catch((error) => {
        console.error("Error:", error);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  return (
    <div className="h-screen w-screen grid grid-flow-row grid-rows-3">
      {/* input section */}
      <div className="min-w-[500px] max-w-[700px] flex flex-col my-28 mx-auto col row-span-2">
        <h1 className="text-3xl font-semibold mb-4">
          <span className="text-lg tracking-wide bg-gray-100 p-2 rounded">
            🔍TinyTrail
          </span>{" "}
          URL Shortner
        </h1>
        <div className="space-y-1">
          <form className="space-x-2" onSubmit={onSubmitHandler}>
            <input
              className="w-[400px] border rounded border-gray-200 p-2"
              type="text"
              placeholder="Enter URL to shorten"
              value={inputUrl}
              onChange={(e) => setInputUrl(e.target.value)}
              required
            />
            <input
              className="border rounded p-2 hover:bg-gray-100 cursor-pointer"
              type="submit"
              value={loading ? "🤝🏽 shortening" : "✂️ shorten"}
              disabled={loading}
            />
          </form>
          {shortenedUrl && (
            <div className="border flex items-center justify-between w-fit">
              <p className="p-2 bg-gray-200 font-mono">Shortened url: </p>
              <div className="p-2 space-x-2">
                <a className="underline" href={shortenedUrl}>
                  {shortenedUrl}
                </a>
                <button
                  className="hover:scale-110 transition-all"
                  title="copy"
                  onClick={() => copyToClipboard()}
                >
                  {copied ? "✅" : "📑"}
                </button>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* steps to usage */}
      <div className="grid grid-cols-3 flex-grow row-span-1">
        <div className="bg-gray-50 flex flex-col justify-center p-4">
          <h2 className="mb-2 text-xl font-semibold text-gray-800">
            1️⃣ Generate Short URL
          </h2>
          <p className="pl-8 tracking-tight text-gray-700">
            Create a short link instantly from your long URL.
          </p>
        </div>
        <div className="bg-gray-100 flex flex-col justify-center p-4">
          <h2 className="mb-2 text-xl font-semibold text-gray-800">
            2️⃣ Share the Short URL
          </h2>
          <p className="pl-8 tracking-tight text-gray-700">
            Copy and share your short link anywhere, effortlessly.
          </p>
        </div>
        <div className="bg-gray-50 flex flex-col justify-center p-4">
          <h2 className="mb-2 text-xl font-semibold text-gray-800">
            3️⃣ Track the URL
          </h2>
          <p className="pl-8 tracking-tight text-gray-700">
            Track real-time click stats of your link.
          </p>
          <div></div>
        </div>
      </div>
    </div>
  );
}
