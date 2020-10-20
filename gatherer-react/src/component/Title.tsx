import React  from 'react';
import PropTypes from 'prop-types';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import AddButton from './buttons/AddButton';


interface TitleProps {
  count: number,
  // children:,
  onAddButtonClick: (e: React.MouseEvent<HTMLButtonElement>) => void
}

const useStyles = makeStyles( (theme: Theme) => 
  createStyles({
    addButton: {
      position: 'relative'
    // right: theme.spacing(3),
    }
  })
);

const Title: React.FC<TitleProps> = (props) => {
  const classes = useStyles();

  const [count, setCount] = React.useState(0);

  React.useEffect(() => {
    setCount(props.count);
  });

  return (
    <Grid container spacing={3}>
      <Grid item xs={11}>
        <Typography component="h2" variant="h6" color="primary" gutterBottom>
          {props.children} + {count}
        </Typography>
      </Grid>
      <Grid item xs={1}>
        <AddButton onClick={props.onAddButtonClick}></AddButton>
      </Grid>
    </Grid>
  );
}

export default Title;
