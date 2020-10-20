

import React from 'react';
import { makeStyles, Theme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import { Switch, Route } from 'react-router-dom';

import Chart from '../Chart';
import Deposits from '../Deposits';
import Orders from '../Orders';
import SFileManager from './DatasetsPage';

interface MainPageProps {
    paperClassName : string
}

const MainPage: React.FC<MainPageProps> = (props) => {

  return (
      <Grid container>
        <Grid item xs={12}>
          <Paper className={props.paperClassName}>
            <Switch>
              <Route path="/dataset">
                <SFileManager/>
              </Route>
              <Route path="/train">
                <Deposits />
              </Route>
            </Switch>
          </Paper>
        </Grid>
      </Grid>
  );
}

export default MainPage;
