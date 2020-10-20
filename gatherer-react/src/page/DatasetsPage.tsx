import React from 'react';
import ReactDOM from 'react-dom';
import { FileManager, FileNavigator } from '@opuscapita/react-filemanager';
import connectorNodeV1 from '@opuscapita/react-filemanager-connector-node-v1';

const apiOptions = {
    ...connectorNodeV1.apiOptions,
    apiRoot: `https://demo.core.dev.opuscapita.com/filemanager/master` // Or you local Server Node V1 installation.
  }
  
interface SFileManagerProps {
}


const SFileManager: React.FC<SFileManagerProps> = (props) => {

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
              alert(`${clickEvent.event}, ${clickEvent.number}, ${clickEvent.rowData}`);
              console.log(clickEvent.event, clickEvent.number, clickEvent.rowData);
            }
            }}
        />
      </FileManager>
    </div>
  );
}

export default SFileManager;
