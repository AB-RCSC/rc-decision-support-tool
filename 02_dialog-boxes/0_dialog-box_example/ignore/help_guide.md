# Operational Metrics Dashboard
The Operational Metrics Dashboard is your all-in-one tool for analyzing key performance metrics.

# Table of Contents
[About](#about)  
[Staying Connected](#staying-connected)  
[Widgets](#widgets)  
* [Basis for All Visuals](#basis-for-all-visuals)
* [Trailing 12-Months](#trailing-12-months)
* [Date Range](#date-range)
* [Model](#model)
* [Client](#client)
* [Metrics](#metrics)
* [Kolmogorov-Smirnov Diagnostics](#kolmogorov-smirnov-ks-diagnostics)
* [Checkbox Group](#checkbox-group)
<br><br>

# About
This dashboard corresponds to version 2.0, reflecting the current production model.

# Staying Connected
Stay connected to the dashboard via the VPN.  Should you become disconnected simply reconnect to the VPN.

# Widgets
## Basis for All Visuals
Tailor the context of the visuals from two different perspectives:
* **List Date:**  Observe not only what has been listed and recovered as a direct result of those listings.  
* **Close Date:**  Whenever we discuss revenue generated, it is from the perspective of the Close Date.  

## Trailing 12-Months
Selecting this checkbox:
* Adjusts the [Date Range](#date-range) and greys them out.
* Displays an interactive line chart with Client-specific trendlines.

## Date Range
Set a custom timeframe for visuals using the Date Pickers, Start Date and End Date.

![Alt text](images/datepicker.jpg)

## Model
Select 2.0 or 1.0. The [Date Range](#date-range) defaults accordingly. 

## Client
The visuals can be holistic or specific to individual Clients based on account listings or closings within the timeframe specified in the [Date Range](#date-range).

The checkboxes in the rectangular frame are only active under the following conditions:
* 'All Clients' is selected.
* The 'Actual' radio button is chosen in [Metrics](#metrics).

## Metrics
Forecasted metrics are only active under the following conditions:
* 'All Clients' is selected in the [Client dropdown](#client).\n\
* 2.0 is selected in the [Model dropdown](#model).\n\
* 'List Date' radio button is selected in the [Basis for All Visuals](#basis-for-all-visuals).

## Kolmogorov-Smirnov (KS) Diagnostics
KS statistics measure the discriminatory power of a model.

## Checkbox Group
When you select "All Clients" from the [Client dropdown](#client), the 13 analytic checkboxes within the rectagular frame become active.