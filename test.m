% Specify the path to your E57 file
file_path = '/Users/home/Desktop/MAIN/Coding/e57_conversion/File Type E57 TEST Scans/1_Mudroom_Garage_and_Laundry_Door.e57';

try
    % Read the point cloud data from the E57 file
    raw_data = e57FileReader(file_path);
    ptCloud = readPointCloud(raw_data, 2);

    % Plot the point cloud
    pcshow(ptCloud);
    xlabel('X');
    ylabel('Y');
    zlabel('Z');
    title('Point Cloud from E57 File');
catch ME
    % If an error occurs, display the error message
    disp('Error occurred:');
    disp(ME.message);
end