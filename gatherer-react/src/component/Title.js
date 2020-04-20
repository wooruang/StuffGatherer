import React, { useState, useEffect }  from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import AddButton from './buttons/AddButton';


const useStyles = makeStyles((theme) => ({
  addButton: {
    position: 'left'
    // right: theme.spacing(3),
  },
}));

export default function Title(props) {
  const classes = useStyles();

  const [count, setCount] = useState(0);

  useEffect(() => {
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
        <AddButton className={classes.addButton} onClick={props.onAddButtonClick}></AddButton>
      </Grid>
    </Grid>
  );
}

Title.propTypes = {
  children: PropTypes.node,
};