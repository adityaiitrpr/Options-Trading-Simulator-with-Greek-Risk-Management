# Options Pricing and Greeks Analysis

## Contact info

Email: saimanishprabhakar2020@gmail.com

[Linkedin](https://www.linkedin.com/in/saimanish-prabhakar-3074351a0/)

## Project Overview

### Key Features

#### Customisable Option Parameters
Users can dynamically input and adjust: Option Type (Call/Put), Underlying Asset Price, Strike Price, Time to Expiration, Risk-Free Interest Rate, Volatility, Dividend Yield, and Monte Carlo Simulation Count

#### Visualisation and Analysis

1. **Options Pricing Insights**
   - Visual analysis of option prices
   - Sensitivity visualisations for: Volatility, Time to Expiration, Strike Price

2. **Monte Carlo Simulation**

   - **Visual Path Simulation**: 
     - Configurable display of 1-50 sample price paths (limited for visualisation purposes)
     - Interactive graph showing possible price evolution scenarios
   - **Pricing Calculation**:
     - Utilises 10,000 simulation paths by default for accurate price estimation
     - Configurable simulation count parameter for balancing precision and performance
   - **Price Distribution Analysis**:
     - Histogram showing distribution of final prices across all simulation paths
     - Statistical summary of simulation results

4. **Comprehensive Greeks Analysis**
   - First-Order Greeks: Delta, Gamma, Theta, Vega, Rho
   - Second-Order Greeks: Charm, Speed, Color, Zomma, Veta, Volga

#### Comparative Visualization
- Bar charts include a 'Difference %' metric
- Compares Black-Scholes and Monte Carlo method results
- Provides insight into model accuracy and deviation

#### Multi-Dimensional Sensitivity Plots

Based on Black-Scholes Greeks:
- Delta Surface: (Greek, Volatility, Stock Price)
- Gamma Surface: (Greek, Volatility, Stock Price)
- Vega Surface: (Greek, Volatility, Stock Price)
- Theta Surface: (Greek, Time to Expiration, Stock Price)
- Rho Surface: (Greek, Risk-Free Rate, Stock Price)

## Built with

- <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">

- <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">

- <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib">

- <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">

- <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">

- <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy">

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your_username/options-pricing-and-greeks.git
cd options-pricing-and-greeks
```
### 2. Create Virtual Environment (Optional but Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install required libraries
pip install -r requirements.txt

# When done working on the project
deactivate
```
### Alternative: Direct Installation
```bash
# If you prefer not to use a virtual environment, you can directly install dependencies
pip install -r requirements.txt
```
### 3. Change git remote url to avoid accidental pushes to base project
```bash
git remote set-url origin github_username/options-pricing-and-greeks
git remote -v # confirm the changes
```

## Usage

### Step-by-Step image walkthrough of project

Adjust the default values of the parameters listed in the sidebar to your liking. 

![User Inputs](images/User_Input_Parameters.png)

If you're unsure about any parameter, hover over the question mark symbol for additional context.

![User Input - Help Functionality](images/Help_Functionality_User_Inputs.png)

As you adjust inputs, all visualisations update in real-time, comparing Black-Scholes and Monte Carlo pricing for both Call and Put options. The comparison graph shows pricing differences with a percentage deviation metric.

![Options Price Comparison](images/Example_Options_Price_Comparison_Graph.png)

The next section demonstrates how options prices respond to changes in key factors:

![Options Price - Volatility Sensitivity](images/Example_Volatility_Sensitivity_Options_Price_graph.png)

![Options Price - Time to Expiration Sensitivity](images/Example_TimetoExpiration_Options_Price_graph.png)

![Options Price - Strike Price Sensitivity](images/Example_StrikePriceSensitivity_Options_Price_graph.png)

The interactive Monte Carlo simulation graph allows you to visualize between 1-50 sample price paths using the slider and 'Generate New Paths' button. Note that this is for visualisation only and differs from the calculation model.

![Monte Carlo Option Price Path](images/Example_Monte_Carlo_Price_Sim_Paths_graph.png)

A histogram displays the distribution of option prices from 10,000 Monte Carlo simulations (default), along with key statistics.

![Monte Carlo Options Price Path Histogram](images/Example_Monte_Carlo_Price_Distribution_graph.png)

Beyond pricing, the application analyses option Greeks (both first and second order) through tabular presentation:

![Greeks Analysis Table](images/Example_Greeks_Analysis_Tables.png)

These Greeks are also visualised graphically using the same comparative format as the pricing charts. Below are examples of first and second-order Greek analyses:

![First Order Greek Analysis - Delta](images/Example_FirstOrderGreeks_Delta_graph.png)

![Second Order Greek Analysis - Volga](images/Example_SecondOrderGreeks_Volga_graph.png)

Finally, the application features interactive 3D sensitivity plots based on Black-Scholes Greeks. These plots show relationships between each Greek, relevant parameters (such as volatility, time-to-expiration, or risk-free rate), and stock price. 

We use "multi-dimensional sensitivity plots" terminology since different Greeks are primarily influenced by different parameters. A dropdown menu lets you explore various Greeks with full interactive controls for panning, zooming, and rotation.

For demonstration purposes, only the Delta sensitivity surface is displayed in this documentation.

![Multi-Dimensional Sensitivity Plot - Delta](images/BS_Multi-Dimensional_Sensitivity_Delta_Plot.png)

## FAQ, Assumptions, Limitations, and Development Challenges

This implementation represents one of several possible approaches to options pricing modeling, necessitating specific technical decisions and architectural trade-offs. 

For transparency and educational purposes, I have documented all underlying assumptions, limitations, and development challenges in the comprehensive [TECHNICAL_NOTES.md](TECHNICAL_NOTES.md) file
which also guides you on interpretation of certain plots such as the - 

- Multi-Dimensional Sensitivity Greeks Plots
- Monte Carlo Options Price Paths

## Future Improvements

- American Option Support: Implement early exercise capability using Least Squares Monte Carlo or binomial tree methods.
- Stochastic Volatility Models: Implement Heston, SABR, or local volatility models to better capture volatility smile/skew.

## Greeks 101

**First-Order Greeks**

   Delta (Δ): Measures rate of change in option price with respect to underlying price
   - First derivative of option price with respect to spot price (∂V/∂S)
   - Represents hedge ratio (number of shares needed to hedge option)
   - Range: 0 to 1 for calls, -1 to 0 for puts
   - Used for: Directional risk management, basic hedging strategies
   
   Gamma (Γ): Measures rate of change in Delta with respect to underlying price
   - Second derivative of option price with respect to spot price (∂²V/∂S²)
   - Shows how much Delta changes for a $1 move in underlying
   - Always positive for both calls and puts
   - Used for: Dynamic hedging, risk assessment of large price moves
   
   Theta (Θ): Measures rate of change in option price with respect to time
   - First derivative of option price with respect to time (-∂V/∂t)
   - Represents time decay of option value
   - Usually negative (options lose value over time)
   - Used for: Time decay management, premium selling strategies
   
   Vega (ν): Measures rate of change in option price with respect to volatility
   - First derivative of option price with respect to volatility (∂V/∂σ)
   - Shows sensitivity to volatility changes
   - Always positive for vanilla options
   - Used for: Volatility risk management, volatility trading
   
   Rho (ρ): Measures rate of change in option price with respect to interest rate
   - First derivative of option price with respect to interest rate (∂V/∂r)
   - Shows sensitivity to interest rate changes
   - Used for: Interest rate risk management, rarely primary concern


**Second-Order Greeks**

   Charm: Rate of change of Delta with respect to time
   - Mixed derivative (∂²V/∂S∂t)
   - Shows how Delta changes as time passes
   - Used for: Maintaining Delta-hedges over time
   
   Speed: Rate of change of Gamma with respect to underlying price
   - Third derivative of option price (∂³V/∂S³)
   - Shows how Gamma changes with large price moves
   - Used for: Risk management of large market moves
   
   Color: Rate of change of Gamma with respect to time
   - Mixed derivative (∂²V/∂S²∂t)
   - Shows how Gamma changes as time passes
   - Used for: Gamma trading strategies over time
   
   Zomma: Rate of change of Gamma with respect to volatility
   - Mixed derivative (∂³V/∂S²∂σ)
   - Shows how Gamma changes with volatility
   - Used for: Volatility risk in Gamma trading
   
   Veta: Rate of change of Vega with respect to time
   - Mixed derivative (∂²V/∂σ∂t)
   - Shows how volatility sensitivity changes over time
   - Used for: Long-term volatility trading
   
   Volga: Rate of change of Vega with respect to volatility
   - Second derivative (∂²V/∂σ²)
   - Also known as Vega convexity
   - Used for: Advanced volatility trading strategies

## Mathematics of Black-Scholes and Monte Carlo models

**Black-Scholes Model**

   The Black-Scholes partial differential equation that option prices must satisfy:
   
   $$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial 
   V}{\partial S} - rV = 0$$

   Where:
   - $$V$$ is the option price
   - $$S$$ is the underlying asset price
   - $$t$$ is time
   - $$\sigma$$ is volatility
   - $$r$$ is the risk-free interest rate

   **Closed-Form Solution**

   **For a European call option:**
   
   $$C(S, t) = S \cdot e^{-q(T-t)} \cdot N(d_1) - K \cdot e^{-r(T-t)} \cdot N(d_2)$$

   **For a European put option:**
   
   $$P(S, t) = K \cdot e^{-r(T-t)} \cdot N(-d_2) - S \cdot e^{-q(T-t)} \cdot N(-d_1)$$

   Where:
   - $$d_1 = \frac{\ln(S/K) + (r - q + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}$$
   - $$d_2 = d_1 - \sigma\sqrt{T-t}$$
   
   And:
   - $$N(x)$$ is the cumulative distribution function of the standard normal distribution
   - $$K$$ is the strike price
   - $$T$$ is the expiration time
   - $$q$$ is the dividend yield



**Monte Carlo Simulation**

   Monte Carlo methods rely on the risk-neutral valuation principle, which states that the option price is the 
   expected payoff discounted at the risk-free rate:
   
   $$V_0 = e^{-rT} \mathbb{E}^Q[V_T]$$
   
   Where:
   - $$V_0$$ is the current option price
   - $$V_T$$ is the option payoff at expiration
   - $$\mathbb{E}^Q$$ is the expectation under the risk-neutral measure

   **Geometric Brownian Motion**
   
   Under the risk-neutral measure, the underlying asset price follows:
   
   $$dS_t = (r - q)S_t dt + \sigma S_t dW_t$$
   
   Where:
   - $$dW_t$$ is a Wiener process (standard Brownian motion)

   **Discretization**

   For simulation, we discretize the continuous process:
   
   $$S_{t+\Delta t} = S_t \exp\left((r - q - \frac{\sigma^2}{2})\Delta t + \sigma \sqrt{\Delta t} \cdot Z\right)$$
   
   Where:
   - $$Z \sim N(0,1)$$ is a standard normal random variable
   - $$\Delta t$$ is the time step

   **Monte Carlo Estimator**

   The option price is estimated as:
   
   $$V_0 \approx e^{-rT} \frac{1}{N} \sum_{i=1}^{N} V_T^{(i)}$$

   Where:
   - $$N$$ is the number of simulations
   - $$V_T^{(i)}$$ is the payoff from the $$i$$-th simulation

   **Error Estimation**
   
   The standard error of the Monte Carlo estimate is:
   
   $$SE = \frac{\sigma_{MC}}{\sqrt{N}}$$

   Where:
   - $$\sigma_{MC}$$ is the standard deviation of the simulated payoffs

## Contributing

I hope you find some value from this project, and wish that it serves you well in your journey towards mastering options.

If you would like to contribute to the development of the options pricing and greeks analysis project, please:

1. Feel free to clone the repository to your local machine (follow the steps in the 'Getting Started' section)
2. Make your contribution, and then submit a pull request.
3. Use the discussions tab within the repository and raise issues if needed.
