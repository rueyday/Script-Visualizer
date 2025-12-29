export interface VideoProcessRequest {
  file: File;
  start: number;
  end: number;
}

export interface ProcessResponse {
  message: string;
  file: string;
}