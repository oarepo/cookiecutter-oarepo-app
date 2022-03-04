// This file is part of InvenioRDM
// Copyright (C) 2020-2022 CERN.
// Copyright (C) 2020-2021 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
// Copyright (C) 2021 New York University.
//
// Invenio App RDM is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.
{%- raw %}
import {
  SearchAppFacets,
  SearchAppResultsPane,
} from '@js/invenio_search_ui/components'
import { i18next } from '@translations/{%- endraw %}{{cookiecutter.package_name}}{%- raw %}/i18next'
import _get from 'lodash/get'
import _truncate from 'lodash/truncate'
import React, { Component } from 'react'
import {
  Count,
  Pagination,
  ResultsList,
  ResultsPerPage,
  SearchBar,
  Sort,
} from 'react-searchkit'
import { Container, Grid, Segment } from 'semantic-ui-react'

import Overridable from 'react-overridable'

export function DashboardResultView(props) {
  const { sortOptions, paginationOptions, currentResultsState } = props
  const { total } = currentResultsState.data
  return (
    total && (
      <Grid>
        <Grid.Row>
          <Grid.Column width={16}>
            <Segment>
              <Grid>
                <Overridable id="DashboardResultView.resultHeader" {...props}>
                  <Grid.Row
                    verticalAlign="middle"
                    className="small padding-tb-5 deposit-result-header"
                  >
                    <Grid.Column width={4}>
                      <Count
                        label={() => (
                          <>
                            {total} {i18next.t('result(s) found')}
                          </>
                        )}
                      />
                    </Grid.Column>
                    <Grid.Column
                      width={12}
                      textAlign="right"
                      className="padding-r-5"
                    >
                      {sortOptions && (
                        <Sort
                          values={sortOptions}
                          label={(cmp) => (
                            <>
                              {i18next.t('Sort by')} {cmp}
                            </>
                          )}
                        />
                      )}
                    </Grid.Column>
                  </Grid.Row>
                </Overridable>
                <Overridable id="DashboardResultView.resultList" {...props}>
                  <Grid.Row>
                    <Grid.Column>
                      <ResultsList />
                    </Grid.Column>
                  </Grid.Row>
                </Overridable>
              </Grid>
            </Segment>
          </Grid.Column>
        </Grid.Row>
        <Overridable id="DashboardResultView.resultFooter" {...props}>
          <Grid.Row verticalAlign="middle">
            <Grid.Column width={4}></Grid.Column>
            <Grid.Column width={8} textAlign="center" floated="right">
              <Pagination
                options={{
                  size: 'mini',
                  showFirst: false,
                  showLast: false,
                }}
              />
            </Grid.Column>
            <Grid.Column textAlign="right" width={4}>
              <ResultsPerPage
                values={paginationOptions.resultsPerPage}
                label={(cmp) => (
                  <>
                    {' '}
                    {cmp} {i18next.t('results per page')}
                  </>
                )}
              />
            </Grid.Column>
          </Grid.Row>
        </Overridable>
      </Grid>
    )
  )
}

export const DashboardSearchLayoutHOC = ({
  searchBarPlaceholder = '',
  newBtn = () => null,
  ...props
}) => {
  const DashboardUploadsSearchLayout = (props) => (
    <Container>
      <Grid>
        <Grid.Row columns={3}>
          <Grid.Column width={4} />
          <Grid.Column width={8}>
            <SearchBar placeholder={searchBarPlaceholder} />
          </Grid.Column>
          <Grid.Column width={4}>{newBtn}</Grid.Column>
        </Grid.Row>
        <Grid.Row>
          <Grid.Column width={4}>
            <SearchAppFacets aggs={props.config.aggs} />
          </Grid.Column>
          <Grid.Column width={12}>
            <SearchAppResultsPane layoutOptions={props.config.layoutOptions} />
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Container>
  )
  return DashboardUploadsSearchLayout
}
{%- endraw %}
