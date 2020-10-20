import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import StorageIcon from '@material-ui/icons/Storage';
import SchoolIcon from '@material-ui/icons/School';
import { Link,  BrowserRouter, Route, Switch} from 'react-router-dom';


interface ListItemLinkProps {
  icon: any,
  primary: string,
  to: string,
}


const ListItemLink: React.FC<ListItemLinkProps> = (props) => {

  const renderLink = React.useMemo(
    () => React.forwardRef<ListItemLinkProps, any>((itemProps, ref) => <Link to={props.to} ref={ref} {...itemProps} />),
    [props.to],
  );

  return (
    <li>
      <ListItem button component={renderLink}>
        {props.icon ? <ListItemIcon>{props.icon}</ListItemIcon> : null}
        <ListItemText primary={props.primary} />
      </ListItem>
    </li>
  );
}

export const mainListItems: JSX.Element = (
    <div>
      <ListItemLink to="/dataset" primary="Dataset" icon={<StorageIcon />} />
      <ListItemLink to="/train" primary="Train" icon={<SchoolIcon />} />
    </div>
);
