{
  description = "YouTube Downloader Python Development Environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      # Supported systems: Linux (x86_64) and Mac (M1/M2 - aarch64)
      supportedSystems = [ "x86_64-linux" "aarch64-darwin" "x86_64-darwin" ];
      
      # Helper function to generate packages for each system
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
    in
    {
      devShells = forAllSystems (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          default = pkgs.mkShell {
            # Packages available in this environment
            packages = [
              pkgs.ffmpeg # Required for video merging and MP3 conversion
              
              # Embedding Python and yt-dlp library
              (pkgs.python3.withPackages (python-pkgs: [
                python-pkgs.yt-dlp
              ]))
            ];

            # Welcome message displayed when terminal opens
            shellHook = ''
              echo "--------------------------------------------------"
              echo "🎥 YouTube Downloader Development Environment (Nix)"
              echo "✅ Python $(python --version) and yt-dlp loaded."
              echo "✅ FFmpeg $(ffmpeg -version | head -n1 | awk '{print $3}') ready."
              echo "--------------------------------------------------"
            '';
          };
        });
    };
}
