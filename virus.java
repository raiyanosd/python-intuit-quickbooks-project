public static void main(String[] args) {

    File source = new File("sourceFile.txt");
    File destination = new File("destinationFile.txt");

    try {
        //Creating a file stream from source file
        FileInputStream inputStream = new FileInputStream(source);
        //Creating a file stream to destination file
        FileOutputStream outputStream = new FileOutputStream(destination);

        //Copy file content byte-by-byte
        int byteRead;
        while ((byteRead = inputStream.read()) != -1) {
            outputStream.write(byteRead);
        }

        //Close streams
        inputStream.close();
        outputStream.close();

        //Printing the success message
        System.out.println("File copied successfully.");

    } catch (IOException e) {
        System.out.println("Error occurred while copying file: " + e.getMessage());
    }


}
