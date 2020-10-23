import React from 'react';
import ReactDOM from 'react-dom';
import { FileManager, FileNavigator } from '@opuscapita/react-filemanager';
import connectorNodeV1 from '@opuscapita/react-filemanager-connector-node-v1';
import ImgDialog from '../component/dialogs/ImgDialog'

const apiOptions = {
    ...connectorNodeV1.apiOptions,
    // apiRoot: `https://demo.core.dev.opuscapita.com/filemanager/master` // Or you local Server Node V1 installation.
    apiRoot: `http://localhost:8000/api/datasets`
  }

interface SFileManagerProps {
}


const SFileManager: React.FC<SFileManagerProps> = (props) => {

  const [openViewerDialog, setOpenViewerDialog] = React.useState(false);
  const [viewerSource, setViewerSource] = React.useState('');
  const [viewerFileName, setViewerFileName] = React.useState('');

  const handleCloseViewerDialog = () => {
    setOpenViewerDialog(false);
  };



  return  (
    <div style={{ height: '480px' }}>
      <FileManager>
        <FileNavigator
          id="filemanager-1"
          api={connectorNodeV1.api}
          apiOptions={apiOptions}
          capabilities={connectorNodeV1.capabilities}
          listViewLayout={connectorNodeV1.listViewLayout}
          viewLayoutOptions={connectorNodeV1.viewLayoutOptions}
          onResourceItemDoubleClick={(clickEvent)=>{
            if (clickEvent.rowData.type !== 'dir') {
              // alert(`${clickEvent.event}, ${clickEvent.number}, ${clickEvent.rowData}`);
              console.log(clickEvent.event, clickEvent.number, clickEvent.rowData);
              setViewerSource(`${apiOptions['apiRoot']}/download?items=${clickEvent.rowData.id}`);
              setViewerFileName(clickEvent.rowData.name);
              setOpenViewerDialog(true);
            }
            }}
        />
      </FileManager>
      <ImgDialog open={openViewerDialog} source={viewerSource} fileName={viewerFileName} handleClose={handleCloseViewerDialog} />
    </div>
  );
}

export default SFileManager;
