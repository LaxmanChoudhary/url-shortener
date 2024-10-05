import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "🔍TinyTrail | Shorten it, share it, track it!.",
  description:
    "Generate your short url and track it's usage for free, no signup, nothing",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
