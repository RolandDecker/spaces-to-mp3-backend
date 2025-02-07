import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import axios from "axios";

export default function SpacesDownloader() {
  const [url, setUrl] = useState("");
  const [downloadLink, setDownloadLink] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleDownload = async () => {
    setLoading(true);
    try {
      const response = await axios.post("/api/download", { url });
      setDownloadLink(response.data.download_url);
    } catch (error) {
      console.error("Error processing the request", error);
      alert("Failed to process the Space URL");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4">
      <Card className="w-full max-w-lg p-6 shadow-lg">
        <CardContent>
          <h1 className="text-xl font-bold mb-4">X Spaces to MP3 Downloader</h1>
          <Input
            type="text"
            placeholder="Paste X Spaces URL here"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="mb-4"
          />
          <Button onClick={handleDownload} disabled={loading}>
            {loading ? "Processing..." : "Convert to MP3"}
          </Button>
          {downloadLink && (
            <a
              href={downloadLink}
              download
              target="_blank"
              rel="noopener noreferrer"
              className="block mt-4 text-blue-600 hover:underline"
            >
              Download MP3
            </a>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
